import socket
import random

def primitive_root(p):
    options_primitive = []
    for i in range(1, 11):
        options = []
        for j in range(1, p):
            ans = (i ** (j)) % p
            # print(ans)
            options.append(ans)
        # print("Options",options)
        # CHECK IF PRIMITIVE
        yesno = check_primitive(options, p, i)
        if (yesno == 1):
            options_primitive.append(i)
    print("Primitive root options are", options_primitive)
    return  options_primitive


def check_primitive(options, p, num):
    # options_primitive=[]
    for i in range(1, p):
        flag = 0
        for j in range(0, p - 1):
            if (i == options[j]):
                flag = 1
        if (flag == 0):
            break
    if (flag == 1):
        # options_primitive.append(num)
        # print("Num is primitive root",num)
        return 1
    return 0

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    P = 23
    print("Value of P : ", P)

    list = primitive_root(P)
    G = list[-1]
    print("Value of G : ", G)

    a = 4
    x = (G ** a) % P

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    data = conn.recv(1024).decode()
    print("Public key from B: " + str(data))
    ka = (int(data) ** a) % P
    data = str(x)
    conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection

    print("The secret common key is", ka)

if __name__ == '__main__':
    server_program()
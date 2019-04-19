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
    return options_primitive


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

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    P = 23

    list_of_numbers = primitive_root(P)
    G = list_of_numbers[-1]
    b = 3

    y = (G ** b) % P
    message = str(y)

    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Public key from A: ' + data)  # show in terminal
    client_socket.close()  # close the connection

    print(data)
    kb = (int(data) ** b) % P
    print("The secret common key is", kb)

if __name__ == '__main__':
    client_program()
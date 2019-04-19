import random

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def main():

    msgs = input("Enter message string")
    p = int(input("Enter value of p(prime number) : "))
    q = int(input("Enter value of q(prime number) : "))

    # p = 53
    # q = 61
    encry = ""
    decry = ""
    print("Random prime numbers are:\np =", p, "\tq = ", q)
    n = p * q

    print("\nValue of N = ", n)
    e = 2

    a = 1
    phi = (p - 1) * (q - 1)
    print("\nphi((p - 1)*(q - 1)): ", phi)
    print("List of possible relative prime numbers")
    k = 2
    while e < phi:
        if gcd(e, phi) == 1:
            print(e, end="  ")
            a += 1
            if a / 10 == 1:
                break
            e += 1
        else:
            e += 1

    e = int(input("\nEnter any of the the above relative prime numbers : "))
    # print("\nValue of encrypt (1< e < phi) = ", e)


    k = 1
    while True:
        if (1 + (k * phi)) % e == 0:
            d = int((1 + (k * phi)) / e)
            break
        k += 1
        
    print("\nPrivate key is : ", d)

    for i in range(0, len(msgs)):
        msg = ord(msgs[i])

        c = msg ** e % n
        encry = encry + str(c)

        m = c ** d % n
        decry = decry + chr(m)

    print("\nEncrypted data = ", encry)
    print("\nOriginal Message Sent = ", decry)

if __name__ == "__main__":
    main()
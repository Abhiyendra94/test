p10 = [3,5,2,7,4,10,1,9,8,6]
p8 = [6,3,7,4,8,5,10,9]
IP8 = [2,6,3,1,4,8,5,7]
EP = [4,1,2,3,2,3,4,1]
key = input("Enter the key")
s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,1]]
s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
p4 = [2,4,3,1]
IPInverse = [4,1,3,5,7,2,8,6]
def leftShift(a):
    x = a[0]
    for i in range(0, 4):
        a[i] = a[i+1]
    a[4] = x
    return a

def calculateBinary(a):
    b = 0
    if a == 0:
        b = [0, 0]
    else:
        for i in range(0, len(a)):
            temp = 2**i
            b = temp * a[len(a)-i-1] + b
    return b

def decodeBinary(a):
    b = []
    for i in range(0,2):
        b.append(a%2)
        a = int(a/2)

    # reverse
    c = []
    for i in range(0, len(b)):
        c.append(b[len(b)-i-1])

    return c

def takeXOR(a, b):
    c =[]
    for i in range(0,len(a)):
        c.append(int(a[i]) ^ int(b[i]))

    return c
def tableConversion(a, b):
    c = []
    for i in range(0, len(b)):
        c.append(a[b[i]-1])
    return c

def preConditions():
    p10Key = []
    p10Key = tableConversion(key, p10)

    L = p10Key[0:5]
    R = p10Key[5:10]

    L = leftShift(L)
    R = leftShift(R)

    combo = L + R
    print(combo)

    Key1 = tableConversion(combo, p8)

    for i in range(0,2):
        L = leftShift(L)
        R = leftShift(R)

    combo = L + R

    Key2 = tableConversion(combo,p8)

    print("Key1", Key1)
    print("Key2", Key2)

    return Key1, Key2

def subEncription(keys,X,Y):
    OP = tableConversion(X, EP)
    print("Expanded", OP)

    OPXOR = takeXOR(OP, keys)
    print("OPXOR", OPXOR)

    L1 = OPXOR[0:4]
    R1 = OPXOR[4:8]

    m = []
    m.append(L1[0])
    m.append(L1[3])
    n = []
    n.append(L1[1])
    n.append(L1[2])


    m = calculateBinary(m)
    n = calculateBinary(n)

    x = []
    x.append(R1[0])
    x.append(R1[3])

    y = []
    y.append(R1[1])
    y.append(R1[2])

    x = calculateBinary(x)
    y = calculateBinary(y)

    m = s0[m][n]
    n = s1[x][y]
    print(m)
    m = decodeBinary(m)
    n = decodeBinary(n)



    p4key = m + n

    print("p4key", p4key)

    p4key = tableConversion(p4key, p4)
    p4key = takeXOR(p4key, Y)
    return p4key

def CipherEncryption(key1, key2):
    # Step1 IP table conversion
    plaintext = input("Enter input plain text")
    o1 = tableConversion(plaintext, IP8)
    print("o1", o1)
    L = o1[0:4]
    R = o1[4:8]

    # step2 Fk function key1
    L = subEncription(key1, R, L)

    # Step3 swap
    temp = R.copy()
    R = L.copy()
    L = temp.copy()

    # step4 Fk function key2
    L = subEncription(key2, R, L)
    encrypted = L + R

    # step5 IP Inverse table conversion
    encrypted = tableConversion(encrypted, IPInverse)

    print("Encrypted:", encrypted)
    return encrypted


def CipherDecryption(key1, key2, encrypted):
    # step1 IP table convert
    text = tableConversion(encrypted, IP8)
    L = text[0:4]
    R = text[4:8]

    # step2 Fk key2 conversion
    L = subEncription(key2, R, L)

    # step3 swap
    temp = R.copy()
    R = L.copy()
    L = temp.copy()

    # step4 Fk key1 conversion
    L = subEncription(key1, R, L)
    decrypted = L + R

    # step5 IPInverse table conversion
    decrypted = tableConversion(decrypted, IPInverse)
    print("Decrypted", decrypted)

    return decrypted

def main():
    print("#################Prerequisites###############")
    key1, key2 = preConditions()
    print("#################Encryption##############")
    encrypted = CipherEncryption(key1, key2)
    print("#################Decryption##############")
    CipherDecryption(key1, key2, encrypted)
if __name__ == "__main__":
    main()

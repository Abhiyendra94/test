Sbox = ["1001", "0100", "1010", "1011", "1101", "0001", "1000", "0101", "0110", "0010", "0000", "0011", "1100", "1110", "1111", "0111"]

SboxInverse = ["1010", "0101", "1001", "1011", "0001", "0111", "1000", "1111", "0110", "0000", "0010", "0011", "1100", "0100", "1101", "1110"]
HexMul = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
[0, 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14]]

hexmul = []
fixmat1 = [[1, 4],[4, 1]]
fixmat2 = [[9, 2],[2, 9]]
#key = 0100101011110101
#text = 1101011100101000
def takeXOR(a, b):
    c =[]
    for i in range(0, len(a)):
        c.append(int(a[i]) ^ int(b[i]))
    return c

def calculateBinary(a):
    b = 0
    if a == 0:
        b = [0, 0]
    else:
        for i in range(0, len(a)):
            temp = 2**i
            b = temp * int(a[len(a)-i-1]) + b
    return b

def rotNib(a):
    a0 = a[0:4]
    a1 = a[4:8]
    a = a1 + a0
    return a

def subNib(a):
    a0 = Sbox[calculateBinary(a[0:4])]
    a1 = Sbox[calculateBinary(a[4:8])]
    a = a0 + a1
    return a

def keyGeneration(key0):
    w0 = key0[0:8]
    w1 = key0[8:16]

    w2 = takeXOR(w0, "10000000")
    w2 = takeXOR(w2, subNib(rotNib(w1)))

    w3 = takeXOR(w2, w1)

    w4 = takeXOR(w2, "001100000")
    w4 = takeXOR(w4, subNib(rotNib(w3)))

    w5 = takeXOR(w4, w3)

    key1 = w2 + w3
    key2 = w4 + w5

    print("Key0", key0)
    print("Key1", key1)
    print("Key2", key2)

    return key1, key2

def convertToList(a1):
    a2 =[]
    for i in range(0,len(a1)):
        a2.append(a1[i])
    return a2

def swapPositions(temp):
    temp = convertToList(temp)
    for i in range(0, 4):
        x = temp[i+4]
        temp[i+4] = temp[i+12]
        temp[i+12] = x
    return temp

def convertToMat(temp):
    mat = [[temp[0:4], temp[8:12]], [temp[4:8], temp[12:16]]]
    return mat

def convertMatTo(temp):
    x = []
    for i in range(0,4):
        for j in range(0,4):
            x.append(temp[i][j])

    return x

def decodeBinary(a):
    b = []
    for i in range(0, 4):
        b.append(a%2)
        a = int(a/2)

    # reverse
    c = []
    for i in range(0, len(b)):
        c.append(b[len(b)-i-1])

    return c

def mulHexMat(a, b):
    x = []
    for i in range(0, 2):
        for j in range(0, 2):
            temp = "0000"
            for k in range(0, 2):
                temp = takeXOR(temp, decodeBinary(HexMul[a[i][k]][calculateBinary(b[k][j])]))
            x.append(temp)

    temp = []
    temp.append(x[0])
    temp.append(x[2])
    temp.append(x[1])
    temp.append(x[3])
    return temp

def ecryption(key0, key1, key2):
    plaintext = input("Enter plain text")
    print("\n//////////////Encryption////////////")
    temp = takeXOR(plaintext, key0)
    print("Add round key0 : ", temp)
    print("///////Round 1///////")
    a1 = ""
    for i in range(0, 4):
        a1 = a1 + Sbox[calculateBinary((temp[i*4:i*4+4]))]
    print("Substitute nibble : ", a1)
    a1 = swapPositions(a1)
    print("Shift rows : ", a1)
    a1 = convertToMat(a1)
    mul = mulHexMat(fixmat1, a1)
    print("Mix columns : ", mul)
    mul = convertMatTo(mul)
    r1 = takeXOR(mul, key1)
    print("Add round key1 : ", r1)
    a1 = ""
    for i in range(0, 4):
        a1 = a1 + Sbox[calculateBinary((r1[i * 4:i * 4 + 4]))]
    print("///////Round 2///////")
    print("Substitute nibble : ", a1)
    a1 = swapPositions(a1)
    print("Shift rows : ", a1)
    r2 = takeXOR(a1, key2)
    print("Add round key2 Encryption : ", r2)
    decryption("0010010011101100", key0, key1, key2)

def decryption(en, key0, key1, key2):
    print("\n//////////////Decryption////////////")
    r2 = takeXOR(en, key2)
    print("Add round key2 : ", r2)
    s1 = swapPositions(r2)
    print("Shift row : ", s1)
    a1 = ""
    for i in range(0, 4):
        a1 = a1 + SboxInverse[calculateBinary(s1[i * 4:i * 4 + 4])]
    print("Substitute inverse nibble : ", a1)
    a1 = takeXOR(a1, key1)
    print("Add round key1 : ", a1)
    mat = convertToMat(a1)
    mul = mulHexMat(fixmat2, mat)
    print("Mix columns : ", mul)
    mul = convertMatTo(mul)
    s1 = swapPositions(mul)
    print("Shift row : ", s1)
    d1 = ""
    for i in range(0, 4):
        d1 = d1 + SboxInverse[calculateBinary(s1[i*4: i*4+4])]
    print("Substitute inverse nibble : ", d1)
    decrypted = takeXOR(d1, key0)
    print("After round key0 Decrypted : ", decrypted)

def main():
    key0 = input("Enter the key")
    key1, key2 = keyGeneration(key0)
    ecryption(key0, key1, key2)

if __name__== "__main__":
    main()
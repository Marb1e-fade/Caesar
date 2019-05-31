engLower = []
engUpper = []
symbols = []


for i in range(65, 91):
    engUpper.append(chr(i))
for i in range(97, 123):
    engLower.append(chr(i))

for i in range(32, 64):
    symbols.append(chr(i))
for i in range(91, 97):
    symbols.append(chr(i))
for i in range(123, 127):
    symbols.append(chr(i))

def CaesarEncrypt(msg, key):
    encMsg = ''
    for i in range(0, len(msg)):
        nKey = int(ord(msg[i])) + key - 26
        print(nKey)
        if msg[i] in symbols:
            continue
        elif ord(msg[i]) + key > 90 and msg[i] in engUpper:
            ch = chr(nKey)
        elif ord(msg[i]) + key > 122 and msg[i] in engLower:
            ch = chr(nKey)
        else:
            ch = chr(ord(msg[i]) + key)
        encMsg += ch
    return encMsg

def CaesarDecrypt(msg, key):
    decMsg = ''
    for i in range(0, len(msg)):
        nKey = int(ord(msg[i])) - key + 26
        if msg[i] in symbols:
            continue
        elif ord(msg[i]) - key < 65 and msg[i] in engUpper:
            ch = chr(nKey)
        elif ord(msg[i]) - key < 97 and msg[i] in engLower:
            ch = chr(nKey)
        else:
            ch = chr(ord(msg[i]) - key)
        decMsg += ch
    return decMsg

key = int(input("Input a key: "))
msg = input("Enter a message: ")
while key > 26:
    key -= 26

encMsg = CaesarEncrypt(msg, key)
decMsg = CaesarDecrypt(encMsg, key)
print(encMsg)
print(decMsg)

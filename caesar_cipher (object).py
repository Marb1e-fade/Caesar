class caesar:
    engLower = []
    engUpper = []
    symbols = []

    def __init__(self, msg, key):
        self.set_language()
        self.change_message(msg)
        self.change_key(key)

    def change_message(self, msg):
        self.msg = msg

    def change_key(self, key):
        self.key = key

    def set_language(self):
        for i in range(65, 91):
            self.engUpper.append(chr(i))
        for i in range(97, 123):
            self.engLower.append(chr(i))

        for i in range(32, 64):
            self.symbols.append(chr(i))
        for i in range(91, 97):
            self.symbols.append(chr(i))
        for i in range(123, 127):
            self.symbols.append(chr(i))

    def encrypt(self):
        encMsg = ''
        for i in range(0, len(self.msg)):
            nKey = int(ord(self.msg[i])) + self.key - 26
            # print(nKey)
            if self.msg[i] in self.symbols:
                continue
            elif ord(self.msg[i]) + self.key > 90 and self.msg[i] in self.engUpper:
                ch = chr(nKey)
            elif ord(self.msg[i]) + self.key > 122 and self.msg[i] in self.engLower:
                ch = chr(nKey)
            else:
                ch = chr(ord(self.msg[i]) + self.key)
            encMsg += ch
        return encMsg

    def decrypt(self):
        msg = self.encrypt()
        decMsg = ''
        for i in range(0, len(msg)):
            nKey = int(ord(msg[i])) - self.key + 26
            if msg[i] in self.symbols:
                continue
            elif ord(msg[i]) - self.key < 65 and msg[i] in self.engUpper:
                ch = chr(nKey)
            elif ord(msg[i]) - self.key < 97 and msg[i] in self.engLower:
                ch = chr(nKey)
            else:
                ch = chr(ord(msg[i]) - self.key)
            decMsg += ch
        return decMsg

if __name__ == "__main__":
    msg = input("Enter your message: ")
    key = int(input("Enter an integer key: "))
    while key >= 26:
        key -= 26
    CAESAR = caesar(msg, key)
    print(CAESAR.encrypt())
    print(CAESAR.decrypt())

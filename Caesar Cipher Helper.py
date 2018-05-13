class CaesarCipher(object):
    def __init__(self, shift):
        self.shift=shift%26

    def encode(self, x):
        x=x.lower()
        n=str()
        for i in range(len(x)):
            if ord(x[i]) in range(97,123):
                if (ord(x[i])+self.shift)>122:
                    a=97+ord(x[i])+self.shift-123
                    n=n+chr(a)
                else:
                    n=n+chr(ord(x[i])+self.shift)
            else:
                n=n+x[i]
        return n.upper()
    def decode(self, x):
        x=x.lower()
        n=str()
        for i in range(len(x)):
            if ord(x[i]) in range(97,123):
                if (ord(x[i])-self.shift)<97:
                    a=122+ord(x[i])-self.shift-96
                    n=n+chr(a)
                else:
                    n=n+chr(ord(x[i])-self.shift)
            else:
                n=n+x[i]
        return n.upper()
c = CaesarCipher(5);
#print(c.encode("ashiraghav"))
print(c.decode("FXMNWFLMFA"))
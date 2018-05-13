import string
def rot13(message):
    message=list(message)
    a=""
    for x in range(len(message)):
        print(message[x])
        if message[x] in string.ascii_lowercase:
            if string.ascii_lowercase.index(message[x]) >12:
                a+=string.ascii_lowercase[(string.ascii_lowercase.index(message[x])-13)]
            else:
                a+=string.ascii_lowercase[(string.ascii_lowercase.index(message[x])+13)]
        elif message[x] in string.ascii_uppercase:
            if string.ascii_uppercase.index(message[x]) >12:
                a+=string.ascii_uppercase[(string.ascii_uppercase.index(message[x])-13)]
            else:
                a+=string.ascii_uppercase[(string.ascii_uppercase.index(message[x])+13)]
        else:
            a+=message[x]
    return a
print(rot13("EBG13 rknzcyr."))
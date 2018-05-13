import re
def is_valid_IP(strng):
    try:
        x=strng.split(".")
        if bool(re.match(r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$",strng)):
            for i in x:
                if not (int(i)<=255 and int(i)>=0):
                    return False
            for i in x:
                if i!="0":
                    if i[0]=='0':
                        return False
            return True
        else:
            return False
    except:
        return False
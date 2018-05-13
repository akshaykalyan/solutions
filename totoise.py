from datetime import datetime, timedelta
def race(v2, v1, g):
    ls=[]
    x=g/(v1/3600-v2/3600)
    print(x)
    sec = timedelta(seconds=x)
    d = datetime(1,1,1) + sec
    ls.append(d.hour)
    ls.append(d.minute)
    ls.append(d.second)
    return ls
print(race(720, 850, 70))

import re,os,shutil
playlist=open("C:\\Best of the best.wpl","r")
r=playlist.read()
r=r.replace("&amp;","&")
r=r.replace("Ð¾Ñ‚","от")
r=r.replace("&apos;","'")
r=r.replace("â–¶","▶")
patern=re.compile("\w:.+\.mp3|\w:.+\.wav|\w:.+\.wma|\w:.+\.m4a")
ls=patern.findall(r)
for x in range(len(ls)):
    #print(ls[x])
    shutil.copy2(ls[x],"D:new")

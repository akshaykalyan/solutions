from ftplib import FTP
ftp = FTP('files.000webhost.com')
ftp.login("megasensortk","excision2307")
ftp.cwd("public_html")
#ftp.delete("index.html")
#print("aawww")
#ftp.retrbinary('RETR index.html', open('index.html', 'wb').write)
filename="index.html"
ftp.storbinary("STOR "+filename,open(filename,'rb'))
ftp.quit()
print("aawww")
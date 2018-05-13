import re
def domain_name(url):
    x=re.search(r"((://www)|(://)|(www))(\.)?(.+)\.",url).group(0)
    print(x)
    if x != None:
	    x=x.lstrip("://www.")
	    x=x.lstrip("://")
	    x=x.lstrip("www.")
	    x=x.rstrip(".")
    return x
print(domain_name("http://google.com"))
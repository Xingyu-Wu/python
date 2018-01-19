import re
import urllib.request
def getlink(url):
	headers = ("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux) Gecko/20100101 Firefox/57.0")
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	urllib.request.install_opener(opener)
	file = urllib.request.urlopen(url)
	data = str(file.read())
	pat = '(https?://[^\s]+\.(\w|/)*)'
	link=re.compile(pat).findall(data)
	link=list(set(link))
	return link

url="http://blog.csdn.net/"
linklist=getlink(url)
for link in linklist:
	print(link[0])

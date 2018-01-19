import re
from bs4 import BeautifulSoup
import requests
import bs4

def getHtmlText(url):
	try:
		req = requests.get(url,timeout=30)
		req.raise_for_status()
		req.encoding = req.apparent_encoding
		return req.text
	except:
		return ""

def fillUnivList(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('td')#等价于：tds = tr.find_all('td')
			ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def printUnivList(ulist,num):
	print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format("排名","学校名称","地区","总分"))
	for i in range(num):
		u=ulist[i]
		print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format(u[0],u[1],u[2],u[3]))

def main():
	ulist=[]
	url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
	html=getHtmlText(url)
	fillUnivList(ulist,html)
	printUnivList(ulist,50)


main()

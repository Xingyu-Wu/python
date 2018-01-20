import re
import requests
import urllib.request

def getHtmalText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:	
		print("error")
		return ""

def parsePage(ilt,html):
	try:
		plt = re.findall(r'\"view_price\":\"[\d\.]*\"',html)
		tlt = re.findall(r'\"title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])#//plt[i]-->第i个商品，plt[i].split(':')-->分割"view_price":"59.00"，得到view_price和价格，\
			#plt[i].split(':')[1]-->取价格那边数据	
			title = eval(tlt[i].split(':')[1])
			ilt.append([price,title])#注意这里的[]
	except:
		print("")

def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名"))#打印表头
	count = 0
	for g in ilt:
		count = count + 1
		print(tplt.format(count,g[0],g[1]))

def main():
	headers = ("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux) Gecko/20100101 Firefox/57.0")
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	urllib.request.install_opener(opener)
	goods = "书包"
	depth = 2
	start_url = "https://s.taobao.com/search?q="+goods
	#start_url = "https://s.taobao.com/search?q="+goods
	infolist = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44+i)
			#url = start_url
			html = getHtmalText(url)
			parsePage(infolist,html)
		except:
			continue

	printGoodsList(infolist)	

main()

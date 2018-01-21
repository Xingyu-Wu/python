import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def getStockList(lst, stockURL):
	html = getHTMLText(stockURL)
	soup = BeautifulSoup(html,'html.parser')
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
			#print(lst)
		except:
			continue	

def getStockInfo(lst, stockURL, fpath):
	for stock in lst:
		url = stockURL + stock + ".html"
		html = getHTMLText(url)
		try:
			if html == '':
				continue
			infoDict = {}
			soup = BeautifulSoup(html,'html.parser')
			stockInfo = soup.find('div',attrs={r'class=\"stock-bets\"'})
			name = stockInfo.findall(attrs={'bets-name'})[0]
			infoDict.update({'股票名称':name.text.split()[0]})
			keyList = stockInfo.find_all('dt')
			valueList = stockInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[1].text
				val = valueList[1].text
				infoDict[key] = val
			with open(fpath,'a',encoding='utf-8') as f:
				f.write(infoDict+'\n')
		except:
			traceback.print_exc()
			continue
	return ""

def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = '/home/huey-pc/python/getTaobaoProduct/Stock.txt'
	slist = []
	getStockList(slist,stock_list_url)
	getStockInfo(slist,stock_info_url,output_file)
	
main()
	



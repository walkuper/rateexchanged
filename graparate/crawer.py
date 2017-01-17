# -*- coding: utf8 -*-
def DataPipe(cncode='USD'):
	from bs4 import BeautifulSoup as bs
	import requests
	import sys
	import json
	sys.setdefaultencoding='utf8'
	lineArr = []

	namedict={u"銀行名稱":"bankname",
              u"現鈔買入":"billbuy",
              u"現鈔賣出":"billsell",
              u"即期買入":"spotbuy",
              u"即期賣出":"spotsell",
              u"更新時間":"refreshtime",
              u"現鈔手續費":"charge"}


	cndict={
	       "USD":"http://www.findrate.tw/USD/#.WGUjWVN97IU",
	       "JPY":"http://www.findrate.tw/JPY/#.WH5AFlN97IU",
	       "CNY":"http://www.findrate.tw/CNY/#.WH5ANFN97IU",
	       "EUR":"http://www.findrate.tw/EUR/#.WH5AT1N97IU",
	       "HKD":"http://www.findrate.tw/HKD/#.WH5AbVN97IU",
	       "GBP":"http://www.findrate.tw/GBP/#.WH5BWVN97IU",
	       "AUD":"http://www.findrate.tw/AUD/#.WH5BdVN97IU"
	}

	result = ''
	resultArr = []
	#urlToVisit = 'http://www.findrate.tw/USD/#.WGUjWVN97IU'
	urlToVisit = cndict[cncode]
	response = requests.get(urlToVisit)
	html = response.content
	soup = bs(html,"html.parser")		
	thline = soup.find('body').findAll('table')[1].findAll('th')
	trs=soup.find('body').findAll('table')[1].findAll('tr')
	
	itrcnt = 0
	itdcnt = 0
	for tr in trs:
		'''
		if itrcnt >1:
			break
		'''
		
		if itrcnt == 0:
			for td in tr:
				try:
					lineArr.append(namedict[td.text])
					#lineArr.append(td.text)
				except AttributeError:
					pass
		else:
			itdcnt = 0
			datadict = {}
			for td in tr:
				try:
					datadict[lineArr[itdcnt]] =  td.text
					itdcnt += 1
				except AttributeError:
					pass
			resultArr.append(datadict)
			
		itrcnt += 1        

    #print (json.dumps(resultArr, encoding="UTF-8", ensure_ascii=False))
	#result = json.dumps(resultArr, encoding="UTF-8", ensure_ascii=False)
	result = json.dumps(resultArr,ensure_ascii=False)
	print (result)
	return result

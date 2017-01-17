# -*- coding: utf8 -*-
def DataPipe():
	from bs4 import BeautifulSoup as bs
	import requests
	import sys
	import json
	sys.setdefaultencoding='utf8'
	lineArr = []

	namedict={u"type":"currencytype",
              u"現鈔買入":"Exrate",
              u"現鈔賣出":"UTC"}

	result = ''
	resultArr = []
	urlToVisit = 'https://tw.rter.info/capi.php'
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

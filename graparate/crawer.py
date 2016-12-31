def DataPipe(request):
	from bs4 import BeautifulSoup as bs
	import requests
	import sys
	import json
	sys.setdefaultencoding='utf8'
	lineArr = []
	
	result = ''
	resultArr = []
	urlToVisit = 'http://www.findrate.tw/USD/#.WGUjWVN97IU'
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
					lineArr.append(td.text)
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
	
		
        #print json.dumps(resultArr, encoding="UTF-8", ensure_ascii=False)
	result = json.dumps(resultArr, encoding="UTF-8", ensure_ascii=False)
	return result

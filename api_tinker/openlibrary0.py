import urllib
import json
import isbndb

key = isbndb.key()
base = 'http://isbndb.com/api/v2/json/' + key + '/book/'

while True:
	isbn = raw_input('Enter isbn: ')
	if len(isbn) < 1: break
	if isbn.lower() == 'zen': isbn = '9784770013514'
	isbn = isbn.translate(None, '-. ')
	url = base + isbn
	uh = urllib.urlopen(url)
	data = uh.read()
	try: js = json.loads(str(data))
	except: js = None
	try:
		result = js['data'][0].get('title_long')
	except:
		result = 'No title found for isbn of ' + isbn
	print result

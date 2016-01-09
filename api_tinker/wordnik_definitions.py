#wordnik
import string
import urllib
import json
import wordnik

key = wordnik.key()
url_prefix = 'http://api.wordnik.com:80/v4/word.json/'
url_suffix = '/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key='

error_msg = "No result. Note whitespace, punctuation and numerals are not valid. Please choose another word to lookup."

while True:
	word = raw_input('Lookup what word? ')
	if len(word) < 1: break
	word = word.translate(None, string.punctuation)
	word = word.translate(None, string.whitespace)
	word = word.translate(None, string.digits)
	if len(word) < 1: # calls may be rate limited
		print error_msg
		continue
	url = url_prefix + word + url_suffix + key
	uh = urllib.urlopen(url)
	data = uh.read()
	try: js = json.loads(str(data))
	except: js = None
	if len(js) < 1:
		print error_msg
		continue
	for item in js:
		print item['text']

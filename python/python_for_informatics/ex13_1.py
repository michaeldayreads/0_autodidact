import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
  address = raw_input('Enter location: ')
  result = 'No country code found in data.'
  if len(address) < 1 :
  	break
  url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
  print 'Retrieving', url
  uh = urllib.urlopen(url)
  data = uh.read()
  print 'Retrieved',len(data),'characters'
  try: js = json.loads(str(data))
  except: js = None
  if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data
    continue
  try:
  	for first in js["results"][0]:
  		for second in js["results"][0][first]:
  			if type(second) != dict : continue
  			if second.get('types') != [u'country',u'political'] :continue
  			result = second.get('short_name')
  except:
  	print 'Portion of data not iterable, possible result:', result
  	continue
  print result

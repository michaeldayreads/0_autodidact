import urllib
import socket # to set timeout, so not a rude bot
socket.setdefaulttimeout(2)

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

while True:
	url = raw_input('Enter a url: ')
	check_for_exit(url)
	if url == '':
		url = 'http://www.dr-chuck.com/page1.htm'
		print 'Using default: ', url
	try:
		fhand = urllib.urlopen(url)
		alldata = ''
		for line in fhand:
			alldata = alldata + line
		# headers if error
		header_end = alldata.find('\r\n\r\n') if (alldata.find('200 OK') > 0) else 0
		print 'Intersting length: ', len(alldata.strip()[header_end:])
		print 'Preview\n-------\n' + alldata.strip()[header_end:3000] + '\n------\nend preview'
		continue
	except:
		print url, '\nNot valid ... Please enter a valid url: '

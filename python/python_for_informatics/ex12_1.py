import socket
import re

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
		host = re.findall('http[s]?://([^/]+)', url)[0]
		print host
		get_url = 'GET ' + url + ' HTTP/1.0\n\n'
		mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mysock.settimeout(2)
		mysock.connect((host, 80))
		break
	except:
		print 'Please enter a valid url: '

mysock.send(get_url)
alldata = ''

while True:
    data = mysock.recv(512)
    alldata = alldata + data
    if ( len(data) < 1 ) :
        break

mysock.close()
print alldata

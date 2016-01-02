import socket
import re

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

while True:
	url = raw_input('Enter a url: ')
	check_for_exit(url)
	if url == '':
		url = 'GET ' + 'http://www.dr-chuck.com/page1.htm' + ' HTTP/1.0\n\n'
		print 'Using default: ', url
	try:
		host = re.findall('http[s]?://(.+?)/', url)[0]
		# html = urllib.urlopen(url).read()
		mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mysock.connect((host, 80))
		break
	except:
		print 'Please enter a valid url: '

mysock.send(url)

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

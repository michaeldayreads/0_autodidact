import socket

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
		words = url.split('/')
		host = words[2]
		url = 'GET ' + url + ' HTTP/1.0\n\n'
		mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mysock.connect((host, 80))
		break
	except:
		print url, '\nNot valid ... Please enter a valid url: '

mysock.send(url)
alldata = ''

while True:
    data = mysock.recv(512)
    alldata = alldata + data
    if ( len(data) < 1 ) :
        break

mysock.close()

# headers if error
# should meet criteria for exercise 12.5 - open to comments if you believe I am missing something
header_end = alldata.find('\r\n\r\n') if (alldata.find('200 OK') > 0) else 0

print 'Intersting length: ', len(alldata.strip()[header_end:])
print 'Preview\n-------\n' + alldata.strip()[header_end:3000] + '\n------\nend preview'

import sys

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		sys.exit()

allthewords = dict()
filename = raw_input('Enter a filename: ')
while True:
	check_for_exit(filename)
	if filename == '':
		filename = 'words.txt'
		print 'Using default: ', filename
	try:
		fhand = open(filename)
		break
	except:
		print 'Please enter a valid filename: '

for line in fhand:
	words = line.split()
	for word in words:
		word = word.replace('{','')
		word = word.replace('}','')
		word = word.replace('\\','')
		if word in allthewords: continue
		allthewords[word] = 'tbd'

print filename + ' has been read into memory.'

while True:
 	command = raw_input('Check for what value? ')
 	check_for_exit(command)
 	if command in allthewords:
 		state = 'in'
 	else:
 		state = 'not in'
 	print command + ' is ' + state + ' the dictionary!'

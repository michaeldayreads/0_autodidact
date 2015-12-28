import string

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

while True:
	filename = raw_input('Enter a filename: ')
	check_for_exit(filename)
	if filename == '':
		filename = 'mbox-short.txt'
		print 'Using default: ', filename
	try:
		fhand = open(filename)
		break
	except:
		print 'Please enter a valid filename: '

letters = dict()

for line in fhand:
	line = line.translate(None, string.punctuation)
	line = line.translate(None, string.whitespace)
	line = line.translate(None, string.digits)
	line = line.lower()
	for char in line:
		letters[char] = letters.get(char, 0) + 1

fhand.close()

data = list()
for letter, count in letters.items():
	data.append((count, letter))

data.sort(reverse=True)

for row in data:
	count, letter = row
	print count, letter

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

days = dict()
error_check = 0
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

for line in fhand:
	words = line.split()
	if len(words) < 3 or line.find('From ', 0) != 0 or line.count('@') != 1 : continue
	error_check = error_check + 1
	days[words[2]] = days.get(words[2],0) +1

print days
error_check = error_check - sum(days.values())
print 'Lines that passeed the guardian logic in excess of total count:', error_check
fhand.close()

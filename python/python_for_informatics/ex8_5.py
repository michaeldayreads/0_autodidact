import sys

contacts = list()
counts = list()
filename = raw_input('Enter a filename: ')
while True:
	if filename.lower == 'quit':
		sys.exit()
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
	if len(words) < 7 or line.find('From', 0) != 0 or line.count('@') != 1: continue
	email = words[1]
	#print email
	try:
		match = contacts.index(email)
		counts[match] = counts[match] + 1
	except:
		if email.find('@') < 1: continue
		contacts.append(email)
		counts.append(1)
for index, contact in enumerate(contacts):
	print 'Contact: ' + contact + ' -- ' + str(counts[index]) + ' emails.'
print '-------\nTotal count: ' + str(sum(counts))

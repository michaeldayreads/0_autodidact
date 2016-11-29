def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

domains = dict()
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
	key = words[1]
	key = key[(key.find('@')+1):]
	domains[key] = domains.get(key,0) +1
fhand.close()

most = max(domains.values())
locquacious = dict() # in case there are ties
for domain, count in domains.iteritems():
	if count == most: locquacious[domain] = count

print 'Domains and domain count from them:', domains
error_check = error_check - sum(domains.values())
if error_check > 0: print 'Lines that passeed the guardian logic in excess of total count:', error_check
print 'Domain(s) sending most email:', locquacious

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

hours = dict()
lines_matched = 0
extracted_values = 0 

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
	if line.find('From ', 0) != 0 or line.count(':') != 2 : continue
	lines_matched += 1
	hours[line[-14:-12]] = hours.get(line[-14:-12], 0) + 1
fhand.close()

data = list()
for hours, count in hours.items():
	data.append((int(hours), hours, count))

data.sort()

for row in data:
	order, hours, count = row
	print hours, count
	extracted_values = extracted_values + count

error_check = lines_matched - extracted_values
if error_check != 0: print 'Lines that passed the guardian logic not equal to total extracted value count:', error_check

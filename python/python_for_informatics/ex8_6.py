numbers = list()
while True:
	value = raw_input('Enter a number: ')
	if value == 'done':
		break
	try:
		int(value)
		numbers.append(value)
	except:
		print 'Please enter numerical values: '
print 'Max', max(numbers)
print 'Min', min(numbers)

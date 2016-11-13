# Write another program that prompts for a list of numbers as above and at the end
# prints out both the maximum and minimum of the numbers instead of the average.

smallest = largest = None
while True:
	line = str(raw_input('>'))
	try:
		int(line)
		if largest is None or line > largest:
			largest = line
		if smallest is None or line < smallest:
			smallest = line
	except:
		if line == 'done':
			print 'Largest:', largest, 'Smallest', smallest
			break
		print 'Invalid input'

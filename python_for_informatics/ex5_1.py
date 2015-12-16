total = count = 0
while True:
	line = str(raw_input('>'))
	try:
		total = total + int(line)
		count = count + 1
	except:
		if line == 'done':
			Average = float(total) / float(count)
			print 'Count:', count, 'Total:', total, 'Average:', Average
			break
		print 'Invalid input'

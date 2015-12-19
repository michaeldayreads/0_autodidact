def shoutfile(fname):
	fhand = open(fname)
	count = 0
	for line in fhand:
		count = count + 1
		if count > 10:
			fname.close()
			return
		print (line.upper()).strip()
	fname.close()
	return

while True:
	fname = raw_input('Enter a file name: ')
	if fname.lower() == 'exit()' or fname.lower() == 'exit':
		exit()
	try:
		shoutfile(fname)
	except:
		print "Unable to locate file. Please try another name."

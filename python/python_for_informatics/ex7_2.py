# functions

def file_handle(fname):
	try:
		fhand = open(fname)
	except:
		output = "Unable to locate file. Please try another name."
		return output
	output = calc_dspam(fhand)
	return output

def calc_dspam(fhand):
	match_count = 0
	calc_count = 0
	total = 0.0
	for line in fhand:
		header_pos = line.find('X-DSPAM-Confidence: ')
		if header_pos == -1:
			continue
		match_count = match_count + 1
		value_pos = line.find(': ')
		try:
			confidence_value = float(line[value_pos+1:].strip())
			calc_count = calc_count + 1
			total = total + confidence_value
		except:
			log(line)
			continue
	if calc_count > 0:
		average = total / calc_count
	else:
		average = 0
	possible_errors = match_count - calc_count
	if possible_errors > 0:
		error_report(possible_errors)
	return average

def log(line):
	global log_file
	global fname
	log_file = log_file + '\nIn file: ' + fname + ' -- ' + line


def error_report(n):
	# If we are looking for a DSPAM average in an email archive, some emails likely reference DSPAM values...
	# Not part of original exercise.
	global log_file
	choice = raw_input(str(n) + ' lines referred to DSPAM but did not appear to be headers.\n Type "review" to see report.\n>')
	if choice.lower() == 'review':
		print log_file
		print '----- END Error Report -----\n'
		return
	else:
		return

#main

log_file = 'Lines referencing X-DSPAM-Confidence and also appearing to not be headers.\n-----'
while True:
	fname = raw_input('Enter a file name: ')
	if fname == '':
		fname = '2td.txt' #test file that includes "errors"
	if fname.lower() == 'exit()' or fname.lower() == 'exit' or fname.lower() == 'quit':
		exit()
	result = file_handle(fname)
	print 'Average spam confidence:', str(result)

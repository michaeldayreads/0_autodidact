import re

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

f = 'mbox.txt'

while True:
	pattern = raw_input('Enter a regular expression: ')
	check_for_exit(pattern)
	match_count = 0
	fhand = open(f)
	for line in fhand:
		match = re.findall(pattern, line)
		#match_count += len(match)
		if len(match) > 0 : match_count += 1
	fhand.close()
	print f, 'had ', match_count, 'lines that matched', pattern

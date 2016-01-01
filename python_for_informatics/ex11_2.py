import re

def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

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

line_count = 0
author = ''
commits = dict()

for line in fhand:
	author_match = re.findall('^Author: ([A-Za-z][\w+-]*\.?[\w+-]+@[A-Za-z][\w-]*\.?[\w-]+\.[A-Za-z]{2,3})', line)
	if len(author_match) > 0: 
		author = author_match[0]
		line_count = 0
	if line_count == 2 and re.findall('^New Revision:.* [0-9]+', line): 
		commits[author] = commits.get(author, 0) +1
	line_count += 1

leader = list()

for email, count in commits.items():
	leader.append((count, email))

leader.sort(reverse=True)

print '\n\n----------  Commit Leader Board  ----------\n\n'
for row in leader:
	count, email = row
	print 'Commits:', count, '  From:', email

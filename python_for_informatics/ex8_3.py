testfile = ['From test@test.com Sat','...','This is an arbitrary test case, but if the word were on\nits\' own line it would break it.','From John,']
print 'The \'Test\' file:\n-----\n'
for line in testfile:
	print line
print '\n-----\n'
fhand = open('mbox.txt')
for line in fhand:
	if line.find('From ',0) == 0 and line.count('@') == 1:
		words = line.split()
		print line
		print words[2]
fhand.close()

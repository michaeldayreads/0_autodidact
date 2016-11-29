# 8.2 part 1)
# severance's example from the book faiiling on a "test file"
# note removed count = 0 line, as count is not used.
# testfile = ['From test@test.com Sat','...','This is an arbitrary test case, but if the word were on\nits\' own line it would break it.','From John,']
# print 'The \'Test\' file:\n-----\n'
# for line in testfile:
# 	print line
# print '\n-----\n'
# fhand = open('mbox.txt')
# for line in testfile:
# 	words = line.split()
# 	if len(words) == 0 : continue
# 	if words[0] != 'From': continue
# 	print words[2]

# 8.2 part 2) modified to not fail test, revised based on 8-3
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

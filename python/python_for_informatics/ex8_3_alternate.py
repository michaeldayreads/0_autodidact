# Alternate solution with error check
# Aside from line count improvement in line 9 that ex 8-3 led to
# this is how I wrote the solution in the middle of the chapter
days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
counts = [0,0,0,0,0,0,0]
error_check = 0
fhand = open('mbox.txt')
for line in fhand:
	words = line.split()
	if len(words) < 3 or line.find('From ', 0) != 0 or line.count('@') != 1 : continue
	error_check = error_check + 1
	day = words[2]
	try:
		match = days.index(day)
		counts[match] = counts[match] + 1
		continue
	except: continue
print days
print counts
error_check = error_check - sum(counts)
print 'Lines that passeed the guardian logic in excess of total count:', error_check
fhand.close()

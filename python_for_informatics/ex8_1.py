days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
def chop(mylist):
	last = len(mylist) - 1
	del mylist[last]
	del mylist[0]
	return

def middle(mylist):
	last = len(mylist) -1
	return mylist[1:last]

print 'The list to start:',days
result2 = middle(days) # get result2 before modifying days
result = chop(days)
print 'Result of function \'chop\':',result
print 'List after \'chop\' called:', days
print 'New list returned from \'middle\' (called first, printed last):', result2

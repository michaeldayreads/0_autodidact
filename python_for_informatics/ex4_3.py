# just can't bring myself to use the lumberjack song. Performed that live once. Long story.
# ex 4.1 and 4.2 code was not interesting. This one I played with a little...
def repent(food):
	oops = eat_too_much(food)
	print "Dammit. I won't do that again. " + oops + ' That is...' + oops

def eat_too_much(food):
	test = 'I ate too much ' + food + '.'
	return test

repent('pizza')

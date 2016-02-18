import re
import os

def check_for_commands(command):
	"""Simple commands, defined in help()"""
	command = command.lower()
	if command == 'help()':
		os.system('clear')
		print """
		help()  : this list
		exit()  : exit script
		clear() : clear screen & restart input cycle
		"""
		return 'continue'
	if command == 'quit()' or command == 'exit()': exit()
	if command == 'clear()': 
		os.system('clear')
		return 'continue'
	
text = 'Starting text. You may replace this with whatever you like.'
pattern = '^$'
print 'Type "help()" at any prompt for commands.\n'

while True:
	print 'Current text:\n > ', text, ' <\nHit "enter" to use again, or type new text below.'
	data = raw_input('text: ')
	if check_for_commands(data) == 'continue': continue
	text = data if (data != '') else text
	print 'Current pattern:\n >', pattern, ' <\n"enter" to use again, or type new - and use \\ when needed!'
	data = raw_input('pattern: ')
	check_for_commands(data)
	pattern = data if (data != '') else pattern
	try:
		if re.search(pattern, text): match = True
		else: match = False
		print '\npattern\n>', pattern, '<', '\n\ntext \n>', text, '< ?\n\n', match, '\n\n-----'
	except:
		print 'Invalid expression!'

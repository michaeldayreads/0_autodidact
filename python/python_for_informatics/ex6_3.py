def count(phrase, char):
	n = 0
	for letter in phrase:
		if letter == char:
			n = n + 1
	return n

phrase = str(raw_input('Enter your text: '))

while True:
	char = str(raw_input('And a single character to count in the text: '))
	if len(char) > 1 or len(char) == 0:
		continue
	else:
		break

number = count(phrase, char)
print number

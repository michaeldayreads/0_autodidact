message = 'Bad score'
try:
	score = float(raw_input('Enter score: '))
	if 0 < score and score < 0.6:
		message = 'F'
	elif 0.6 <= score and score < 0.7:
		message = 'D'
	elif 0.7 <= score and score < 0.8:
		message = 'C'
	elif 0.8 <= score and score < 0.9:
		message = 'B'
	elif 0.9 <= score and score < 1.0:
		message = 'A'
	print message
except:
	print message

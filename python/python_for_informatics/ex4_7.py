def computegrade(score):
	result = 'Bad Score'
	if 0 < score and score < 0.6:
		result = 'F'
	elif 0.6 <= score and score < 0.7:
		result = 'D'
	elif 0.7 <= score and score < 0.8:
		result = 'C'
	elif 0.8 <= score and score < 0.9:
		result = 'B'
	elif 0.9 <= score and score < 1.0:
		result = 'A'
	return result

try:
	score = float(raw_input('Enter Score: '))
	grade = computegrade(score)
except:
	grade = computegrade(0)
print grade

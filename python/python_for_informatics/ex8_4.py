romeo = ['But soft what light through yonder window breaks','It is the east and Juliet is the sun','Arise fair sun and kill the envious moon','Who is already sick and pale with grief']
allthewords = list()
for line in romeo:
	words = line.split()
	# print words
	for word in words:
		try:
			allthewords.index(word)
			continue
		except:
			allthewords.append(word)
allthewords.sort()
print allthewords

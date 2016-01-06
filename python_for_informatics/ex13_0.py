import json

input = '''
[
	{	"id" : "001",
		"x" : "2",
		"name" : "Chuck"	
	} ,
	{	"id" : "000",
		"x" : "8",
		"name" : "Michael"
	}
]
'''

info = json.loads(input)
print 'User count:', len(info)

print info[0]

at_list = list()

# let attributes of data determine how we unpack it
for attribute in info[0]:
	at_list.append(attribute)

print at_list

for item in info:
	for attr in at_list:
		print attr, item[attr]

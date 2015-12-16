def computepay(hours, rate):
	pay = hours * rate
	if hours > 40:
		pay = pay + ((hours - 40) * (rate * 0.5))
	pay = float(int(pay * 100)) / 100
	print 'Pay is $' + str(pay)

try:
	hours = float(raw_input('Enter hours: '))
	rate = float(raw_input('Enter rate: '))
	computepay(hours, rate)
except :
	print 'Error, please enter numeric input'

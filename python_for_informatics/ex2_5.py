celcius = int(raw_input('Degrees Celcius? '))
fahrenheit = celcius * 9.0 / 5 + 32 # included one float so result is float
print str(celcius) + ' degrees celcius is ' + str(fahrenheit) + ' degrees Fahrenheit.' # inferred str() from introduction of int()

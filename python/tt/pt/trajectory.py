def check_for_exit(cmd):
    if cmd.lower() == 'quit()' or cmd.lower == 'exit()':
        exit()

muscle_rate = 0.44  # Athletes can gain 0.44 lbs a week
fat_loss = 2.0  # two lbs a week is the high end.

while True:
    data = input('Enter weight and bodyfat: ')
    check_for_exit(data)
    current = data.split()
    weight = float(current[0])
    bf = float(current[1])/100
    lean_mass = weight - (weight*bf)
    gain_lean = 180 - lean_mass
    non_lean = weight - lean_mass
    muscle_weeks = gain_lean / muscle_rate
    bf_weeks = (non_lean - 20) / fat_loss
    print(f"Min weeks until lean mass achieved: {muscle_weeks:.2f}")
    print(f"Min weeks until body fat achieved: {bf_weeks:.2f}")


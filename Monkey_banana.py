monkey = input('Is monkey on the floor?(y/n): ')
chair = input('Is chair on the floor?(y/n): ')
position = input('Is chair in the center?(y/n): ')

# Checking if the monkey is on the floor, the chair is on the floor and the chair is in the center.
if monkey.lower() == 'y' and chair.lower() == 'y' and position.lower() == 'y':
    print('Case possible')

# Checking if the monkey is not on the floor, the chair is on the floor and the chair is in the
# center.
elif monkey.lower() == 'n' and chair.lower() == 'y' and position.lower() == 'y':
    print('Case poosible')

# Checking if the monkey is on the floor, the chair is on the floor and the chair is not in the
# center.
elif monkey.lower() == 'y' and chair.lower() == 'y' and position.lower() == 'n':
    while True:
        op = input('Continue?(y/n): ')

        # Checking if the user input is equal to 'n' and if it is, it will print the following
        if op.lower() == 'n':

            # message: 'Chair is in the center'.
            print('Chair is in  the center')
            print('Case possible')
            break
        else:
            print('Drag the chair')
            continue

# Checking if the monkey is not on the floor, the chair is not on the floor and the chair is not in
# the center.
elif monkey.lower() == 'n' and chair.lower() == 'n' and position.lower() == 'n':
    print('Case not possible')
else:
    print('Invalid')

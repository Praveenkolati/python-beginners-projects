# Importing the random module.
import random

# Importing the math module.
import math

lower = int(input('enter the lower boundary: '))
upper = int(input('enter the upper boundary: '))

# Generating a random number between the lower and upper boundaries.
x = random.randint(lower, upper)

count = 0

print('You have only', round(math.log(upper-lower+1, 2)), 'trys!')

while count < (math.log(upper-lower+1, 2) - 1):

    # Adding 1 to the count.
    count += 1

# Asking the user to guess a number between the specified range.
    guess = int(input('Guess a number between the specified range: '))

 # Checking if the guess is equal to the random number. If it is, it will print the number of tries it
 # took. If it is not, it will check if the guess is greater than the random number. If it is, it will
 # print that the guess is too low. If it is not, it will check if the guess is less than the random
 # number. If it is, it will print that the guess is too high.
    if x == guess:
        print('Congrats you sis it in', count, 'trys')

    elif x > guess:
        print('Guess is too low')

    elif x < guess:
        print('Guess is too high')

# Checking if the count is greater than the number of tries. If it is, it will print the number.

if count > (math.log(upper-lower+1, 2)-1):
    print('Better luck next time. The number is', x)
    
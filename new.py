import random
from random import randint
iny = randint(1,100)
def ggc():
    attempt = 1
    inputs = [0]
    prev_diff = None
    while attempt < 20:
        user_input = int(input('Enter The Number To Win The Lottery : '))
        inputs.append(user_input)
        curr_diff = abs(user_input - iny)
        if user_input == iny:
            print('You Have Guessed The Correct Number In', attempt, 'Attempt')
        elif user_input < 1 or user_input > 100:
            print('Out Of Bound')
        elif curr_diff < 10 and attempt <= 1:
            print('Warm')
        elif curr_diff > 10 and attempt <= 1:
            print('Cold')
        elif curr_diff is not None and curr_diff < prev_diff:
            print('Warmer')
        elif curr_diff is not None and curr_diff > prev_diff:
            print('Colder')
        attempt += 1
        prev_diff = curr_diff
    return f"'Sorry' You Have Not Guessed The Correct Number in Given Attempts and The Number Was {iny}"
print(ggc())
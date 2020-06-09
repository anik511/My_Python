import random
num = random.randint(1, 1000)
attempts = 0

while True:
    guessnmbr = int(input('Guess a number between 1-1000: '))
    attempts += 1
    if guessnmbr == num:
        print('Yes Guess Correct number')
        break
    elif guessnmbr > num:
        print('Incorrect!!! Try smaller number')
    else:
        print('Incorrect!!! Try larger number')
print('After', attempts, 'attempts you find correct number')
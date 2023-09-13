from random import randint
otp = randint(1111,9999)
print(otp)
attempt = 1
while attempt <= 3:
    try:
        attempt += 1
        user_input = int(input('Enter Your otp'))
        if user_input == otp:
            print('Successfully Verified')
        else:
            print(" 'oh' wrong otp, please try again")
    except:
        print('you have tried maximum number of attempts')

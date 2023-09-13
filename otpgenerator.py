from random import randint

otp = randint(1111, 9999)
print('your otp is :', otp)
attempt = 1
while attempt <= 3:
    try:
        attempt += 1
        user_input = int(input('Enter Your otp :'))
        if user_input == otp:
            print('Successfully Verified the otp')
            break
        else:
            if attempt < 4:
                print(" 'oh' wrong otp, please try again")
            if attempt == 4:
                print('your card is blocked')
    except:
        print('you have tried maximum number of attempts')
        if attempt < 4:
            print(" 'oh' wrong otp, please try again")
        if attempt == 4:
            print('your card is blocked')
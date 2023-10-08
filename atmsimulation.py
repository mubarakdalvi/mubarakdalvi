import random
import timeit
from datetime import date
from datetime import time
from datetime import datetime


amc = 200.00
account_balance = 1000000
otp = random.randrange(1111,9999)


def bank_acc(account_balance):
    try:
        def chk_bank(bank_LasT_digit):
            if len(str(bank_LasT_digit)) == 6 and bank_LasT_digit == 104032:
                return "'Yes' My Account Is Active "
            if len(str(bank_LasT_digit)) == 6 and bank_LasT_digit != 104032:
                raise Exception('PLease Enter Your Account Number')
            if len(str(bank_LasT_digit)) != 6 and bank_LasT_digit != 104032:
                raise Exception('Please Enter Last Six Digit Of Your Account')
        print(chk_bank(int(input('Enter Bank Account Number : '))))

        def validate_card(card_number):
            if len(str(card_number)) == 12 and str(card_number)[-6:] == '509874':
                print('Card Is Valid, You Can Continue To Your Transaction')
                return True
            else:
                raise Exception('Please Enter Valid Card Number')
        print(validate_card(int(input('Enter Card Number To Check : '))))
        def validate_pin(pin):
            if len(str(pin)) == 4:
                return 'Valid Pin'
            else:
                raise Exception('Invalid Pin Please Enter Correct Pin')
        print(validate_pin(int(input('Enter Pin : '))))
        def validate_otp(user_input):
            if otp == int(user_input):
                print('Valid Otp You Can Now Withdraw The Balance ')
                return True
            else:
                raise Exception('Sorry Wrong Otp Please Enter Valid Otp To Withdraw The Balance ')
        print(f"OTP Is {otp}")
        user_input = input('Enter Otp To Withdraw Balance : ')
        validate_otp(user_input)
        def bank_balance(account_balance):
            user_input = input('Please Select Withdraw or Deposit : ')
            if user_input.lower() == 'deposit':
                deposit = int(input('Enter Amount To Deposit In Account : '))
                if int(deposit) <= account_balance:
                    account_balance += int(deposit)
                    print(f'Deposit Successful, Your New Balance is {account_balance}.Rs and transaction time is {datetime.now()}')
                else:
                    raise Exception('Please Enter Amount Less Than Available Balance')
            elif user_input.lower() == 'withdraw':
                withdraw = int(input('Enter Amount To Withdraw From Account : '))
                if account_balance >= int(withdraw):
                    account_balance -= int(withdraw)
                    notes_500 = int(withdraw) // 500
                    withdraw %= 500
                    notes_200 = int(withdraw) // 200
                    withdraw %= 200
                    notes_100 = int(withdraw) // 100
                    withdraw %= 100
                    notes_50 = int(withdraw) // 50
                    withdraw %= 50
                    print(f'Withdrawal Successful, Your Available Balance is {account_balance}.Rs and transaction time is {datetime.now()}')
                    print(f'Number of 500 Notes is {notes_500} ,Number of 200 Notes is{notes_200}, Number of 100 Notes is{notes_100}, Number of 50 Notes is{notes_50}')
                    return account_balance
                else:
                    raise Exception('Please Enter Amount Less Than Available Balance')
        account_balance = bank_balance(account_balance)
        def amc_charges(amc,account_balance):
            date_of_amc = date.today()
            if date_of_amc.month == 10 and date_of_amc.day == 8:
                if amc <= account_balance:
                    account_balance -= amc
                    print(f'Annual Maintenance Charges Is Deducted From Bank Account On {datetime.now()} If you are Facing Any problem Please Contact To 1800-180-190. Your Available Balance Is {account_balance}')
                elif account_balance < amc:
                    print('PLease Pay AMC Charges On Time To Avoid Late Payment Charges Charges')
                else:
                    raise Exception('PLease Pay Your AMC Otherwise Yorr Account Would BE Freeze By Bank')
            else:
                print('Today Is Not A Day of AMC Deduction.')
        amc_charges(amc,account_balance)
    except Exception as e:
        print(f'Please Enter Valid Details {e}')
    finally:
        print('Thank You For Banking With Us')

start_time = timeit.default_timer()
bank_acc(account_balance)
end_timer = timeit.default_timer()
print(f'Time Taken For The Transaction Is : {end_timer - start_time} Seconds.')
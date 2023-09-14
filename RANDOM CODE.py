from collections import OrderedDict

d1 = OrderedDict()
d2 = OrderedDict()

d1 = {}
d1['A'] = 'a'
d1['B'] = 'b'
d1['C'] = 'c'
d1['D'] = 'd'

d2 = {}
d2['A'] = 'a'
d2['B'] = 'b'
d2['C'] = 'c'
d2['D'] = 'd'

print(d1 == d2)




from random import randint
pin = randint(1111,9999)
print(pin)

transactions = 1
while transactions < 3:
    try:
        transactions += 1
        user_input = int(input('Enter Your Pin To validate with system :'))
        if user_input == pin:
            print('Successful Transaction, Happy Banking')
        else:
            print("'Ah' wrong pin please try again")
        if transactions == 4:
            print('Card is blocked, please try next day')
        if transactions >= 4:
            print('Card is blocked , please try next day')
    except:
        print('There is some error in the system, please try after some time')
        if transactions == 4:
            print('Card is blocked, please try next day')
        if transactions >= 4:
            print('Card is blocked , please try next day')
    finally:
        print('Thank you for banking with us, Happy banking')

    from collections import defaultdict


    def defualt_balance():
        return 0


    d1 = defaultdict(defualt_balance)

    d1['account1']
    d1['account2']
    d1['account3'] = 500
    print(d1)


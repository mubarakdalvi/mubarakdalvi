def tezt():
    while True:
        try:
            a = int(input('Enter First Number :'))
            b = int(input('Enter Second Number : '))
            print(a + b)
            break
        except:
            print('There is some locha')
tezt()
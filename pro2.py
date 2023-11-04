#in fisrt attempt
if __name__ == '__main__':
    n = int(input('Enter 1 : '))
    integer_list = map(int, input('Enter : ').split())
    t = tuple(integer_list)
    print(hash(t))

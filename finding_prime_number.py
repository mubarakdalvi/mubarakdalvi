def find_prime_numbers(n):
    result = []
    for args in range(2,n+1):
        isPrime = True
        for num in range(2, args):
            if args % num == 0:
                isPrime = False
        if isPrime:
            result.append(args)
    return result

find_prime_numbers(20)
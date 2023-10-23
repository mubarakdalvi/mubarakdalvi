shoes_number = int(input('Enter Number Of Shoes You Have Available In Stock : '))
shoes_size = list(map(int,input('Enter Shoes Number : ').split()))
customer_numbers = int(input('Enter Number Of Customers : '))
total_earned = 0

for _ in range(customer_numbers):
    size, price = map(int, input('Enter size and final prise  of shoes : ').split())
    if size in shoes_size:
        total_earned += price
        shoes_size.remove(size)
print(total_earned)
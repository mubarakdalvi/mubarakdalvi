# FINDING CARD NUMBER INDEX IN THE GIVEN EG

#test to find the index
def locate_card(card,query):
    return card.index(query)
test = {
    'input': {
        'card': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

print(locate_card(**test['input']) == test['output'])



#finding the index ising dict

def locate_card(cards,query):
    cards = list(map(int,cards))
    cards.sort(reverse=True)
    if query in cards:
        return cards.index(query)
    elif cards == [0] and query == [0]:
        return cards[0]
    return query

cards = input('Enter Card Number To Add In List : ').split()
query = int(input('Enter Card NUmber To Choose: '))
result = locate_card(cards,query)
print(result)


#finding index of the card using list
def locate_card(card,query):
    if query in card:
        return card.index(query)
    else:
        print('Wrong Guess Please try Again')
card = [13,11,10,7,4,3,1,0]
query = 7
output = 3
result = locate_card(card,query)
print(result)
result = output


# another eg

def locate_card(card,query):
    position = 0
    while True:
        if card[position] == query:
            return position
        position += 1

        if position == len(card):
            return -1

card = input('Enter Number : ').split()
query = input('Enter Query : ')
print(locate_card(card,query))

# another another eg

def locate_card(cards,query):
    try:
        cards = list(map(int,cards))
        if query in cards:
            return cards.index(query)
        else:
            return -1
    except (Exception,ValueError,KeyError):
        print('Please Enter Valid Input')


cards = input('Enter Card Number To Add In List : ').split()
query = int(input('Enter Card Number To Choose: '))
print(locate_card(cards,query))

#another optimized solution

def locate_card(card,query):
    for i in range(len(card)):
        if card[i] == query:
            return i
    return -1

card = input('Enter Number : ').split()
query = input('Enter Query : ')

print(locate_card(card,query))
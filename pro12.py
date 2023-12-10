lst = ['a','b','c','f','l','d','e']

lst_set = set(lst)

# Check if there are duplicates in the list
if len(lst) != len(lst_set):
    # If there are duplicates, print the index of each element in the list
    stt = [i for i in lst if lst.index(i)]
    print(False)
else:
    print(True)
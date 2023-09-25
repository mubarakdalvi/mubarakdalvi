import re
s = 'I live in Dapoli'
a = ['I', 'Dapoli']
for i in a:
    print(re.findall(i, s))

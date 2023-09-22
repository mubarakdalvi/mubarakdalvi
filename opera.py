# collection Module and defaultdict liberary
from collections import defaultdict
d1 = defaultdict(lambda : 100)
print(d1['account1'])
d1['account2'] = 20
print(d1['account2'])
print(d1)

# collection Module and OrderedDict liberary
from collections import OrderedDict
od1 = OrderedDict()
od2 = OrderedDict()

od1['A'] = ['a']
od2['B'] = ['b']

od1['B'] = ['b']
od2['A'] = ['a']

print(od1 == od2)


d1 = {}
d2 = {}

d1['A'] = ['a']
d2['B'] = ['b']

d1['B'] = ['b']
d2['A'] = ['a']

print(d1 == d2)
s1 = OrderedDict()
s1['Mumbai is a LARGE'] = 'City and CAPITAL of MAHARASHTRA'
print(s1)


# collection Module and namedtuple liberary

from collections import namedtuple
Mubarak = namedtuple('Mubarak','Age Mobile_Number Address Blood_Group')
my_info = Mubarak(Age = 23, Mobile_Number = 9146911874, Address = '102, Sajid Aprtment Kalkai Kond Near Markaz Masjid Dapoli', Blood_Group = 'O+')
Mubarak.Crush ='Nida'
print(Mubarak.Crush)
print(my_info)


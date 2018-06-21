#range
mylist = [1,2,3]

for num in range(10):
    print(num)

print(list(range(0,11,2)))

#enumerate

word = 'abcde'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

#zip
#only zips to list that is shortest
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)

print(list(zip(mylist1, mylist2)))

#in 
print('x' in [1,2,3])
#min max
mylist = [10,20,30,40,50]
print(min(mylist))

#random
from random import shuffle
mylist = [1,2,3,4,5,6]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))
#input always a string
mynumber = input('enter a number: ')
int(mynumber)
print('you chose ', mynumber)
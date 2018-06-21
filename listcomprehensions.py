mystring = 'hello'

mylist = [letter for letter in mystring]

print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [x for x in range(0,11) if x%2 == 0]
print(mylist)

celcius = [0,10,23,34]

fahrenheit = [( (9/5)*temp +32) for temp in celcius]
print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

#nested loop
mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist)
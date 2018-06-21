mylist = [1,2,3,4,5,6,7,8,9,10]

# for num in mylist:
#     print(num)

for num in mylist:
    if num % 2 ==0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum += num
print(list_sum)

mystring = "hello world"
for letter in mystring:
    print(letter)

tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2), (3,4), (5,6)]
#tupil unpacking
for (a,b) in mylist:
    print(a)
    print(b)
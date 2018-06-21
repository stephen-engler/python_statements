x=0

while x < 5:
    print(f"the current value of x: {x}")
    x+=1
else: 
    print('x is not less than 5')
#break break out of current closest loop
#continue: goes to the top of the closest enclosing loop
#pass: does nothing at all

mystring = 'stephen'
for letter in mystring:
    if letter == 'e':
        #continue
        break
    print(letter)
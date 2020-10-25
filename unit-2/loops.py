#check if a password is valid based on the following rules
# at least one letter between[a-z] and at least one letter between [A-Z]
# at least one number between [0-9]
# at least one character from [$@#]
# minimum length of 6 characters
#maximum length of 16 characters
'''
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '$@#'

password = 'P@ssword'

has_lower = False #At the beginning, we say that this is False as default (the password doesn't have the lower case)
has_upper = False
has_special = False
valid_length = False

if len(password) > 6 and len(password) < 16:
    valid_length = True

for letter in password:
    if letter in lower:
        has_lower = True
    elif letter in lower:
        has_upper = True
    elif letter in special:
        has_special = True

if has_lower and has_upper and has_special and valid_length:
    print('Good password')
else:
    print('bad password')
    
###Version 2

if len(password) < 6 or len(password) > 16:
    valid_length = False
else:
    for letter in password:
        if letter in lower:
            has_lower = True
        elif letter in lower:
            has_upper = True
        elif letter in special:
            has_special = True

    if has_lower and has_upper and has_special and valid_length: #we can have a single variable if it is a boolean
        print('Good password')
    else:
        print('bad password')


#iterating over a string or a list

#the white loop
    num = 10
    while num >= 0:
        print(num)
        num -=1

#infinite loop
    while True:
        val = input('Enter a value: ')
        print(f'you entered {val}')
        if val == '-1':
            break

#prompt the user to enter a value between 1 and 10

#compare the input with your secret number

#if input is less than secret, print 'too small'

#if input is greater than secret, print 'too big'

#if input is equal, , print 'yaaah you are correct!'

x=6
while True:
    val = int(input('Enter a value between 1-10: '))
    if val < x:
        print('too small')
    elif val > x:
        print('too big')
    elif val == x:
        print('yaaah you are correct!')
        break

#or 

x=6
while True:
    val = int(input('Enter a value between 1-10: '))
    if val < x:
        print('too small')
    elif val > x:
        print('too big')
    else:
        print('yaaah you are correct!')
        break

    #Exercise: #use a while loop to reverse a string
    
my_string = 'welcome to python programming'

    #hint: strings are immutable, so you have to build a new string

reversed_string = ''
pos = len(my_string) -1

while pos >= 0:
    reversed_string += my_string[pos]
    pos -= 1
print(reversed_string)

#For Loop

my_other_string = 'hello world'
new_str =''
for letter in my_other_string:
        new_str = letter + new_str

print(new_str)

'''
#another way 
my_other_string ='hello world'
print(my_other_string[::-1])



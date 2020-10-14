'''

#conditionals
#Comparison operators
#>
#<
#>=
#<=
#==
#!=

#if conditions:
#    action
#else:
#    action

num = 25

if num > 10:
    print('great')
else:
    print('Not great')

    print(num)

val = 8
if (val % 2 == 0):
    print('your number is even')
else:
    print('your number is odd')

# how to read input from keyboard

# all keyboard inout is strings (you cannot do mathematical stuff on that unless first you convert it to integer)
value = input('Enter a value: ')

new_val = int(value) + 50

print(new_val)

#read an integer from keyboard (between 1 and 7)
#print the corresponding day name
#eg 1 should print Sunday
value = input('Enter a number (1-7): ')
if (value == '1'):
    print('Sunday'),
if (value == '2'):
    print('Monday'),
if (value == '3'):
    print('Tuesday'),
if (value == '4'):
    print('Wednesday'),
if (value == '5'):
    print('Thursday'),
if (value == '6'):
    print('Friday'),    
if (value == '7'):
    print('Saturday')    

#or (another solution)

value = int(input('Enter a number (1-7): '))
if (value == 1):
    print('Sunday'),
if (value == 2):
    print('Monday'),
if (value == 3):
    print('Tuesday'),
if (value == 4):
    print('Wednesday'),
if (value == 5):
    print('Thursday'),
if (value == 6):
    print('Friday'),    
if (value == 7):
    print('Saturday')   


#using elif
#if there are mulitiple conditions, use elif
#use else for the last condition in a chain
#of related conditions
city = 'Toronto'
if city == "Toronto":
    print('covid is bad there!')
elif city == 'Montreal':
    print('I\'m scared, covid is still bad')
elif city == 'Calgary':
    print('It\'s not sod bad')
elif city == 'Vancouver':
    print('Under control')
else:
    print('No idea what\'s happening')


#print the corresponding letter for a given score, based on these conditions
#create a variable called score, assign it a value
#80 - 100 - print A 
#60 - 79 - print B
#50 - 69 print C
#less than 50 print F 


value = int(input('Enter a number (0-100): '))
if 80 <= value <= 100:
    print('A')
elif 60 <= value <= 79:
    print('B')
elif 40 <= value <= 59:
    print('c')
elif 0<= value <40:
    print('F')
else:
    print('not valid')

#or (simpler way)

score = int(input('Enter your score: '))
if score >= 80:
    print('A')
elif score >=60:
    print('B')
elif score >=50:
    print('C')
else:
    print('F')


# For loop
for num in range (1, 11):
    print (num, end=' ')

#for the first 50 natural numbers
# 1 - 50
#if the number is a multiple of 3, print 'fizz'
#if the number is a multiple of of 5, print 'buzz'
# if the number is a multiple of 15, print 'fizzbuzz'
#otherwise, just print the number

for num in range(1, 51):
    if  num % 15 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print (num)

#check if a password is valid based on the following rules
# at least one letter between a-z and at least one letter between [A-Z]
# at least one number between [0-9]
# at least one character from [$@#]
# minimum length of 6 characters
#maximum length of 16 characters

if len(pass) < 6:
    print('minimum length must be six characters')
elif len(pass) > 16:
    print('maximum length must be sixteen characters')
elif not pass.isdigit():
    print('you must use at least one number between 1 to 9')
elif not pass.islower():
    print('you must use at least one letter')
elif not pass.isupper():
    print('you must use at least one capital letter')
elif not pass.SpecialSym():
    print('you must use at least one special character')
else:
    print('Congratulations! Your password is valid')
    '''
password = '26535@'
if 6 <= len(password) <= 16:
    print('greater than 6, less than 16')
    for element in password:
        print(element, end=" ")
        if element.isalpha() != True:
            break
        elif element.isnumeric() != True:
            break
        elif element != '$':
            break            
        elif element != '@':
            break
else:
    print('password does not meet criteria')
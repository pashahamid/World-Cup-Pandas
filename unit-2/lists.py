'''
#create a list
my_numbers = [1, 2, 3, -7, 11, 0.5, 10.7]
random_things = ['cat', 12.3, True]
#an empty list

#acces an element in a list
print(my_numbers[0])
print(my_numbers[1:])
print(my_numbers[1:4])
print(my_numbers[-1])
print(my_numbers[::-1])
#replace elements in the list
my_numbers[3] = 68
print(my_numbers)
#replace several elements in a list
my_numbers[1:4] =[0 ,1, 1]
print(my_numbers)
#empty the list
my_numbers[0:] = []
print(my_numbers)

student_names = []
#add the names of your classmates to the student_names list
student_names.append('brad')
print(student_names)
student_names.pop()
student_names.pop(1)
print(my_numbers.index(-7))
print(my_numbers.index(1000))

student_names.append('sarah') #adds to the end
student_names.append('isaac')
print(student_names)
#remove an item from a list
student_names.pop() #removes from end
print(student_names)
student_names.insert(0, 'john') #inserts at the given index
print(student_names)
student_names.pop(1) # removes item from a given index
print(student_names)
#replace an element in a list
student_names[1] = 'isaac'
print(student_names)
#append, pop, insert, pop(index), index
#create a list of the first 10 integers
#create a new list comprising the first five numbers
#insert the number 100 at postion 4 in the original list
#remove the second to last number from original list
#string functions
#find the number of items in a list, use len
canada_cities = ['Toronto', 'Calgary', 'Montreal', 'Vancouver', 'Edmonton']
my_numbers = [1, 2, 3, -7, 11, 0.5, 10.7]
print(len(canada_cities))
print(max(my_numbers))
print(min(my_numbers))
#sorted - returns a sorted copy of the list
sorted_list = sorted(my_numbers)
print(sorted_list)
print(my_numbers)
print(' '.join(canada_cities)) # create a string from items in list, separated by space
#min, max, sorted, join
#create a list of cars - makes - 5 items
# sort the list
# create a single string from the list with each make separated by '&'
ages = [21, 34, 55, 67, 89, 40, 68, 27, 5, 27]
#find the sum of the highest and lowest ages
#join the 3rd to sixth values in the list, separated by '&'



student_name = []
student_name.append('brad')
student_name.append('Jonathan')
student_name.append('Rebecca')
student_name.append('Hamid')
print(student_name)

student_name.pop(1)
print(student_name)

my_numbers = [1, 2, 3, -7, 11, 0.5, 10.7]

my_numbers.insert(-1, 1000)

print(my_numbers)

numbers = [1, 2, 3, -7, 11, 0.5, 10.7]
#use for loop to find total of the numbers

total = 0
for num in numbers:
    total += num
print(total)


#find the sum of all the odd numbers in this list
numbers = [-7, 8, 15, 22, 31, 11, 9, 3, 4, 28]

odd_total = 0
for num in numbers:
    if num % 2 == 1:
        odd_total += num
print(odd_total)


#create a new list that contains only those cities with a 't'
canada_cities = ['Toronto', 'Calgary', 'Montreal', 'Vancouver', 'Edmonton']

t_cities =[]
for city in canada_cities:
    if 't' in city:
        t_cities.append(city)

print(t_cities)

'''
#Group challenge /  Game
import random


player1_total = 0
player2_total = 0
max_score = 20

turn = 0 

while True:
    print(f'player {turn+1} playing.')
    choice = input('Enter R to roll or H to hold: ')
    if choice == 'r':
        val = random.randint(1, 6)
        if turn == 0:
            if val!= 1:
                player1_total += val
                print(f'player {turn+1} rolled {val}...current score = {player1_total}')
            else:
                print(f'player {turn+1} rolled {val}... loses turn.')
                player1_total = 0
                turn = 1
        else:
            if val!= 1:
                player2_total += val
                print(f'player {turn+1} rolled {val}...current score = {player2_total}')
            else:
                print(f'player {turn+1} rolled {val}... loses turn.')
                player2_total = 0
                turn = 0
        if player1_total >= max_score or player2_total >= max_score:
            break
    else:
        if turn == 0:
            turn = 1
        else:
            turn = 0
if player1_total>= max_score:
    print('Player 1 Wins!')
else:
    print('player 2 Wins!')

    
 



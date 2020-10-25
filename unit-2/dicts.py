'''
#dictionaries store pairs of keys and values
car = {'make': 'Toyota', 'model': 'Corolla', 'year': 2017}
#get a value by using the key in square brackers
print(car['make'])

#we can also use get
print(car.get('Make'))
#we can add an item to our dictionary using a new key in square bracket
car['color'] = 'Blue'
print(car)
#keys are unique, adding an existing key will overwrite teh current value
car['color'] = 'Black'
print(car)
#create a dictionary from a list of tuples, each being a key value pair
my_city = dict([('name', 'toronto'), ('pop', 1.9e6), ('location', (43.65, -79.38))])
print(my_city)
names = ['The Hulk', 'Iron Man', 'Thor', 'Captain America', 'Black Panther']
weapons = ['strength', 'armour', 'hammer', 'shield', 'agility']
#use zip to combine lists into key value pairs for dictionary
marvel_characters = dict(zip(names, weapons))
print(marvel_characters)
destinations = ['Cancun', 'Cozumel', 'Montego Bay', 'Negril', 'Bora Bora', 'Bali', 'Boracay']
countries = ['Mexico', 'Mexico', 'Jamaica', 'Jamaica', 'French Polynesia', 'Indonesia', 'Philippines']
#create a dictionary called 'vacation' with destinations as keys, and countries as values
#add a destination in hawaii to your dictionary

verse = '''if you can keep your head when all about you are losing theirs and blaming it on you 
if you can trust yourself when all men doubt you
but make allowance for their doubting too
if you can wait and not be tired by waiting
or being lied about  don't deal in lies
or being hated  don't give way to hating
and yet don't look too good nor talk too wise'''
#find the number of unique words in verse
##unique_words = set(words)
#print(len(unique_words))
'''
#use a dictionary to print the occurence of each character in a string

#insert each letter in the dictionary as the key, the value will be hw often it occurs in the string
my_string = 'there was once an old lady'

letter_count = {}
for char in my_string:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print(letter_count)

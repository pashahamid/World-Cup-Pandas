'''
#Problem 1
#Write a function called letter_count that takes a string and a single character, and returns the number of times that character appears in the string

def letter_count(a_string, letter):
    counts_i = 0
    for i in a_string:
        if i == letter:
            counts_i += 1
    return print((counts_i))

letter_count('abcde', 'a')
letter_count('this is going to be easy', 'i')
letter_count('how about that?', 'z')


#Problem 2
#Write a function called count_words that takes a string and returns the number of words in the string.

def count_words(a_string):
  a_list = []
  for i in a_string:
    a_list = a_string.split()
    return print(len(a_list))

count_words('hey there!!')
count_words('I\'m staying home because of the epidemic')
count_words('how-about-a-hypenated-string?')



#Problem 3
#Write a function called reverse_list that takes a list and returns a new list with the items reversed.

def reverse_list(a_list):
  return print(a_list[::-1])

reverse_list([])
reverse_list([1, 2, 3])
reverse_list(['this', 'is', 'cool!'])


#Problem 4
#Write a function called split_list that takes a list of integers and an integer (called the pivot), and returns a list containing two lists:
#• one with all the numbers less than the pivot
#• the other with all the numbers greater than or equal to the pivot

def split_list(a_list, b):
  c_list = []
  b_list = []
  for i in a_list:
    if a_list[i] < b:
      c_list.append(i) 
    elif a_list[i] >= b:
      b_list.append(i)
  return print(c_list, b_list)

'''

#Problem 5
#Write a function called is_isogram that takes a string and returns true if all the characters are unique (no repeated characters), or returns false otherwise.

def is_isogram(word):
    a_list=[]
    for i in word:
        a_list.append(i)
    if(len(set(a_list)) == len(a_list)):
      return print('True')
    else:
      return print('False')

is_isogram('abc')
is_isogram('hi there') 
is_isogram('Hapy coding!')  


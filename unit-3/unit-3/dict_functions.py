'''
#Problem 1
#Write a function called dict_merge that merges two dictionaries.
#If there are common keys, the merged dictionary should have a list of the values of the common keys

def dict_merge(x, y):
    z ={}
    z.update(x)
    z.update(y)
    return print(z)

dict_merge({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

dict_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

### 
dic1 = {'A': 25, 'B': 41, 'C': 32}
dic2 = {'A': 21, 'B': 12, 'C': 62}
result = {}
for key in (dic1.keys() | dic2.keys()):
    if key in dic1: result.setdefault(key, []).append(dic1[key])
    if key in dic2: result.setdefault(key, []).append(dic2[key])

print(result)

#Problem 2
#Write a function called list_to_dict that accepts a person list (which is a list of lists),
#and returns a dictionary. Each list in the person list has only two items.
#The keys of your result dictionary should be the first item in each list,
#and the value should be the second item.

def list_to_dict(x):

    res = dict()

    for sub in x:
        res[tuple(sub[:2])] = tuple(sub[2:])
    
print(list_to_dict([['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']]))
'''
#Problem 3
#Write a function called reverse_dict to reverse a dictionary. 
#This means, given a dictionary, return a new dictionary that has the keys of as values, 
#and the values as keys
odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar', '123451' , '0.0', 'papa', '-pq-']
item_count=[]

for item in odd_strings:
    if len(str(item)) > 3 and item[0] == item[-1]:
        item_count.append('item')
        

print (len(item_count))

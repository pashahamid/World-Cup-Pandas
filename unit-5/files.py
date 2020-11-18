'''
#open a file for reading
my_file = open('lines.txt')

#read the data from the file
data = my_file.read()

print(data)

my_file.close() #close file after reading or writing


#open a file for writing
my_file = open('lines.txt', 'w') #w overwrites the existing contents of the file

#write to file
my_file.write('Third line')

my_file.close()

#open file for appending
my_file = open('lines.txt', 'a') #a adds to the existing contents of the file

my_file.write('\nFourth line')

my_file.close

#using the with keyword - no need to close file each time
with open('sample.csv', 'w') as data_file:
    data_file.write('name,address,age')
    data_file.write('\nJohn,Toronti,30')



import json

#read a json file

with open('students.json', 'r') as student_file:
    student_data = json.load(student_file)

print(student_data)

#read it in a simpler way:
print(json.dumps(student_data, indent=3))

'''






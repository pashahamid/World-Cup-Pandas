#the division / always results in floating point value

x = 5 / 2 # x will be floating point

y = 5 % 2 #modulus gives remainder after division

z = 2 ** 4 #raises 2 to the power 4

#
current_population = 1900000

area = 21000000

#find 10 percent of current population, store in a variable called bottom_ten
bottom_ten_first_way = current_population * (10/100)
bottom_ten = 0.1 * 1900000
print(bottom_ten_first_way)
print(bottom_ten)

#increase population by 15 percent
current_population *= 1.15 #updates the original value

print(current_population)

#find population per area
population_per_area = current_population / area
print(population_per_area)



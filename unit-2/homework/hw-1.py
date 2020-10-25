num=[]
for x in range(1500, 20000):
    if (x % 7 == 0) and (x %5 == 0):
        num.append(x)
print(num) 
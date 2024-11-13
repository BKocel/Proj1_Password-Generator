import random   
numbers = []

i = 0
nrcount = 2
while i in range(nrcount):
    rand = int(random.uniform(1, 9))
    numbers.append(rand)
    i += 1

print(*numbers)

    
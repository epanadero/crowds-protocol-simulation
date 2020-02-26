import random

n = int(input("Number of items: "))

distribution = []

for i in range(n):
	distribution.append(random.uniform(0, 1))


s = sum(distribution)
for i in range(n):
	distribution[i] /= s

print(distribution)

print('Sum is: {}'.format(sum(distribution)))

import random

numbers = []

for i in range(10):
	numbers.append(random.randint(0,100))

print('Desordenados',numbers)

for i in range(0,10):
	for j in range(i+1,10):
		if numbers[i] > numbers[j]:
			temp = numbers[i]
			numbers[i] = numbers[j]
			numbers[j] = temp

print('Ordenados   ', numbers)
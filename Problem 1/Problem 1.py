## X is for all the multiples of 3, y is for all the multiples of 5, check's job is to remove the multiples of 5, from the multiples of 3, and sum is the sums of x and y
## for Project Euler Problem 1

three = int(0)
five = int(0)
check = int(0)
total = int(0)


while three!= 999:
	three+=3
	check = three % 5
	if check != 0:
		total += three
print(total)

while five!=995:
	five+=5
	total += five

print(total)

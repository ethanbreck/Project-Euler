## X is for all the multiples of 3, y is for all the multiples of 5, check's job is to remove the multiples of 5
## from the multiples of 3, and sum is the sums of x and y 
x = int(0)
y = int(0)
check = int(0)
sum = int(0)
unused = int(0)

while x!= 999:
	x+=3
	check = x % 5
	print(check)
	if check == 0:
		unsued += x
		else sum += x:

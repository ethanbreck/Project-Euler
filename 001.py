'''For project Euler project 1'''

total = 0
for num in range(1000):
	if num % 3 == 0 or num % 5 == 0:
		print(num)
		total = total + num
print total:

three = int(0)
five = int(0)
check = int(0)
total = int(0)


while three!= 999:
	three+=3
	check = three % 5
	if check != 0:
		total += three

while five!=995:
	five+=5
	total += five

print(total)

num1 = int(input("Your initial value: "))
num2 = int(input("Your final value: "))
print()

addition = 0

for add in range(num1, num2 + 1):

	addition = add + addition

	print()
	print("Repeted addition: ", addition)
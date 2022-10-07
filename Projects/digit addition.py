a = int(input("Enter your value: "))

def getSum(a):

	sum = 0

	for digit in str(a):

		sum += int(digit)

	return sum

print(getSum(a))
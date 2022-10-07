
#print()
#print("Max value:")
#print(max(a, b, c, d, e))

#print()
#print("Min value:")
#print(min(a, b, c, d, e))

num = int(input("Enter a number: "))

max_val, min_val = num, num

for x in range(4):

	num1 = int(input("Enter a number: "))

	if max_val < num1:
	
		max_val = num1

	if min_val > num1:

		min_val = num1

print()
print("Values:")
print("Maximum value: ", max_val)
print("Minimum value: ", min_val)
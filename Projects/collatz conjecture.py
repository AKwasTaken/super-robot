n = int(input("Enter a number: "))

lst = []

while n:

	if n % 2 == 0:

		n = n/2

#		print(int(n), end = ', ')

		lst.append(int(n))

		continue

	elif n == 1:

		break
	
	elif n % 2 != 0:

		n = (n*3) + 1

#		print(int(n), end = ', ')

		lst.append(int(n))

		continue

print()

print("\n",lst)
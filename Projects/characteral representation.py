snt = input("Enter a line: ")

upc = 0
lwc = 0
num = 0
spl = 0
alp = 0
spc = 0

for a in snt:

	if a.isalpha():

		alp = alp + 1

		if a.isupper():

			upc = upc + 1

		elif a.islower():

			lwc = lwc + 1

	elif a.isdigit():

		num = num + 1

	elif a.isspace():

		spc = spc + 1

	else:

		spl = spl + 1

print()
print('Uppercase letters = ', upc)
print('Lowercase letters = ', lwc)
print('Special Characters = ', spl)
print('Numbers = ', num)
print('Alphabets = ', alp)
print('Spaces = ', spc)
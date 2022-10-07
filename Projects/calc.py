print("Calc")

a = float(input("Enter your first value: "))
b = float(input("Enter your second value: "))
c = input("Enter your operator: ")

answer = 0

if c == '+':
	answer = a+b

elif c == '-':
	answer = a-b

elif c == '*':
	answer = a*b

elif c == '/':
	answer = a/b

elif c == '%':
	answer = a%b

else:
	print("Invalid input.")


print(a, c, b, '=', answer)
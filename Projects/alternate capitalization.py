snt = input()

x = len(snt)

snt2 = ' '

for a in range(0, x, 2):

	snt2 = snt2 + snt[a]

	if a < (x-1):

		snt2 = snt2 + snt[a + 1].lower()

print()

print(snt2)
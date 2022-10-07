import decimal

def intg(x):
	d = decimal.Decimal(x)
	return d.as_tuple().exponent


a = 2
b = 7
for i in range(1000000):
	
	num = i+1
	x = (num)**(1/a)
	y = (x)**(1/b)

	j = intg(y)
	k = intg(x)
	if j==0 and k==0:
		print(num)
	else:
		continue
import csv
import time

start = time.time()

pc1 = open(r"D:\Code\Python\IP\class_12\data\Phy\phy_chap1.csv", 'r')

pc1r = csv.reader(pc1)

pc1 = []

for x in pc1r:
	pc1.append(x)

print(pc1)

end = time.time()
print(str(start-end))
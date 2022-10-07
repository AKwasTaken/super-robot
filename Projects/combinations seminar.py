myFile = open(r'D:\Code\Python\Worked\Resource\combinations.txt', 'w+')

good = ['HPranav','SriBarath','Rohith','AneethKumaar','OmAkash','MPranav']
avg = ['SriHari','Shrigith','Rishwanth','Vishvanth','Mohnish','Rakesh','GowthamSurya']
lst = []
count = 1

for x in good:
    for y in avg:
        line = str(count) + " " + x + " " + y
        lst.append(line)
        myFile.write(line)
        count += 1
    myFile.write('\n')

print(lst)
myFile.close()

#['HPranav','SriBarath','Rohith','AneethKumaar','OmAkash','MPranav']
#['SriHari','Shrigith','Rishwanth','Vishvanth','Mohnish','Rakesh','GowthamSurya']
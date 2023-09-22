infile=open('demo.txt','r')
line=int(input("enter the first N line"))
for x in range(line):
    r=infile.readline()
    print(x+1,r)
infile.seek(0)
n=input("enter the word to count")
count=0
for y in infile:
    z=y.split()
    count+=z.count(n)
print(count)
dict={'I':1,'V':5,'X':10,'C':100,'L':50,'M':1000}
a=input("entre the roman")
a=a[::-1]
p=a[0]
sum=dict[p]
for i in a[1:]:
    if(dict[p]<=dict[i]):
        sum=sum+dict[i]
    else:
        sum=sum-dict[i]
    p=i
print(sum)
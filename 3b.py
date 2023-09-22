#simalrity in string

str1=input("enter the string1")
str2=input("enter the string2")
lenmax=max(len(str1),len(str2))

count=0
for i in range(lenmax):
    if(str1[i]==str2[i]):
        count+=1
print("match count",count)
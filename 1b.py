#find palindrome and the count each occurence of number

n=input("enter the number")
if(n==n[::-1]):
    print("yes it is palindrome")
else:
    print("no it is not a plindrome")

print("counting of each element")
b={}
for i in range(len(n)):
    b[n[i]]=n.count(n[i])
print(b)

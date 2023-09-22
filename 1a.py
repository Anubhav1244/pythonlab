# average of the best two number
nums=[]
for i in range (0,3):
    print("enter the num",i+1)
    n=int(input())
    nums.append(n)
nums.sort()
print("average of best two number")
print((nums[2]+nums[1])/2)


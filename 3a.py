n=input("enter the input data")
lower,upper,digit,space=0,0,0,0
for i in range(len(n)):
    if(n[i].islower()==True):
        lower+=1
    elif(n[i].isdigit()==True):
        digit+=1
    elif(n[i].isupper()==True):
        upper+=1
    elif(n[i].isspace()==True):
        space+=1
print("lower:",lower)
print("upper:",upper)
print("digit:",digit)
print("space:",space)
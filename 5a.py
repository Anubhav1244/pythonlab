import re
def withoutreg(n):
    if(n[0:3].isdigit() and n[4:7].isdigit() and n[8:12] and n[3]=='-' and n[7]=="-"):
        print("valid number")
    else:
        print("not valid")

def withreg(n):
    pattern =('\d{3}-\d{3}-\d{4}')
    result=re.match(pattern,n)
    if result:
        print("valid")
    else:
        print("not valid")

n="776-682-7656"
withoutreg(n)
withreg(n)

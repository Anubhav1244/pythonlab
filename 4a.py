def inseration(list):
    n=len(list)
    for i in range(1,n):
        temp=list[i]
        i=i-1
        while(i>=0 and temp<list[i]):
            list[i+1]=list[i]
            i=i-1
        list[i+1]=temp
    return list

def merge(llist,rlist):
    lindex,rindex=0,0
    newlist=[]
    while(lindex<len(llist) and rindex<len(rlist)):
        if(llist[lindex]<rlist[rindex]):
            newlist.append(llist[lindex])
            lindex+=1
        else:
            newlist.append(rlist[rindex])
            rindex+=1
    while(lindex<len(llist)):
        newlist.append(llist[lindex])
        lindex+=1
    while(rindex<len(rlist)):
        newlist.append(rlist[rindex])
        rindex+=1
    return newlist

def mergesort(list):
    if(len(list)<=1):
        return list
    mid=len(list)//2
    llist=list[0:mid]
    rlist=list[mid:]
    llist=mergesort(llist)
    rlist=mergesort(rlist)
    return merge(llist,rlist)

a=[5,7,2,1]
b=mergesort(a)
print(b)
    
import sys
class Employee:

    def __init__(self):
        self.name=""
        self.id=""
        self.dept=""
        self.sal=0
    def getDetails(self):
        self.name=input("enter the name of the employee")
        self.id=input("enter the id of the employee")
        self.dept=input("enter the dept of the employee")
        self.sal=int(input("enter the sal of the employee"))
    def displayDetails(self):
        print("name :",self.name)
        print("id :",self.id)
        print("dept :",self.dept)
        print("sal :",self.sal)
    
    def updatesal(self):
        self.sal=int(input("enter the upadted sal of the employee"))
        print("sal is updated sucessfully")
        return self.sal

EMP=[]
emp=Employee()
n= int(input("enter the number of employee"))
for i in range(n):
    emp.getDetails()
    print(".......display details..........")
    emp.displayDetails()
    EMP.append(emp)


n=int(input("press 1 to update the sal or 0 to terminate the process"))
if(n==1):
    name=input("netr the name of the employee")
    for i in range(len(EMP)):
        if(EMP[i].name==name):
            EMP[i].sal=emp.updatesal()
            emp.displayDetails()
            break
else:
    sys.exit(0)

            

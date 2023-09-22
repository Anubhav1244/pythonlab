class palindrome_str:
    
    def __init__(self):
        self.str=""

    def palindrome(self,str):
        self.str=str
        if(self.str==self.str[::-1]):
            print("yes it is plaindrome")
        else:
            print(self.str)
            print("not a palindrome")
class palindrome_int:
    
    def __init__(self):
        self.str=""

    def palindrome(self,val):
            self.str=str(val)
            if(self.str==self.str[::-1]):
                print("yes it is plaindrome")
            else:
                print("not a palindrome")

p=palindrome_int()
p.palindrome(121)
q=palindrome_str()
q.palindrome("nayan")

        
import re 
phone_pat=re.compile(r'\+\d{12}$')
email_pat=re.compile(r'[0-9a-zA-Z_.]+@gmail.com')
f=open('demo.txt','r')
for i in f:
    matches=phone_pat.findall(i)
    for match in matches:
        print(match)
    matches=email_pat.findall(i)
    for match in matches:
        print(match)
f.close()

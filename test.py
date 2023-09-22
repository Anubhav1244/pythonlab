import re
email_pat=re.compile(r'[0-9]')
res=re.match(email_pat,"11.5")
if res:
    print("yes")
else:
    print("no")
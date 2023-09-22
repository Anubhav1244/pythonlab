import json

with open('a.json','rb') as f:
    data=json.load(f)


current_temp=data["weather"]["temp"]
current_humid=data["weather"]["humidity"]
current_desc=data["weather"]["desc"]

print(current_temp)
print(current_humid)
print(current_desc)
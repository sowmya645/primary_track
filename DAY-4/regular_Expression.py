import re
text="python is powerful"
result=re.search("python",text)
if result:
    print("Match found: ",result.group())
    
text="my number is 12345 and 98765"
number=re.findall("\d{5}",text)
print(number)
for match in re.finditer("\d{5}",text):
    print("match found at",match.start(),"to",match.end())
text="my phone number is 1234"
masked=re.sub(R'\d','*',text)
print(masked)
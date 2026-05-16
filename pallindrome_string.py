s="A man, a plan, a canal: Panama"
str=""
for x in s:
    if x.isalpha():
        str=str+x
print(str)
str=str.lower()
print(str)
rev=str[::-1]
if rev==str:
    print("pallindrome")
else:
    print("not pallindrome")
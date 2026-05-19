s="h4c"
t="h4c"
count=0
output=0
if len(s)>len(t):
    output=len(s)-len(t)
elif len(s)<len(t):
    output=len(t)-len(s)
elif len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    output=count
print(output)
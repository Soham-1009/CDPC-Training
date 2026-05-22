import re
x="a"
x='ab+'
x='a*'
x='a?'
x='a{3}'
x='a{2,3}'
matcher=re.finditer(x,"abaababaab")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())
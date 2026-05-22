import re
count = 0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababaab")
for match in matcher:
    count+=1
    print(match.start(),"...",match.end(),"...",match.group())
print("total no of group occurences: ", count)

######################################################################

import re
count = 0
matcher=re.finditer("ab","abaababaab")
for match in matcher:
    count+=1
    print(match.start(),"...",match.end(),"...",match.group())
print("total no of group occurences: ", count)
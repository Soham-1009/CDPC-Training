import re
x='[abc]'
x='[^abc]'
x='[a-z]'
x='[0-9]'
x='[a-zA-Z0-9]'
x='[^a-zA-Z0-9]'
matcher=re.finditer(x,"a8H93@01sdefoe&*DSNSJN")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())

#####################################################################

import re
x='\\s'
x='\\S'
x='\\d'
x='\\D'
x='\\w'
x='\\W'
x='.'
matcher=re.finditer(x,"a8H93 @01sde foe&* DSNSJN")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())
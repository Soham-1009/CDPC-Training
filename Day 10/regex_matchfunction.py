# match() function
# We can use match function to check the given pattern at
# beginning of target string.
# If the match is available then we will get Match object,
# otherwise we will get None.
# import re
# str=input("Enter any string :")
# m=re.match(str,"abc@xyz_pqr*")
# if m != None:
#     print("Yes matching is available at beg")
#     print('start index: ',m.start(),'.end index:',m.end())
# else:
#     print("matching is not available at beg")

#########################################################################

import re
str=input("Enter any string :")
m=re.fullmatch(str,"abc@xyz_pqr*")
if m != None:
    print("Yes matching is available at beg")
    print('start index: ',m.start(),'.end index:',m.end())
else:
    print("matching is not available at beg")
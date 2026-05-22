# 10 digits numbers
# Rules:
# 1: exactly 10 digit number
# 2: start number with 6 or 7 or 8 or 9

# [6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
# or
# [6-9][0-9]{9}
# or
# [6-9]\d{9}|

import re

number=input("Enter mobile number")
match=re.fullmatch("[6-9]\\d{9}",number)
if match!=None:
    print(number," is valid mobile number")
else:
    print(number," is not valid mobile number")
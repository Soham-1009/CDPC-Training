# a function is a self contatined block of code which is designed to perform a perticular task.

######################################################################################

# def add():
#     a=int(input("enter the value of a:"))
#     b=int(input("enter the value of b:"))
#     res=a+b
#     print("Addition is ",res)
# if __name__ == "__main__":
#     add()

######################################################################################

# parameterized function

# def add(a,b):
#     res=a+b
#     print("Addition is ",res)
# if __name__ == "__main__":
#     a=int(input("enter the value of a:"))
#     b=int(input("enter the value of b:"))
#     add(a,b)

######################################################################################

# function with parametres and with return single values 

# def add(a,b):
#     res=a+b
#     return res
    
# if __name__ == "__main__":
#     a=int(input("enter the value of a:"))
#     b=int(input("enter the value of b:"))
#     r=add(a,b)
#     print("Addition is ",r)

######################################################################################

# function with parametres and with return multuple values 

def add(a,b):
    res=a+b
    res1=a-b
    res2=a*b
    return res,res1,res2
                                                                                                                    
if __name__ == "__main__":
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    r,r1,r2=add(a,b)
    print("Addition is ",r)
    print("Subraction is ",r1)
    print("Multipliaction is ",r2)
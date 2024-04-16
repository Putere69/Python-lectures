a = 1
b = 7

def learning():
    a = 1
    b = 7
    print ("a+b=", a+b)
    print ("A=", a, "B=", b)


    a="1"
    b="7"
    print ("a+b=", a+b)


    print (type (a).__name__)

    if (type (a).__name__ == "int" and type (b).__name__ == "int"):
        print("a+b", a+b)
    else :
        print("a+b=", int (a) + int (b) )

# learning()


a = '7'
 
def check_type(a, b):
    if (type (a).__name__ == "int" and type (b).__name__ == "int"): 
        return True
    else :
       return False


if check_type (a, b) == True:
    print (a+b)
else: 
    print ("nu pot aduna ")



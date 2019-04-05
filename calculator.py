def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
def choice():
    op=input("enter 1 for addition,2 for substraction,3 for multiplication,4 for division")
    a1=int(input("enter first number"))
    a2=int(input("enter second number"))
    
    if(op=="1"):
        print("added value is:" ,add(a1,a2))
    if(op=="2"):
        print("substracted value is:" ,sub(a1,a2))
    if(op=="3"):
        print("multiplied value is:" ,mul(a1,a2))
    if(op=="4"):
        print("divided value is:" ,div(a1,a2))
choice()

    
c=input("do you want to continue(y for yes/n for no)")
while c=='y':
    choice()
    c=input("do you want to continue(y for yes/n for no)")

    

def add(n):
    for i in n:
       a=input("") 
    return a

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
def choice():
    op=input("enter 1 for addition,2 for substraction,3 for multiplication,4 for division")
    
    
    if(op=="1"):
        n=input("enter the no. you want to add")
        print("added value is:" ,add(n))
    if(op=="2"):
        a1=int(input("enter first number"))
        a2=int(input("enter second number"))
        print("substracted value is:" ,sub(a1,a2))
    if(op=="3"):
        a1=int(input("enter first number"))
        a2=int(input("enter second number"))
        print("multiplied value is:" ,mul(a1,a2))
    if(op=="4"):
        a1=int(input("enter first number"))
        a2=int(input("enter second number"))
        print("divided value is:" ,div(a1,a2))
choice()

    
c=input("do you want to continue(y for yes/n for no)")
while c=='y':
    choice()
    c=input("do you want to continue(y for yes/n for no)")

    

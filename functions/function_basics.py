#function

#simple function
def my_func():
    print("Hello Ravi prakash")
my_func()

#function parameter
def my_func1(c):
    print("I am from:" ,c)
my_func1("usa")

#add by function
def my_func2(x):
    return 5*x
print(my_func2(4))

#input by user
def my_func3(y):
    return 4*y
a=int(input("enter the number"))
res=my_func3(a)
print("result",res)

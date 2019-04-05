#required arguement
def my_func1(c):
    print("I am from:" ,c)
my_func1("usa")

#keyword arguement
def my_func2(x,y):
    print(y)
    print(x)
my_func2(x="ravi",y="hi")

#default parameter
def my_func3(c="india"):
    print("I am from:" ,c)
my_func3()

#multiple arguement
def my_func4(arg1,*vartuple):
    print("output is:")
    print(arg1)
    for i in vartuple:
        print(i)
my_func4(arg1=10)
my_func4("hello",45,56,34)

#list

#list creation
a=["ravi","prakash","developer"]
b=["frontend","webdeveloper"]
print(type(a))

#access list
print("the list is : " ,a)
print(a[0])
print(a[0:2])

#update
a[2]="python"
print(a)

#insert
a.append("java")
a.append(b)
print(a)

#delete
del a[1]
print(a)

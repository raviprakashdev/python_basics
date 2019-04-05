#list creation
a=["ravi","prakash","developer"]
b=["frontend","webdeveloper"]
print(type(a))

#list count
print(a.count("prakash"))

#extend
a.extend(b)
print(a)

#index
print(a.index("developer"))

#insert
#a.insert("developer","pro")
#print(a)

#pop
print(a.pop(1))

#remove
a.remove("ravi")
print(a)


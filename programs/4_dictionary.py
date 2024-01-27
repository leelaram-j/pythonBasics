# this is like a hashmap of java
# with key value pair

dic = {"a": 2, 3: "string"}
print(dic)


print(dic.get("a"))
print(dic.get(3))

print(dic["a"])
print(dic[3])
dic.pop(3)
print(dic)

dic["firstname"] = "Dick"
dic["lastname"] = "tom"

print(dic)

# to build empty dictionary use
dict1 = {}

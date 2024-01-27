# List always with [] similar to array in java
# starts from zero'th index
# allows multiple values with different datatype
# list is mutable -> values can be changed once assigned


values = [1, 2, 3.4, "test"]
print(values)

print(values[1])
print(values[3])

# to print the last value in list
print(values[-1])

# to print within a range
# last index will  not be printed
print(values[1:3])

values.insert(3, "robot")
print(values)

values.append("end")
print(values)

values[4] = "TEST"

del values[0]
print(values)

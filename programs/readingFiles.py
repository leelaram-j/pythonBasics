file = open("sample.txt")
#print(file.read())
#print(file.read(5))

# to read from file one single line
#print(file.readline())


# print all contents of a file line by line

line = file.readline()

while line != "":
    print(line)
    line = file.readline()

file.close()

# read lines as list , this will be useful for iteration

file1 = open("sample.txt")
print(file1.readlines())
file1.close()


file2 = open("sample.txt")
for line in file2.readlines():
    print(line)
file2.close()
# r-> read mode, w-> write mode

with open("sample.txt", "r") as reader:
    content = reader.readlines()
    #reversed(content) # used to reverse items in the list
    with open("sample.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)


# with open("sample.txt", "r") as reader:
#     content = reader.readlines()
#     print(content)
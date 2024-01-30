it = 4

while it > 1:
    if it != 3:
        print(it)
    it -= 1
print("loop complete")


it = 4

while it > 1:
    if it == 3:
        break
    print(it)
    it -= 1
print("loop complete")


it = 10

while it > 1:
    if it == 3:
        print("inside if condition")
        it -= 1
        continue
    print(it)
    it -= 1
print("loop complete")

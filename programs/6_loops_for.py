# for loop

obj = [1, 2, 3, 5, "str"]

for i in obj:
    print(i)
    print(i*2)

# sum of first 5 natural numbers
total = 0
for i in range(1, 6):
    total += i
print(total)


total = 0
for i in range(1, 6, 2):
    total += i
    print(i)
print(total)

print("\n")

for i in range(10):
    print(i)

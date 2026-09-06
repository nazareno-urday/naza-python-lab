size = int(input("How many elements would you like to introduce?: "))
list = []

for i in range(size):
    choice = int(input("Enter a number: "))
    list.append(choice)

temp = 0
for i in range(size):
    for j in range(size):
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(f"This is the sorted list: {list}")

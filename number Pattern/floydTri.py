counter = 1
n = int(input("Enter yor number: "))
for i in range(n):
    for j in range(i):
        print(counter, end=" ")
        counter += 1
    print()
counter=1
n = int(input("Enter your number: "))
for i in range(n):
    for j in range(n):
        print(counter*counter, end=" ")
        counter += 1
    print()
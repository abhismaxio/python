n = int(input("Enter your number: "))
for i in range(n):
    for j in range(n-i):
        print(i+j ,end=" ")
    print()
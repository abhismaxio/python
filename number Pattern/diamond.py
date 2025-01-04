n = int(input("Enter your name: "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    for j in range(i+1):
        print(j+1, end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
for i in range(n+1):
    for j in range(i):
        print("*", end=" ")
    for j in range(n-i+1):
        print(j+1, end=" ")
    for j in range(n-i,0,-1):
        print(j, end=" ")
    print()
# Number of rows
n = 6

# Generate Pascal's Triangle
for i in range(n):
    # Initialize the first element of each row to 1
    row = [1] * (i + 1)

    # Calculate the values of the current row
    for j in range(1, i):
        row[j] = row[j - 1] + row[j]

    # Print the current row
    print(" ".join(map(str, row)))

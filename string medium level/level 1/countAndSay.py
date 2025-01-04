def count_and_say(n):
    if n == 1:
        return "1"

    prev = count_and_say(n - 1)
    result = ""
    count = 1

    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1

    result += str(count) + prev[-1]
    return result

# Example
print(count_and_say(4))  # Output: "1211"


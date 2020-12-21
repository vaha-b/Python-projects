numbers = [8, 11, 15, 15, 15, 12]
num = max(numbers)

for i in range(0, len(numbers)):
    if numbers[i] == num:
        index = i

print(index)

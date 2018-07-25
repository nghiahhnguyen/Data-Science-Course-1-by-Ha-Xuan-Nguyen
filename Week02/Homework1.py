numbers = list(map(int, input().split(',')))
odd = []
even = []
for num in numbers:
    if num % 2:
        odd.append(num)
    else:
        even.append(num)
for num in odd:
    print(num, end=' ')
print()
for num in even:
    print(num, end=' ')

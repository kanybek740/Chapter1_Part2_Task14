numbers = [1,2,3,4,5,6,7,8,9,10]
new_numbers = []
for n in numbers:
    if n % 2 == 0:
        new_numbers.append(n)
    else:
        continue
    print(new_numbers, end=' ')
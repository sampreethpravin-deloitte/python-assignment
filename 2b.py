numbers = [12, 75, 150, 180, 145, 525, 50]
list2 = []
for i in numbers:
    if i>=500:
        break
    if i%5 ==0 and i<=150:
            list2.append(i)
print(list2)
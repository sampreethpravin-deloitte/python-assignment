values = [1, 5, 7, 3, 4, 9, 10]
#values.sort()
length = len(values)
i = 1
min = 1
while i < length:
    if values[i] % 2 == 0:
        min = values[i]
        break
    i += 1
if min > 1:
    while i < length:
        if values[i] % 2 == 0:
             if min > values[i]:
                min = values[i]
        i += 1
    print(" the smallest even number in list is :", min)
else:
    print("not even ")

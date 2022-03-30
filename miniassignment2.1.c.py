#Using filter() function filter the list so that only negative numbers are left.


list1=[12, -1, 9, 8, -0.5, -0.2, -100]

list2= list(filter(lambda x: x<0, list1))

print(list2)
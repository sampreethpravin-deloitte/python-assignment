#Write a Python program to triple all numbers of a given list of integers. Use Python map

numbers = (1, 2, 3, 4, 5, 6, 7)
print("Original list: ", numbers)
result = map(lambda x: x + x + x, numbers)
print("\ntriple all numbers of a given list:")
print(list(result))
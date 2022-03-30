def longest_word(miniassignment3b):
    with open(miniassignment3b, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('miniassignment3b.txt'))


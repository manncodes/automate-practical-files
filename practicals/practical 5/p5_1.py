a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# one liner to find common elements in a list
print([x for x in list(set(a)) if x in list(set(b))])

# lambda to find common elements in a list
print(list(filter(lambda x: x in list(set(b)), list(set(a)))))

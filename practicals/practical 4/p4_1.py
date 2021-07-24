# can be any list
a = [i ** 2 for i in range(1, 11)]

# one-liner
b = [i for i in a if i % 2 == 0]

# lambda function to get all even numbers in list
c = list(filter(lambda x: x % 2 == 0, a))

print(b)
print(c)

# function that takes a list and prints number greater than 5
def print_greater_than_5(l):
    for i in l:
        if i > 5:
            print(i, end=" ")


if __name__ == "__main__":
    print_greater_than_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

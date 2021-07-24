# function to make list of first and last elements of a list.
def first_last(list):
    return [list[0], list[-1]]


if __name__ == "__main__":
    print(first_last([1, 2, 3, 4, 5]))

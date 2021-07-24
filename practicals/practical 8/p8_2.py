# function that takes ordered list and a number and returns if number is in list or not.
def contains(ordered_list, number):
    # check if number is in list
    return number in ordered_list


if __name__ == "__main__":
    print(contains([1, 2, 3, 4, 5], 6))
    print(contains([1, 2, 3, 4, 5], 3))

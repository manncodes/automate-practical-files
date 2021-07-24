# function to print common elements in two lists without duplicates


def print_common(list1, list2):
    common = []
    for i in list1:
        for j in list2:
            if (i == j) and (i not in common or j not in common):
                common.append(i)

    print(common)


if __name__ == "__main__":
    print_common(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    )

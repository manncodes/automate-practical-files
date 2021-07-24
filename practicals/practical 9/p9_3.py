# function for bubble sort
def bubbleSort(lst):
    for _ in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# function for insertion sort
def insertionSort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst


if __name__ == "__main__":
    lst = [5, 4, 3, 2, 1]
    print("Bubble sort: ", bubbleSort(lst))
    print("Insertion sort: ", insertionSort(lst))

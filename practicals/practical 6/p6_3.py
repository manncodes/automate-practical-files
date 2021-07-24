# function that takes a string and returns string with reversed words
def reverse_words(string):
    # split string into list of words
    words = string.split()
    # reverse list of words
    words.reverse()
    # join reversed list of words into string
    return " ".join(words)


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(reverse_words(s))

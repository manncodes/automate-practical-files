# function that prints if a number is even or odd
def check_number(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


if __name__ == "__main__":
    check_number(int(input("Enter a number: ")))

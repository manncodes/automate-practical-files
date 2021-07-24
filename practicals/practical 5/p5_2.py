# write short function to find the number is prime or not
def prime_or_not(number):
    if number == 1:
        return "Not prime"
    elif number == 2:
        return "Prime"
    else:
        for i in range(2, number):
            if number % i == 0:
                return "Not prime"
        return "Prime"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(prime_or_not(number))

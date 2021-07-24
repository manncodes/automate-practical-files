# function to print list of divisors of a number
def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


if __name__ == "__main__":
    print(divisors(26))

# generate given number of fibonacci numbers
def generate_fibonacci(num):
    fib_list = [0, 1]
    for _ in range(num - 2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


# generate given numbers of fibonacci numbers using recursive function
def generate_fibonacci_recursive(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        fib_list = generate_fibonacci_recursive(num - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


if __name__ == "__main__":
    print(generate_fibonacci(10))
    print(generate_fibonacci_recursive(10))

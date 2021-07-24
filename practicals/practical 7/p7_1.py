# function that generates a strong password with alpha-numeric characters and a special character
import random
import string


def generate_password(length):

    return "".join(
        random.choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(length)
    )


if __name__ == "__main__":
    print(generate_password(8))
    print(generate_password(10))

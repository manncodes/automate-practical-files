from datetime import datetime


def tell():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))

    # get current year from datetime
    current_year = datetime.now().year
    year_100 = current_year + (100 - age)

    print(f"{name} will be 100 years old in year {year_100} A.D !")


if __name__ == "__main__":
    tell()

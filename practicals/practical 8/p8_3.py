import random

common_names = [
    "John",
    "James",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Charles",
    "Joseph",
    "Thomas",
    "Christopher",
    "Daniel",
    "Paul",
    "Mark",
    "George",
    "Kenneth",
    "Steven",
    "Edward",
    "Brian",
    "Ronald",
    "Anthony",
    "Kevin",
    "Jason",
    "Matthew",
    "Gary",
    "Timothy",
    "Jose",
    "Larry",
    "Jeffrey",
    "Frank",
    "Scott",
    "Eric",
    "Stephen",
    "Andrew",
    "Raymond",
    "Gregory",
    "Joshua",
    "Jerry",
    "Dennis",
    "Walter",
]

# function to write a text file with many names
def write_text_file(filename, names):
    """
    (str, list) -> NoneType
    Write the content of the list to the file
    """
    with open(filename, "w") as f:
        random_length = random.randint(len(names), 3 * len(names))
        for _ in range(random_length):
            f.write(random.choice(names) + "\n")


# function to count the number of each names in the file
def count_names(filename):
    """
    (str) -> dict
    Return a dictionary with the number of each names in the file
    """
    with open(filename, "r") as f:
        names = f.read().splitlines()
    return dict(
        sorted(
            {name: names.count(name) for name in names}.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    )


if __name__ == "__main__":
    write_text_file("p8_3.txt", common_names)
    print(count_names("p8_3.txt"))

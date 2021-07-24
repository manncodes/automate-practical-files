# example of assert
def test_assert(x):
    assert x == 1, "x is not equal to 1"
    print("Assertion test succeeded")


# example of exeption handling
def test_exeption_handling():
    try:
        test_assert(1)
    except AssertionError as e:
        print(e)
        print("Assertion test failed")


if __name__ == "__main__":
    test_exeption_handling()

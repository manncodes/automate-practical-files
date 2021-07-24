# find order in which base classes are searched when executing a method
def find_order(obj):
    return obj.__class__.__mro__


class Parent(object):
    def __init__(self):
        print("Parent init")

    def parent_method(self):
        print("Parent method")

    def do_something(self):
        print("Parent do something")


class Child(Parent):
    def __init__(self):
        print("Child init")

    def child_method(self):
        print("Child method")

    def do_something(self):
        print("Child do something")


if __name__ == "__main__":
    child = Child()
    print(find_order(child))

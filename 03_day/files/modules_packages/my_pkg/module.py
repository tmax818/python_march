## module.py

def best_function():
    print("hi mom")

def my_other_func():
    print("hello from the module")

def the_other_useless_func():
    pass
print(__name__)


def test():
    print("it ran in the module")

# print(__name__)
if __name__ == "__main__":
    test()
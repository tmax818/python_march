# def_params_named_args.py
# demo


def divide(numerator, denominator):
    print(numerator//denominator)
    return numerator//denominator

divide(10,2)
divide(denominator = 2, numerator = 10)

def greet(name, salutation = 'Dr.'):
    print(f" Hello {salutation} {name}")

greet("Tyler", "Mr.")
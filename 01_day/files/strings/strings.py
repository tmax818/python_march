## strings.py
## demo


## TODO string literals

my_string = "the average airspeed velocity of an unladen swallow."


## TODO concatenating strings and variables with the `print` function

name = 'Tyler'
print("My name is", name)

print("My name is " + name)

## TODO type casting or explicit type conversion

print("Hello", 42)
# print("hello" + 42) # TypeError
print("Hello" + str(42))

## TODO string interpolation (three types)

## TODO f-string

first_name = "Ed"
last_name = "Im"
age = 31

print(f"My name is {first_name} {last_name} and I am {age} years old.")

## TODO string.format()

print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))

## TODO %-formatting

print("My name is %s %s and I am %d years old." % (first_name, last_name, age))


## TODO built-in string methods


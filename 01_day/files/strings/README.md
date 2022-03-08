## TODO string literals
```py
my_string = "the average airspeed velocity of an unladen swallow."
```

## TODO concatenating strings and variables with the `print` function
```py
name = 'Tyler'
print("My name is", name)

print("My name is " + name)
```

## TODO type casting or explicit type conversion
```py
print("Hello", 42)
# print("hello" + 42) # TypeError
print("Hello" + str(42))
```

## TODO string interpolation (three types)

## TODO f-string

```py
first_name = "Ed"
last_name = "Im"
age = 31

print(f"My name is {first_name} {last_name} and I am {age} years old.")
```
## TODO string.format()
```py
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
```

## TODO %-formatting
```py
print("My name is %s %s and I am %d years old." % (first_name, last_name, age))
```

## TODO built-in string methods

- [`upper()`]
- [`lower()`]
- [`count()`]
- [`split()`]
- [`find()`]
- [`join()`]

***

[`upper()`]: https://www.w3schools.com/python/ref_string_upper.asp
[`lower()`]: https://www.w3schools.com/python/ref_string_lower.asp
[`count()`]: https://www.w3schools.com/python/ref_string_count.asp
[`split()`]: https://www.w3schools.com/python/ref_string_split.asp
[`find()`]: https://www.w3schools.com/python/ref_string_find.asp
[`join()`]: https://www.w3schools.com/python/ref_string_join.asp
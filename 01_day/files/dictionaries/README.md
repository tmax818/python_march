# Dictionaries

- aka associative array, a container(i.e. data structure) with the following characteristics:
  - unordered collection of objects
  - values are accessed with the key
  - dictionary keys must be immutable
  - a dictionary is mutable
  - cannot use sequence operations
  - 

See [dictionaries.py](dictionaries.py)

## Creating a dictionary

- compare to making a list
```py
person_list = ['Tyler', 39, ['coding', 'sleeping']]
```
- dictionaries give us ways to associate data 
```py
person_dict = {'name': 'Tyler', 'age': 39, 'hobbies': ['coding', 'sleeping']}
```
## accessing values
```py
print(person['name'])
# => 'Tyler'
```

## removing values
- two ways:
```py
removed_value = person.pop('age')
```
```py
removed_value = person.pop('age')
print(person)
```

## nested dictionaries
```py
del person['hobbies']
print(person)
```

## built-in functions/methods

- [.clear()]
- [.copy()]
- [.fromkeys()]
- [.get()]
- [.items()]
- [.keys()]
- [.values()]



***

[.clear()]: https://www.w3schools.com/python/ref_dictionary_clear.asp
[.copy()]: https://www.w3schools.com/python/ref_dictionary_copy.asp
[.fromkeys()]: https://www.w3schools.com/python/ref_dictionary_fromkeys.asp
[.get()]: https://www.w3schools.com/python/ref_dictionary_get.asp
[.items()]: https://www.w3schools.com/python/ref_dictionary_items.asp
[.keys()]: https://www.w3schools.com/python/ref_dictionary_keys.asp
[.values()]: https://www.w3schools.com/python/ref_dictionary_values.asp


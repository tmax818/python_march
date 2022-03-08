# Tuples

- an **immutable** container(i.e. data structure) for a fixed sequence of data objects.
- defined by () and a comma (,)

```py
my_tuple = (1)
print(type(my_tuple))
```

## Tuple immutability

>Like strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be changed. But we can add and slice tuples. See example below:

```py
dog = ("Canis Familiaris", "dog", "carnivore", 12)
```
- what's up with this?

```py
dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
```
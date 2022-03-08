# Python Loops

## `for` loops with range

see [loops.js](loops.js) and [loops.py](loops.py)

### `range()` with one arg

- compare with JavaScript
```javascript
for(var i = 0; i < 10; i++) {
    console.log(i)
}
```
- same code in Python:
```py
for i in range(10):
    print(i)
```
### range with 2 args:
```py
start = 0 # inclusive
stop = 10 # exclusive
step = 2
for i in range(start, stop):
    print(i)
```
### range with 3 args:
```py
start = 0 # inclusive
stop = 10 # exclusive
step = 2
for i in range(start, stop, step):
    print(i)
```

### Compare to JS

```javascript

var start = 0
var stop = 10
var step = 2

for(var i = start; i < stop; i += step) {
    if (!(i % 2)) {
        console.log(i)
    }
}
```
## `for` loops through strings

my_string = "the average airspeed velocity of an unladen swallow."

for char in my_string:
    print(char)

## `for` loops through lists
```py
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
```
## `for` loops through tuples
```py
dog = ("Canis Familiaris", "dog", "carnivore", 12)

for data in dog:
    print(data)
```
## `for` loops through dictionaries
```py
person = {'name': 'Ed', 'age': 31}

for k in person:
    print(k)

for k in person:
    print(person[k])

for key, value in person.items():
    print(f"The peson's {key} is {value}.")
```

## TODO Loop through lists of dictionaries
```py
data = [
    {'name': 'Ed', 'age': 31},
    {'name': 'John', 'age': 29},
    {'name': 'Tyler', 'age': 39}
]

for person in data:
    print(f"{person['name']} is {person['age']} years old.")
```
# While Loops
```py
count = 0
while count < 5:
    print(count)
    count += 1
```

## loop control

- `break` - exit the loop usually when a condition is met.
- `continue` - returns control to the beginning of the loop.



# Functions

>A function is a named block of code that we can execute to perform a specific task.

see [functions.py](functions.py)
and [functions.js](functions.js)

## syntax

- use the `def` keyword and end the function signature with a colon:

## parameters and arguments

- define the function with optional parameters
- `parameter` is the variable that will hold or reference the argument(s) passed in when the function is invoked/called.

```py
#function declaration:
def function_name(parameter):
    print(parameter)

#function invocation: invoke or call
function_name('argument')
```

## returning values
```py
def seven(lucky_number):
    print(lucky_number)
    return 6 + 1

return_value = seven(42)
# => print to terminal the argument: 42
# => returns 7

print(return_value)
# print function prints the return value to the terminal
```

>**a function is what it returns**

## compare to JavaScript

```javascript
// functions.js

function functionName(parameter) {
    console.log("inside function:", parameter)
    return parameter
}

console.log("value of the function: ", functionName('argument'))
```
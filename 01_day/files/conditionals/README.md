# Conditional Statements

>Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.

see [conditionals.py](conditionals.py)

- keywords: `if`, `elif`, `else`

- compare to js
```javascript
var x = 10
if(x > 10) {
    console.log("greater")
} else if (x < 10) {
    console.log("less")
} else {
    console.log("equal")
}
```
- same code in Python:
```py
x = 10
if x > 10:
    print("greater")
elif x < 10:
    print("less")
else:
    print("equal")
```

## comparison and logical operators

|operator|Python|JavaScript|Description
|:---:|:---:|:---:|:---:|
|equality|==|===|check for equality|
|inequality|!=|!==|check for inequality|
|and|`and`|`&&`|check if both expressions are true
|or|`or`|`\|\|`|check if either expression is true
|not|`not`|`!`|check if either expression is true

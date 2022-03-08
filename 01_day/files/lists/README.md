# Lists

see [lists.py](lists.py)

# Lists

- aka array, a **mutable** container(i.e. data structure) for holding a group of values

## Accessing Values

```py
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens
```

## Manipulating Lists

see [lists.py](lists.py)

- append a new item:
```py
x = [1,2,3,4,5]
x.append(99)
print(x)
#the output would be [1,2,3,4,5,99]
```

### Python list slicing

```py
start = 0 # inclusive
stop = len(x)# exclusive
step = 1

print(x[:]) # makes a copy
print(x[start:stop:step]) # same as above
```

### List (built-in) functions

```py
x = [1,2,3,4,5]
dir(x)
```




- [append]
- [clear]
- [copy]
- [count]
- [extend] 
- [index]
- [insert] 
- [pop]
- [remove] 
- [reverse]
- [sort]

***

[append]: https://www.w3schools.com/python/ref_list_append.asp
[clear]: https://www.w3schools.com/python/ref_list_clear.asp
[copy]: https://www.w3schools.com/python/ref_list_copy.asp
[count]: https://www.w3schools.com/python/ref_list_count.asp
[extend]: https://www.w3schools.com/python/ref_list_extend.asp
[index]: https://www.w3schools.com/python/ref_list_index.asp
[insert]: https://www.w3schools.com/python/ref_list_insert.asp
[pop]: https://www.w3schools.com/python/ref_list_pop.asp
[remove]: https://www.w3schools.com/python/ref_list_remove.asp
[reverse]: https://www.w3schools.com/python/ref_list_reverse.asp
[sort]: https://www.w3schools.com/python/ref_list_sort.asp




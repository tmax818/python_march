from pprint import pprint
## lists.py
## demo

## TODO accessing values

my_list = [1,2,3,4,5]

print(my_list[4])

## TODO manipulating lists

my_list.append(6)
print(my_list)

# pprint(dir(my_list))



## TODO Python list slicing
#my_list = [1,2,3,4,5]
start = 2 # inclusive
stop = 4 # exclusive
step = 1

print(my_list[start:stop:step])
print(my_list[0:5:2])
print(my_list[::-1])


## TODO list functions
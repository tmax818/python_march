## dictionaries.py
## demo

# TODO creating dictionaries

## TODO How would you make a person list?

person = ["Tyler", "Maxwell", 39, True]
# print(person[0])

## TODO dictionaries give us ways to associate data 

person_dict = {'first_name': "Tyler", 'last_name': "Maxwell", 'age': 39, 'admin': True}
print(person_dict['first_name'])
person_dict['hobbies'] = ['sleeping']
person_dict['children'] = []
person_dict['hobbies'].append('coding')
print(person_dict)
person_dict['hobbies'].pop()
print(person_dict)


## TODO add to the hobbies list: 'gaming'

## TODO add to hobbies list in the person_list:


## TODO remove values with pop('key')

person_dict.pop('age')
print(person_dict)

## TODO remove values with del

del person_dict['admin']
print(person_dict)

# TODO nested dictionaries

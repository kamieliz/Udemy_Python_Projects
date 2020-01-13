# Dictionaries - keys have to be immutable data types
# sets
# tuples
my_dictionary = {'name':'mashrur', 'course':'python','fav_food':'ice cream'}
phone_dict = {'mashrur':'555-55-5555',
            'zoolander':'999-99-0000',
            'jon_snow':'fail-o-so-bad'}
print(my_dictionary)
print(my_dictionary['name'])
print(my_dictionary.get('name'))
print(my_dictionary.get('job'))
print(my_dictionary.items())
for k,v in my_dictionary.items():
    print(k,v)

my_random_tuple = {'first',1,7,6,4,5,8,'hi there',2,3,1,5,2,1,9,10}
my_tuple = ('first_value','second_value','third_value')
print(dir(my_random_tuple))
print(len(my_random_tuple))
print(my_random_tuple.index('hi there'))
print('first' in my_random_tuple)
for item in my_random_tuple:
    print(item)

my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python',6}
programming_set = {'java','ruby','javascript','python','c'}
print(my_set) #no duplicates, no indexing
print('java' in my_set)
print(my_set.union(programming_set)) # all the elements of both sets, including common ones but duplicates wont print
print(my_set.intersection(programming_set)) # gives the elements common to both sets
print(my_set.difference(programming_set)) #all the ones that exist in second set but not in first set

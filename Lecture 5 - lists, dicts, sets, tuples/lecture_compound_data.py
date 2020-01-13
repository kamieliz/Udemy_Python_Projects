# lists - [1,2,False,4,"mashrur",None, node_1, 5.0]
# dictionaries - {'name':'mashrur','course':'python'}
# sets - {1,2,False,4,"mashrur",None,Node_1,5.0} no key value pairs like dict, sets dont allow duplicates
# Tuples - (1,2,False,4,"mashrur",None, 5.0) immutable can't change teh value

node_1 = "custom object"
my_data_type = [1,2, False, 4, "mashrur", None, node_1, 5.0, 1]
print(my_data_type)
print(my_data_type[4])
print(type(my_data_type))
my_data_type = {1:'hello',2:'mashrur',3:None, 4:node_1, 5:5.0}
print(my_data_type)
print(my_data_type[2])
print(type(my_data_type))
my_data_type = {1,2, False, 4, "mashrur", None, node_1, 5.0, 1}
print(my_data_type) # sets get rid of duplicates when you print, no order
print(type(my_data_type))
my_data_type = (1,2, False, 4, "mashrur", None, node_1, 5.0, 1)
print(my_data_type) #maintains order, items can be indexed but not changed
#my_data_type[5] = "Python" will error out
print(type(my_data_type))

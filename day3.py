# TERNARY OPERATOR
age = 17
status = "above 18" if age >= 18 else "below 18"
print(status)

# IDENTITY OPERATORS -> is, is not
x = 'a'
y = 'a'
print(x is y)
print(x is not y)

#bitwise operators -> &, |, ^, ~, <<, >>
p = 5  # 0101
q= 3  # 0011
print(p & q)  # 0001 -> 1
print(p | q)  # 0111 -> 7

#data structures -> list, tuple, set, dictionary
#list mutable data structure
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)
print(my_list)
my_list.remove(3)
print(my_list)
print(my_list[2])  # Accessing element at index 2
my_list.extend([7, 8, 9])
print(my_list)
my_list.pop()  # Removes last element
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print(my_list.count(4))
print(len(my_list))
my_list.insert(2, 10)  # Inserting 10 at index 2
print(my_list)

# tuple immutable data structure
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])  # Accessing element at index 1
print(my_tuple.count(3))
print(len(my_tuple)) 
#my_tuple[2] = 10  # This will raise an error since tuples are immutable
#print(my_tuple)

print(my_tuple + (6, 7, 8))  # Concatenation

list_from_tuple = list(my_tuple)  # Converting tuple to list
print(list_from_tuple)
list_from_tuple.extend([6, 7, 8])
my_tuple = tuple(list_from_tuple)  # Converting back to tuple
print(my_tuple)
print(type(my_tuple)) 

# set unordered collection of unique items
my_set = {1,2,3,4,5,5,4,3,2,}
print(my_set)  # Duplicates will be removed

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

print(4 in my_set)  # Membership test

print(len(my_set))

#my_set.remove(10)  # This will raise an error if 10 is not in the set
my_set.discard(10)  # This will not raise an error

print(my_set.pop())  # Removes and returns an arbitrary element

set2 = {3,4,5,6,7,8}
print(my_set.union(set2))  # Union
print(my_set.intersection(set2))  # Intersection
print(my_set.difference(set2))  # Difference


#dictionary key-value pairs
my_dict = {'name': 'Sangam',
           'age': 25,
           'city': 'New York'
           }

print(my_dict)
print(my_dict['name']) 
my_dict['age'] = 26  # Updating value
print(my_dict)

print(my_dict.get('city'))  # Accessing value using get method

print(my_dict.keys())  # Getting all keys
print(my_dict.values())  # Getting all values
print(my_dict.items()) #GETTING BOTH 

print(my_dict.pop('age'))  # Removing key-value pair
print(my_dict)


for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for keys, values in my_dict.items():
    print(f"{keys} : {values}")
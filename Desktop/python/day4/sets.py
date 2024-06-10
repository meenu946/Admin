
# # creating and accesing elements in a set
# In[ ]:

fruits = {"apple", "banana", "cherry", "date"}

print("apple" in fruits)    
print("orange" in fruits)   

for fruit in fruits:
    print(fruit)


# # adding and removing elements in a set

# In[3]:

numbers = {1, 2, 3, 4, 5}

numbers.add(6)
numbers.update([7, 8, 9])

numbers.remove(3)
numbers.discard(10)  

print(numbers)  

# # set operations: union, inetersection difference

# In[4]:

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_set = set_a.union(set_b)
print("Union:", union_set)  

intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)  

difference_set = set_a.difference(set_b)
print("Difference:", difference_set)  


# # set comprehensions
# In[5]:

squares = {x**2 for x in range(1, 6)}
print(squares) 

evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens) 

# # removing duplicates from a list using a set

# In[6]:

numbers_list = [1, 2, 2, 3, 4, 4, 5]

numbers_set = set(numbers_list)
print(numbers_set) 

unique_numbers_list = list(numbers_set)
print(unique_numbers_list)  


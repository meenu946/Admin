
# # Tuples with Different Data Types using Tuple Constructor

# In[ ]:

mixed_tuple = tuple([1, "Hello", 3.14, (1, 2, 3), {'name': 'John', 'age': 30}])

print("Mixed Tuple:", mixed_tuple)

print("\nAccessing Elements:")
print("Element 1:", mixed_tuple[0])   
print("Element 2:", mixed_tuple[1]) 
print("Element 3:", mixed_tuple[2])
print("Element 4:", mixed_tuple[3])    
print("Element 5:", mixed_tuple[4])    

print("\nIterating through Tuple:")
for item in mixed_tuple:
    print(item)

print("\nTuple Unpacking:")
num, greeting, pi, coordinates, person = mixed_tuple
print("Number:", num)
print("Greeting:", greeting)
print("Pi:", pi)
print("Coordinates:", coordinates)
print("Person:", person)

# # Characteristics of Tuples in Python

# In[3]:

employee_records = (
    ("John Doe", 35, "Male", "Senior Developer"),
    ("Jane Smith", 28, "Female", "Project Manager"),
    ("Michael Johnson", 42, "Male", "Data Scientist"),
    ("Emily Davis", 30, "Female", "UX Designer")
)

print("Employee Records:")
for record in employee_records:
    print("Name:", record[0])
    print("Age:", record[1])
    print("Gender:", record[2])
    print("Position:", record[3])
    print()  

def print_employee(name, age, gender, position):
    print(f"Employee Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Position: {position}")
    print()

for record in employee_records:
    print_employee(*record)

print("Number of Employee Records:", len(employee_records))

additional_record = ("Samuel Brown", 38, "Male", "Product Manager")
all_records = employee_records + (additional_record,)
print("\nAll Employee Records:")
for record in all_records:
    print_employee(*record)

search_record = ("Emily Davis", 30, "Female", "UX Designer")
if search_record in all_records:
    print(f"{search_record} found in Employee Records.")
else:
    print(f"{search_record} not found in Employee Records.")

# # Counting Element Occurrences in Tuples

# In[4]:

tuple_example = (1, 2, 3, 2, 4, 2, 5, 2)

count_of_twos = tuple_example.count(2)
count_of_fours = tuple_example.count(4)
count_of_sixes = tuple_example.count(6)

print("Tuple Example:", tuple_example)
print("Count of 2:", count_of_twos)
print("Count of 4:", count_of_fours)
print("Count of 6:", count_of_sixes)

def count_elements(t, element):
    count = 0
    for item in t:
        if item == element:
            count += 1
    return count

element_to_count = 2
result = count_elements(tuple_example, element_to_count)
print(f"\nCount of {element_to_count} using for loop:", result)

def count_elements_while(t, element):
    count = 0
    index = 0
    while index < len(t):
        if t[index] == element:
            count += 1
        index += 1
    return count

result_while = count_elements_while(tuple_example, element_to_count)
print(f"Count of {element_to_count} using while loop:", result_while)

# # Indexing and Slicing in Tuples
# In[5]:

tuple_example = (1, 'a', 3.14, 'Hello', [5, 6, 7])

print("Tuple Example:", tuple_example)
print("Element at index 0:", tuple_example[0])     
print("Element at index 3:", tuple_example[3])  
print("Last element:", tuple_example[-1])         
print()

print("Slicing Examples:")
print("First three elements:", tuple_example[:3]) 
print("Elements from index 2 to end:", tuple_example[2:])
print("Elements from index 1 to 3:", tuple_example[1:4]) 
print("Last three elements:", tuple_example[-3:]) 
print()

nested_tuple = ((1, 2), ('a', 'b', 'c'), (3.14, 2.71))

print("Nested Tuple Example:")
print("Element at index 0, 1:", nested_tuple[0][1])   
print("Elements from index 1 to end in tuple at index 1:", nested_tuple[1][1:]) 

first, second, third = nested_tuple
print("\nTuple Unpacking:")
print("First tuple:", first)
print("Second tuple:", second)
print("Third tuple:", third)

# # Built-in Functions in Tuples

# In[6]:

tuple_numbers = (10, 5, 7, 2, 1, 15, 6)

print("Tuple Numbers:", tuple_numbers)
print("Length of Tuple:", len(tuple_numbers))

print("\nSum of Tuple Elements:", sum(tuple_numbers))

print("\nMaximum Element in Tuple:", max(tuple_numbers))

sorted_tuple = sorted(tuple_numbers)
print("\nSorted Tuple:", sorted_tuple)

print("Original Tuple:", tuple_numbers)

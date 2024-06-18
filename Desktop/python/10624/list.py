
# # List Methods for Managing a Shopping Cart
# In[ ]:

shopping_cart = []

shopping_cart.append("Apples")
shopping_cart.append("Bananas")
shopping_cart.append("Milk")
shopping_cart.append("Bread")

print("Initial Shopping Cart:")
print(shopping_cart)

shopping_cart.insert(2, "Eggs")

print("\nShopping Cart after Insertion:")
print(shopping_cart)

shopping_cart.remove("Bananas")

print("\nShopping Cart after Removal:")
print(shopping_cart)

copied_cart = shopping_cart.copy()

print("\nCopied Shopping Cart:")
print(copied_cart)

apple_count = shopping_cart.count("Apples")
print("\nCount of 'Apples' in Shopping Cart:", apple_count)

additional_items = ["Cheese", "Yogurt"]
shopping_cart.extend(additional_items)

print("\nShopping Cart after Extension:")
print(shopping_cart)

milk_index = shopping_cart.index("Milk")
print("\nIndex of 'Milk' in Shopping Cart:", milk_index)

shopping_cart.sort()

print("\nShopping Cart after Sorting:")
print(shopping_cart)

shopping_cart.reverse()

print("\nShopping Cart after Reversing:")
print(shopping_cart)

shopping_cart.clear()

print("\nCleared Shopping Cart:")
print(shopping_cart)

shopping_cart = copied_cart.copy()

last_item = shopping_cart.pop()
print(f"\nRemoved Last Item '{last_item}' from Shopping Cart")
print("Remaining Shopping Cart:")
print(shopping_cart)

# # List Comprehension for Filtering and Transforming Data

# In[3]:

temperatures_celsius = [25, 30, 15, 18, 22, 28, 12, 20]

temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

print("Original Temperatures (Celsius):")
print(temperatures_celsius)
print("\nTemperatures (Fahrenheit):")
print(temperatures_fahrenheit)

high_temperatures = [temp for temp in temperatures_celsius if temp > 25]

print("\nHigh Temperatures (> 25°C):")
print(high_temperatures)

temperature_types = [("high" if temp > 25 else "normal") for temp in temperatures_celsius]

print("\nTemperature Types:")
print(temperature_types)

# # Indexing Operations on a List of Tasks

# In[4]:

tasks = ["Write report", "Prepare presentation", "Send email", "Attend meeting", "Review feedback"]

print("Initial List of Tasks:")
print(tasks)

first_task = tasks[0]
third_task = tasks[2]
last_task = tasks[-1]

print("\nPositive Indexing:")
print(f"First Task: {first_task}")
print(f"Third Task: {third_task}")
print(f"Last Task: {last_task}")

tasks[1] = "Revise presentation"

print("\nUpdated List of Tasks:")
print(tasks)

second_last_task = tasks[-2]
third_last_task = tasks[-3]

print("\nNegative Indexing:")
print(f"Second Last Task: {second_last_task}")
print(f"Third Last Task: {third_last_task}")

tasks[-3] = "Schedule meeting"

print("\nUpdated List of Tasks after Negative Indexing Update:")
print(tasks)

# # Slicing Operations on a List of Tasks
# In[5]:

tasks = ["Write report", "Prepare presentation", "Send email", "Attend meeting", "Review feedback"]

print("Initial List of Tasks:")
print(tasks)

first_three_tasks = tasks[0:3]  
last_two_tasks = tasks[-2:]    

print("\nPositive Slicing:")
print("First Three Tasks:", first_three_tasks)
print("Last Two Tasks:", last_two_tasks)

tasks[1:3] = ["Revise presentation", "Prepare agenda"]

print("\nUpdated List of Tasks after Positive Slicing Update:")
print(tasks)

middle_tasks = tasks[1:-1]     

print("\nNegative Slicing:")
print("Middle Tasks:", middle_tasks)

del tasks[-2:]  

print("\nUpdated List of Tasks after Negative Slicing Delete:")
print(tasks)

tasks = tasks[:2] + ["Call client"] + tasks[2:]

print("\nUpdated List of Tasks after Inserting 'Call client':")
print(tasks)

# # Searching and Sorting Operations on Student Scores

# In[6]:

scores = [78, 92, 64, 85, 72, 91, 88, 67]

print("Initial List of Scores:")
print(scores)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 

target_score = 85
index = linear_search(scores, target_score)

if index != -1:
    print(f"\nFound {target_score} at index {index}.")
else:
    print(f"\n{target_score} not found in scores.")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

bubble_sort(scores)

print("\nSorted List of Scores:")
print(scores)


# # Using Special Methods for Student Data Processing

# In[6]:
from functools import reduce

students = [
    {"name": "Alice", "age": 20, "gpa": 3.5},
    {"name": "Bob", "age": 21, "gpa": 3.2},
    {"name": "Charlie", "age": 19, "gpa": 3.8},
    {"name": "David", "age": 22, "gpa": 3.1},
    {"name": "Eve", "age": 20, "gpa": 3.9}
]

total_gpa = reduce(lambda acc, student: acc + student["gpa"], students, 0)

print("Total GPA of all students:", total_gpa)

capitalized_names = list(map(lambda student: student["name"].upper(), students))

print("\nCapitalized Names of Students:")
print(capitalized_names)

top_students = list(filter(lambda student: student["gpa"] > 3.5, students))

print("\nTop Students (GPA > 3.5):")
for student in top_students:
    print(student["name"], "- GPA:", student["gpa"])

names_ages = list(zip(map(lambda student: student["name"], students), map(lambda student: student["age"], students)))

print("\nNames and Ages of Students:")
for name, age in names_ages:
    print(f"{name} - Age: {age}")

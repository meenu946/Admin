
# # Accessing and Modifying Dictionaries
# In[ ]:

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "email": "john.doe@example.com"
}
print("Name:", person["name"])       
print("Age:", person["age"])         
print("City:", person["city"])      
print("Email:", person["email"])   
person["age"] = 32
person["city"] = "San Francisco"
print("\nModified Age:", person["age"])    
print("Modified City:", person["city"])  
person["phone"] = "123-456-7890"
print("\nUpdated Dictionary:", person)     
removed_email = person.pop("email")
print("\nRemoved Email:", removed_email)  
print("Updated Dictionary:", person)       

print("\nIterating through keys and values:")
for key, value in person.items():
    print(f"{key}: {value}")

if "phone" in person:
    print("\nPhone number exists in dictionary.")

person.clear()
print("\nCleared Dictionary:", person)     

del person

# # Dictionary Methods in Product Inventory Management

# In[3]:

inventory = {
    "1001": {"name": "Keyboard", "price": 29.99, "stock": 50},
    "1002": {"name": "Mouse", "price": 14.99, "stock": 75},
    "1003": {"name": "Monitor", "price": 199.99, "stock": 25},
    "1004": {"name": "Headphones", "price": 49.99, "stock": 30}
}

print("Product IDs:")
print(list(inventory.keys()))   
print("\nProduct Details:")
print(list(inventory.values())) 
print("\nProduct Inventory:")
for product_id, details in inventory.items():
    print(f"Product ID: {product_id}, Details: {details}")

print("\nProduct Details for ID 1002:")
print(inventory.get("1002"))   
removed_product = inventory.pop("1003")
print("\nRemoved Product Details:")
print(removed_product)         
print("Updated Inventory:")
print(inventory)             
inventory.clear()
print("\nCleared Inventory:")
print(inventory)           
original_inventory = {
    "1001": {"name": "Keyboard", "price": 29.99, "stock": 50},
    "1002": {"name": "Mouse", "price": 14.99, "stock": 75},
    "1003": {"name": "Monitor", "price": 199.99, "stock": 25},
    "1004": {"name": "Headphones", "price": 49.99, "stock": 30}
}
copied_inventory = original_inventory.copy()

copied_inventory["1001"]["stock"] = 45

print("\nOriginal Inventory:")
print(original_inventory)      
print("Copied Inventory:")
print(copied_inventory)         


# # Adding and Removing Key-Value Pairs in a Dictionary

# In[4]:

employees = {}

employees["E101"] = {"name": "John Doe", "age": 30, "department": "HR"}
employees["E102"] = {"name": "Jane Smith", "age": 25, "department": "Engineering"}
employees["E103"] = {"name": "Michael Johnson", "age": 35, "department": "Marketing"}

print("Initial Employee Dictionary:")
print(employees)

employees["E104"] = {"name": "Emily Brown", "age": 28, "department": "Sales"}
employees["E105"] = {"name": "David Lee", "age": 32, "department": "Finance"}

print("\nUpdated Employee Dictionary:")
print(employees)

removed_employee = employees.pop("E103")
print("\nRemoved Employee Details:")
print(removed_employee)

print("\nEmployee Dictionary after Removal:")
print(employees)

employees["E101"]["department"] = "Operations"

print("\nEmployee Dictionary after Modification:")
print(employees)

employees.clear()

print("\nCleared Employee Dictionary:")
print(employees)

# # Dictionary Comprehension for Student Grades
# In[5]:

student_grades = {
    "John": 85,
    "Jane": 92,
    "Doe": 78,
    "Emily": 95,
    "David": 88
}

grade_categories = {name: 'Pass' if score >= 80 else 'Fail' for name, score in student_grades.items()}

print("Student Grades:")
print(student_grades)

print("\nCategorized Grades:")
print(grade_categories)

# # Nested Dictionaries for Company Departments and Employees

# In[6]:

company = {
    "HR": {
        "employees": [
            {"name": "John Doe", "age": 30, "position": "HR Manager"},
            {"name": "Jane Smith", "age": 25, "position": "HR Assistant"}
        ],
        "head": "Michael Johnson"
    },
    "Engineering": {
        "employees": [
            {"name": "David Lee", "age": 32, "position": "Software Engineer"},
            {"name": "Emily Brown", "age": 28, "position": "System Analyst"}
        ],
        "head": "Andrew Wilson"
    },
    "Marketing": {
        "employees": [
            {"name": "Mark Davis", "age": 35, "position": "Marketing Manager"},
            {"name": "Emma Garcia", "age": 27, "position": "Marketing Specialist"}
        ],
        "head": "Sarah Martinez"
    }
}

print("Company Departments and Employees:")

for department, info in company.items():
    print(f"\nDepartment: {department}")
    print(f"Department Head: {info['head']}")
    print("Employees:")
    for employee in info["employees"]:
        print(f"- Name: {employee['name']}, Age: {employee['age']}, Position: {employee['position']}")

print("\nAccessing Specific Information:")
print("HR Department Head:", company["HR"]["head"])
print("Engineering Employees:", company["Engineering"]["employees"])

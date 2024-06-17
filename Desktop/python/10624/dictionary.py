
# # creating and accesing elements in a dictionary
# In[ ]:


fruits = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "date": "brown"
}

print(fruits["apple"])    
print(fruits["banana"])   


# # adding and modifying elements in a dictionary

# In[3]:


student_grades = {}

student_grades["Alice"] = 90
student_grades["Bob"] = 85

student_grades["Alice"] = 95

print(student_grades) 


# # removing elements from a dictionary

# In[4]:


cities = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000
}

population = cities.pop("Chicago")
print(population)  
print(cities)      

last_city = cities.popitem()
print(last_city)   
print(cities)      


# # iterating over a dictionary
# In[5]:

countries = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

for country in countries:
    print(country)

for capital in countries.values():
    print(capital)

for country, capital in countries.items():
    print(f"The capital of {country} is {capital}")



# # dictionary comprehensions

# In[6]:

squares = {x: x**2 for x in range(1, 6)}
print(squares)  

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares) 



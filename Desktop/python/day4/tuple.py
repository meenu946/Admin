
# # creating and accesing elements in a tuple
# In[ ]:


fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])  
print(fruits[2])  


print(fruits[-1])  




# # tuple unpacking

# In[3]:


person = ("John", 30, "Engineer")

name, age, profession = person

print(name)       
print(age)       
print(profession) 



# # tuples are immutable

# In[4]:


colors = ("red", "green", "blue")

try:
    colors[1] = "yellow"
except TypeError as e:
    print(e) 



# # iterating over a tuple
# In[5]:


animals = ("cat", "dog", "elephant")

for animal in animals:
    print(animal)


# # using tuples as keys in a dictionary

# In[6]:


location_coordinates = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, -0.1278): "London"
}

print(location_coordinates[(40.7128, -74.0060)])  
print(location_coordinates[(51.5074, -0.1278)])  







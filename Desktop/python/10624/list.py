
# # creating and accesing elements in a list
# In[ ]:


fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  
print(fruits[2])  

print(fruits[-1])  




# # modifying elements in a list

# In[3]:


numbers = [1, 2, 3, 4, 5]

numbers[1] = 20
numbers[3] = 40

print(numbers) 




# # adding and removing elements in a list

# In[4]:


colors = ["red", "green", "blue"]

colors.append("yellow")
colors.insert(1, "orange")

colors.remove("green")
popped_color = colors.pop()  

print(colors)        
print(popped_color)   




# # List comprehensions 
# In[5]:



squares = [x**2 for x in range(1, 6)]
print(squares) 


evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  



# # iterating over a list 

# In[6]:



animals = ["cat", "dog", "elephant"]


for animal in animals:
    print(animal)


for index in range(len(animals)):
    print(f"Index {index}: {animals[index]}")






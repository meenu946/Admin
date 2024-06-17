
# # basic inheritance
# In[ ]:


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.speak()) 



# # multi level inheritance

# In[3]:


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"

my_cat = Cat("Whiskers", "Brown")
print(my_cat.speak())      
print(my_cat.fur_color)   




# # hierarchial inheritance

# In[4]:


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")
print(my_dog.speak())
print(my_cat.speak())  




# # multiple inheritance

# In[5]:


class Walkable:
    def walk(self):
        return "I can walk."

class Swimmable:
    def swim(self):
        return "I can swim."

class Amphibian(Walkable, Swimmable):
    def describe(self):
        return "I am an amphibian."

frog = Amphibian()
print(frog.walk())     
print(frog.swim())      
print(frog.describe())  




# # using super() to access parent methods

# In[6]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_details(self):
        parent_details = super().get_details()
        return f"{parent_details}, Employee ID: {self.employee_id}"

employee = Employee("John Doe", 30, "E12345")
print(employee.get_details())  






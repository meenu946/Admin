
# # class and object

# In[ ]:


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} is barking!"

my_dog = Dog("Buddy", 3)
print(my_dog.name) 
print(my_dog.age)   
print(my_dog.bark()) 



# # inheritance

# In[3]:


class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        pass

class Cat(Animal):
    def __init__(self, name, species="Cat"):
        super().__init__(species)
        self.name = name

    def sound(self):
        return "Meow"

my_cat = Cat("Whiskers")
print(my_cat.species) 
print(my_cat.name)    
print(my_cat.sound()) 



# # encapsulation

# In[4]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  



# # polymorphism

# In[5]:


class Bird:
    def sound(self):
        pass

class Sparrow(Bird):
    def sound(self):
        return "Chirp"

class Duck(Bird):
    def sound(self):
        return "Quack"

def make_sound(bird):
    print(bird.sound())

sparrow = Sparrow()
duck = Duck()
make_sound(sparrow)  
make_sound(duck)     



# # method overriding

# In[6]:


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        return f"Vehicle: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def description(self):
        return f"Car: {self.make} {self.model}, Doors: {self.doors}"

my_car = Car("Toyota", "Corolla", 4)
print(my_car.description())  





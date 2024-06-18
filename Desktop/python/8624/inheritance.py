
# # Vehicle Hierarchy with Inheritance and MRO
# In[ ]:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, {self.num_doors} doors"


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()}, Battery: {self.battery_capacity} kWh"


class ElectricCar(Car, ElectricVehicle):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        Car.__init__(self, make, model, year, num_doors)
        ElectricVehicle.__init__(self, make, model, year, battery_capacity)

def main():
    car1 = Car("Toyota", "Camry", 2020, 4)
    print(car1.display_info()) 

    ev1 = ElectricVehicle("Tesla", "Model S", 2022, 100)
    print(ev1.display_info())  

    electric_car1 = ElectricCar("Nissan", "Leaf", 2021, 4, 40)
    print(electric_car1.display_info())  

    print(ElectricCar.mro())  
if __name__ == "__main__":
    main()

# # Types of Inheritance in Employee Hierarchy

# In[3]:

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display_info(self):
        return f"Manager - {super().display_info()}, Department: {self.department}"

class Skills:
    def __init__(self, skills):
        self.skills = skills

    def display_skills(self):
        return f"Skills: {', '.join(self.skills)}"


class Developer(Employee, Skills):
    def __init__(self, name, emp_id, skills):
        Employee.__init__(self, name, emp_id)
        Skills.__init__(self, skills)

    def display_info(self):
        return f"Developer - {super().display_info()}, {super().display_skills()}"

class TeamLead(Manager):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    def display_info(self):
        return f"Team Lead - {super().display_info()}, Team Size: {self.team_size}"

class Tester(Employee):
    def __init__(self, name, emp_id, experience):
        super().__init__(name, emp_id)
        self.experience = experience

    def display_info(self):
        return f"Tester - {super().display_info()}, Experience: {self.experience} years"


class Designer(Employee):
    def __init__(self, name, emp_id, software):
        super().__init__(name, emp_id)
        self.software = software

    def display_info(self):
        return f"Designer - {super().display_info()}, Software: {self.software}"

class ProductManager(Manager, Skills):
    def __init__(self, name, emp_id, department, skills, product):
        Manager.__init__(self, name, emp_id, department)
        Skills.__init__(self, skills)
        self.product = product

    def display_info(self):
        return f"Product Manager - {super().display_info()}, {super().display_skills()}, Product: {self.product}"

def main():
  
    manager = Manager("John Doe", "M001", "Engineering")
    print(manager.display_info())

    developer = Developer("Alice Smith", "D001", ["Python", "JavaScript", "SQL"])
    print(developer.display_info())

    team_lead = TeamLead("Jane Brown", "TL001", "Engineering", 8)
    print(team_lead.display_info())

    tester = Tester("Michael Green", "T001", 5)
    designer = Designer("Emily White", "D002", "Adobe Suite")
    print(tester.display_info())
    print(designer.display_info())

    product_manager = ProductManager("Sarah Lee", "PM001", "Product Management", ["Market Analysis", "Project Management"], "New Product Launch")
    print(product_manager.display_info())

if __name__ == "__main__":
    main()

# # Method Overriding with Animals

# In[4]:
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

    def info(self):
        return f"I am {self.name}, and I make {self.make_sound()}"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

class Duck(Animal):
    def make_sound(self):
        return "Quack"

def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    cow = Cow("Bessie")
    duck = Duck("Daffy")

    print(dog.info()) 
    print(cat.info())  
    print(cow.info()) 
    print(duck.info()) 

if __name__ == "__main__":
    main()

# # Using super() with __init__() and __str__() Methods

# In[5]:
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def __str__(self):
        return f"Manager - {super().__str__()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, emp_id, skills):
        super().__init__(name, emp_id)
        self.skills = skills

    def __str__(self):
        return f"Developer - {super().__str__()}, Skills: {', '.join(self.skills)}"

class Tester(Employee):
    def __init__(self, name, emp_id, experience):
        super().__init__(name, emp_id)
        self.experience = experience

    def __str__(self):
        return f"Tester - {super().__str__()}, Experience: {self.experience} years"

def main():
    manager = Manager("John Doe", "M001", "Engineering")
    developer = Developer("Alice Smith", "D001", ["Python", "JavaScript", "SQL"])
    tester = Tester("Michael Green", "T001", 5)

    print(manager)    
    print(developer)   
    print(tester)      

if __name__ == "__main__":
    main()






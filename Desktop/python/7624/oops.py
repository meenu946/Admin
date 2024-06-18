
# # class and object - banking system

# In[ ]:

class BankAccount:
   
    def __init__(self, account_number, account_holder, balance=0.0):
      
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid amount. Deposit failed.")
    
    def withdraw(self, amount):
       
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient balance. Withdrawal failed.")
    
    def check_balance(self):
        
        print(f"Account balance is ${self.balance}.")
    
    def __str__(self):
        
        return f"Bank Account #{self.account_number} of {self.account_holder} with balance ${self.balance}"


class SavingsAccount(BankAccount):
    
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.05):
       
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
       
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest added. New balance is ${self.balance}.")


account1 = BankAccount("101", "Alice")
account2 = BankAccount("102", "Bob", 1000.0)

account1.deposit(500)
account2.withdraw(200)
account2.check_balance()

savings_account1 = SavingsAccount("201", "Claire", 500.0, 0.03)
savings_account2 = SavingsAccount("202", "David", 1000.0)

savings_account1.deposit(1000)
savings_account1.add_interest()
savings_account2.withdraw(500)
savings_account2.check_balance()

print("\nBank Account Details:")
print(account1)
print(account2)
print("\nSavings Account Details:")
print(savings_account1)
print(savings_account2)
 



# # Employee Management System with Instance and Class Variables

# In[3]:


class Employee:
   
    num_of_employees = 0
    raise_amount = 1.05 
    
    def __init__(self, first_name, last_name, salary):
       
        self.first_name = first_name  
        self.last_name = last_name    
        self.salary = salary        
        
        Employee.num_of_employees += 1 
        
    def full_name(self):
        
        return f"{self.first_name} {self.last_name}"
    
    def apply_raise(self):
        
        self.salary = int(self.salary * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
       
        cls.raise_amount = amount
    
    @staticmethod
    def is_workday(day):
        
        return day.weekday() in range(5)

emp1 = Employee("Alice", "Smith", 50000)
emp2 = Employee("Bob", "Johnson", 60000)

print(f"Employee 1: {emp1.full_name()}, Salary: ${emp1.salary}")
print(f"Employee 2: {emp2.full_name()}, Salary: ${emp2.salary}")

print(f"Number of Employees: {Employee.num_of_employees}")

emp1.apply_raise()
print(f"After raise: {emp1.full_name()}, New Salary: ${emp1.salary}")

Employee.set_raise_amount(1.06)

emp2.apply_raise()
print(f"After raise: {emp2.full_name()}, New Salary: ${emp2.salary}")

import datetime
day = datetime.date(2024, 6, 7) 
print(f"Is {day} a workday? {Employee.is_workday(day)}")



# # Car Class with Different Types of Methods

# In[4]:


class Car:
    
    num_of_cars = 0
    
    def __init__(self, make, model, year, mileage):
        
        self.make = make        # Instance variable
        self.model = model      # Instance variable
        self.year = year        # Instance variable
        self.mileage = mileage  # Instance variable
        
        Car.num_of_cars += 1    # Increment class variable
    
    def display_info(self):
        
        return f"{self.year} {self.make} {self.model}, Mileage: {self.mileage} miles"
    
    def drive(self, miles):
        
        if miles > 0:
            self.mileage += miles
            print(f"Driving {miles} miles.")
        else:
            print("Invalid miles. Drive operation failed.")
    
    @staticmethod
    def check_electric(car):
       
        return car.make.lower() in ['tesla', 'bmw i3', 'nissan leaf']
    
    @classmethod
    def from_string(cls, car_string):
        
        make, model, year, mileage = car_string.split(',')
        return cls(make, model, int(year), int(mileage))

car1 = Car("Toyota", "Camry", 2020, 15000)
car2 = Car("Tesla", "Model S", 2021, 5000)

print(car1.display_info())
print(car2.display_info())

car1.drive(100)
car2.drive(200)

print(f"Is {car1.make} {car1.model} electric? {Car.check_electric(car1)}")
print(f"Is {car2.make} {car2.model} electric? {Car.check_electric(car2)}")

car3 = Car.from_string("Honda,Civic,2019,20000")
print(car3.display_info())

print(f"Number of Cars: {Car.num_of_cars}")

# # Book Class with Special Methods

# In[5]:


class Book:
    
    def __new__(cls, title, author, price):
       
        print(f"Creating new instance of {title} by {author}")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, title, author, price):
       
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        
        return f"{self.title} by {self.author}, Price: ${self.price:.2f}"

book1 = Book("Python Crash Course", "Eric Matthes", 29.99)
book2 = Book("Clean Code", "Robert C. Martin", 39.95)

print(book1)
print(book2)



# # Employee Class with Constructors and Destructor-like Behavior

# In[6]:

class Employee:
    
    num_of_employees = 0
    
    def __init__(self, first_name, last_name, salary=0.0):
       
        self.first_name = first_name  
        self.last_name = last_name   
        self.salary = salary          
        
        Employee.num_of_employees += 1  
        print(f"Employee {self.full_name()} created.")
    
    def full_name(self):
       
        return f"{self.first_name} {self.last_name}"
    
    def display_info(self):
       
        return f"Employee: {self.full_name()}, Salary: ${self.salary}"
    
    def __del__(self):
       
        print(f"Employee {self.full_name()} is being deleted.")
        Employee.num_of_employees -= 1

emp1 = Employee("Alice", "Smith")
emp2 = Employee("Bob", "Johnson", 60000.0)
emp3 = Employee("Claire", "Davis", 75000.0)

print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())

print(f"Number of Employees: {Employee.num_of_employees}")




# # BankAccount and Transaction Classes

# In[ ]:

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
      
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def transfer(self, amount, to_account):
       
        if self.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False
    
    def __str__(self):
        
        return f"Account {self.account_number}, Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


class Transaction:
   
    def __init__(self, from_account, to_account, amount):
       
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
    
    def execute(self):
        
        if self.from_account.transfer(self.amount, self.to_account):
            return True
        return False
    
    def get_details(self):
        
        return f"Transaction from {self.from_account.account_number} to {self.to_account.account_number}, Amount: ${self.amount:.2f}"

account1 = BankAccount("123456", "Alice", 5000.0)
account2 = BankAccount("789012", "Bob", 3000.0)

print(account1)
print(account2)

account1.deposit(1500.0)
print(account1)

account2.withdraw(500.0)
print(account2)

transaction1 = Transaction(account1, account2, 2000.0)
if transaction1.execute():
    print("Transaction successful.")
else:
    print("Transaction failed.")
print(account1)
print(account2)

print(transaction1.get_details())

class Calculator:
    
    def add(self, a, b, c=0):
        
        return a + b + c

calc = Calculator()
print(f"Sum of 2 and 3: {calc.add(2, 3)}")
print(f"Sum of 2, 3, and 4: {calc.add(2, 3, 4)}")



# # BankAccount Class with Data Encapsulation

# In[3]:

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
       
        self.__account_number = account_number  
        self.__account_holder = account_holder  
        self.__balance = balance                
    
    def deposit(self, amount):
        
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
       
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        
        return self.__balance
    
    def get_account_holder(self):
       
        return self.__account_holder
    
    def get_account_number(self):
       
        return self.__account_number
    
    def set_account_holder(self, new_holder):
       
        self.__account_holder = new_holder
    
    def __str__(self):
       
        return f"Account {self.__account_number}, Holder: {self.__account_holder}, Balance: ${self.__balance:.2f}"

account = BankAccount("123456", "Alice", 5000.0)

print(account)

account.deposit(1500.0)
print(account)

account.withdraw(500.0)
print(account)

print(f"Account Holder: {account.get_account_holder()}")
print(f"Account Number: {account.get_account_number()}")
print(f"Account Balance: ${account.get_balance()}")

account.set_account_holder("Alice Johnson")
print(account)


# # Online Payment System with Data Abstraction

# In[4]:


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
   
    @abstractmethod
    def authorize_payment(self, amount):
        
        pass

    @abstractmethod
    def process_payment(self, amount):
       
        pass


class CreditCard(PaymentMethod):
    
    def __init__(self, card_number, card_holder, expiry_date):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date

    def authorize_payment(self, amount):
        print(f"Authorizing credit card payment for {self.card_holder}.")
       
        return True

    def process_payment(self, amount):
        if self.authorize_payment(amount):
            print(f"Processing credit card payment of ${amount:.2f} for {self.card_holder}.")
            
            return True
        return False


class PayPal(PaymentMethod):
   
    def __init__(self, email):
        self.email = email

    def authorize_payment(self, amount):
        print(f"Authorizing PayPal payment for {self.email}.")
       
        return True

    def process_payment(self, amount):
        if self.authorize_payment(amount):
            print(f"Processing PayPal payment of ${amount:.2f} for {self.email}.")
           
            return True
        return False


class BankTransfer(PaymentMethod):
    
    def __init__(self, account_number, account_holder, bank_name):
        self.account_number = account_number
        self.account_holder = account_holder
        self.bank_name = bank_name

    def authorize_payment(self, amount):
        print(f"Authorizing bank transfer payment for {self.account_holder}.")
        
        return True

    def process_payment(self, amount):
        if self.authorize_payment(amount):
            print(f"Processing bank transfer payment of ${amount:.2f} for {self.account_holder}.")
            
            return True
        return False

def make_payment(payment_method, amount):
    
    if payment_method.process_payment(amount):
        print("Payment successful.")
    else:
        print("Payment failed.")

credit_card = CreditCard("1234-5678-9012-3456", "Alice Smith", "12/24")
paypal = PayPal("alice@example.com")
bank_transfer = BankTransfer("9876543210", "Alice Smith", "Bank of Python")

make_payment(credit_card, 150.0)
make_payment(paypal, 75.0)
make_payment(bank_transfer, 300.0)


# # Book Class with Data hiding

# In[5]:


class BankAccount:
    
    def __init__(self, account_number, account_holder, balance=0.0):
        
        self.__account_number = account_number  
        self.__account_holder = account_holder 
        self.__balance = balance               
    
    def deposit(self, amount):
       
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
            return True
        print("Deposit amount must be positive.")
        return False
    
    def withdraw(self, amount):
       
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
            return True
        print("Insufficient balance or invalid amount.")
        return False
    
    def get_balance(self):
        
        return self.__balance
    
    def get_account_holder(self):
       
        return self.__account_holder
    
    def get_account_number(self):
       
        return self.__account_number
    
    def set_account_holder(self, new_holder):
        
        if new_holder:
            self.__account_holder = new_holder
            print(f"Account holder name updated to {self.__account_holder}.")
        else:
            print("Invalid account holder name.")
    
    def __str__(self):
       
        return f"Account {self.__account_number}, Holder: {self.__account_holder}, Balance: ${self.__balance:.2f}"

account = BankAccount("123456", "Alice", 5000.0)

print(account)

account.deposit(1500.0)
print(account)

account.withdraw(500.0)
print(account)

print(f"Account Holder: {account.get_account_holder()}")
print(f"Account Number: {account.get_account_number()}")
print(f"Account Balance: ${account.get_balance()}")

account.set_account_holder("Alice Johnson")
print(account)

try:
    print(account.__balance)  
except AttributeError as e:
    print(e)

try:
    account.__balance = 10000  
except AttributeError as e:
    print(e)

print(f"Actual private balance: {account._BankAccount__balance}")



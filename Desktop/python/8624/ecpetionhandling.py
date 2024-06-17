
# # basic exception handling
# In[ ]:


try:
    x = int(input("Enter a number: "))
    print(f"The number you entered is {x}")
except ValueError:
    print("That's not a valid number!")


# # handling multiple exceptions

# In[3]:


try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = a / b
    print(f"The result is {result}")
except ValueError:
    print("Invalid input! Please enter integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")


# # using else and finnaly blocks

# In[4]:


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x + y
except ValueError:
    print("Invalid input! Please enter integers.")
else:
    print(f"The result is {result}")
finally:
    print("Execution completed.")



# # raising custom exceptions

# In[5]:


class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
    print(f"The number you entered is {num}")
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter an integer.")




# # custom exception classes

# In[6]:


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: balance {balance}, amount {amount}")
        self.balance = balance
        self.amount = amount

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(100)
    amount_to_withdraw = int(input("Enter amount to withdraw: "))
    new_balance = account.withdraw(amount_to_withdraw)
    print(f"Withdrawal successful. New balance: {new_balance}")
except InsufficientFundsError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter an integer.")







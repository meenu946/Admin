
# # ATM Application with Basic Exception Handling
# In[ ]:
class InsufficientFundsError(Exception):
   
    def __init__(self, balance, amount):
        super().__init__(f"Attempt to withdraw ${amount:.2f} with only ${balance:.2f} in account.")
        self.balance = balance
        self.amount = amount


class InvalidAmountError(Exception):
    
    def __init__(self, amount):
        super().__init__(f"Invalid amount: ${amount:.2f}. Amount must be positive.")
        self.amount = amount


class ATM:
   
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
       
        if amount <= 0:
            raise InvalidAmountError(amount)
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
       
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):

        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

def main():
    atm = ATM(1000.0)

    while True:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '3':
                atm.check_balance()
            elif choice == '4':
                print("Exiting the ATM. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except InvalidAmountError as e:
            print(e)
        except InsufficientFundsError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

# # E-Commerce Order Processing System - multiple exceptions

# In[3]:
class InvalidProductIDError(Exception):
   
    def __init__(self, product_id):
        super().__init__(f"Invalid product ID: {product_id}")
        self.product_id = product_id


class OutOfStockError(Exception):
   
    def __init__(self, product_id):
        super().__init__(f"Product ID {product_id} is out of stock.")
        self.product_id = product_id


class PaymentFailedError(Exception):
 
    def __init__(self, reason):
        super().__init__(f"Payment failed: {reason}")
        self.reason = reason


class Product:
  
    def __init__(self, product_id, name, stock, price):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price


class PaymentProcessor:
    
    def process_payment(self, amount):
       
        if amount <= 0:
            raise PaymentFailedError("Invalid payment amount.")
      
        import random
        if random.choice([True, False]):
            raise PaymentFailedError("Transaction declined by bank.")
        print(f"Payment of ${amount:.2f} processed successfully.")


class OrderProcessor:
 
    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 10, 999.99),
            2: Product(2, "Smartphone", 5, 499.99),
            3: Product(3, "Headphones", 0, 149.99), 
        }
        self.payment_processor = PaymentProcessor()

    def process_order(self, product_id, quantity, payment_amount):
 
        if product_id not in self.products:
            raise InvalidProductIDError(product_id)
        
        product = self.products[product_id]
        
        if product.stock < quantity:
            raise OutOfStockError(product_id)
        
        total_cost = product.price * quantity
        
        if payment_amount < total_cost:
            raise PaymentFailedError("Insufficient payment amount.")

        self.payment_processor.process_payment(payment_amount)
        
        product.stock -= quantity
        print(f"Order processed successfully for {quantity} unit(s) of {product.name}.")

def main():
    order_processor = OrderProcessor()

    orders = [
        (1, 2, 2000.00),  
        (2, 1, 300.00),  
        (3, 1, 200.00),  
        (4, 1, 100.00),  
        (2, 1, 600.00),   
    ]

    for product_id, quantity, payment_amount in orders:
        try:
            print(f"\nProcessing order: Product ID={product_id}, Quantity={quantity}, Payment=${payment_amount:.2f}")
            order_processor.process_order(product_id, quantity, payment_amount)
        except InvalidProductIDError as e:
            print(f"Error: {e}")
        except OutOfStockError as e:
            print(f"Error: {e}")
        except PaymentFailedError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

# # Enhanced E-Commerce Order Processing System with else and finally Blocks

# In[4]:

class InvalidProductIDError(Exception):
   
    def __init__(self, product_id):
        super().__init__(f"Invalid product ID: {product_id}")
        self.product_id = product_id


class OutOfStockError(Exception):
   
    def __init__(self, product_id):
        super().__init__(f"Product ID {product_id} is out of stock.")
        self.product_id = product_id


class PaymentFailedError(Exception):
   
    def __init__(self, reason):
        super().__init__(f"Payment failed: {reason}")
        self.reason = reason


class Product:
  
    def __init__(self, product_id, name, stock, price):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price


class PaymentProcessor:
  
    def process_payment(self, amount):
       
        if amount <= 0:
            raise PaymentFailedError("Invalid payment amount.")
      
        import random
        if random.choice([True, False]):
            raise PaymentFailedError("Transaction declined by bank.")
        print(f"Payment of ${amount:.2f} processed successfully.")


class Receipt:
   
    def generate_receipt(self, order_details):
      
        print("\nGenerating receipt...")
        print(f"Order Receipt:\n{order_details}")
        print("Receipt generated successfully.")


class OrderProcessor:

    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 10, 999.99),
            2: Product(2, "Smartphone", 5, 499.99),
            3: Product(3, "Headphones", 0, 149.99), 
        }
        self.payment_processor = PaymentProcessor()
        self.receipt = Receipt()

    def process_order(self, product_id, quantity, payment_amount):
     
        order_details = None
        try:
            if product_id not in self.products:
                raise InvalidProductIDError(product_id)
            
            product = self.products[product_id]
            
            if product.stock < quantity:
                raise OutOfStockError(product_id)
            
            total_cost = product.price * quantity
            
            if payment_amount < total_cost:
                raise PaymentFailedError("Insufficient payment amount.")
            
            self.payment_processor.process_payment(payment_amount)
            
            product.stock -= quantity

            order_details = (f"Product: {product.name}\n"
                             f"Quantity: {quantity}\n"
                             f"Total Cost: ${total_cost:.2f}\n"
                             f"Payment: ${payment_amount:.2f}")

            print(f"Order processed successfully for {quantity} unit(s) of {product.name}.")

        except InvalidProductIDError as e:
            print(f"Error: {e}")
        except OutOfStockError as e:
            print(f"Error: {e}")
        except PaymentFailedError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
           
            self.receipt.generate_receipt(order_details)
        finally:
            print("Cleaning up resources...\n")

def main():
    order_processor = OrderProcessor()

    orders = [
        (1, 2, 2000.00),  
        (2, 1, 300.00),  
        (3, 1, 200.00),   
        (4, 1, 100.00), 
        (2, 1, 600.00),   
    ]

    for product_id, quantity, payment_amount in orders:
        print(f"Processing order: Product ID={product_id}, Quantity={quantity}, Payment=${payment_amount:.2f}")
        order_processor.process_order(product_id, quantity, payment_amount)

if __name__ == "__main__":
    main()


# # Enhanced E-Commerce Order Processing System with Common Built-in Exceptions

# In[5]:
class InvalidProductIDError(Exception):
   
    def __init__(self, product_id):
        super().__init__(f"Invalid product ID: {product_id}")
        self.product_id = product_id


class OutOfStockError(Exception):
    
    def __init__(self, product_id):
        super().__init__(f"Product ID {product_id} is out of stock.")
        self.product_id = product_id


class PaymentFailedError(Exception):
   
    def __init__(self, reason):
        super().__init__(f"Payment failed: {reason}")
        self.reason = reason


class Product:
   
    def __init__(self, product_id, name, stock, price):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price


class PaymentProcessor:
    
    def process_payment(self, amount):
       
        if amount <= 0:
            raise PaymentFailedError("Invalid payment amount.")
        # Simulate a random payment failure
        import random
        if random.choice([True, False]):
            raise PaymentFailedError("Transaction declined by bank.")
        print(f"Payment of ${amount:.2f} processed successfully.")


class Receipt:
    
    def generate_receipt(self, order_details):
       
        print("\nGenerating receipt...")
        print(f"Order Receipt:\n{order_details}")
        print("Receipt generated successfully.")


class OrderProcessor:
 
    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 10, 999.99),
            2: Product(2, "Smartphone", 5, 499.99),
            3: Product(3, "Headphones", 0, 149.99),  # Out of stock
        }
        self.payment_processor = PaymentProcessor()
        self.receipt = Receipt()

    def process_order(self, product_id, quantity, payment_amount):
      
        order_details = None
        try:
            if not isinstance(product_id, int):
                raise TypeError("Product ID must be an integer.")
            if not isinstance(quantity, int):
                raise TypeError("Quantity must be an integer.")
            if not isinstance(payment_amount, (int, float)):
                raise TypeError("Payment amount must be a number.")

            if product_id not in self.products:
                raise InvalidProductIDError(product_id)
            
            product = self.products[product_id]
            
            if product.stock < quantity:
                raise OutOfStockError(product_id)
            
            total_cost = product.price * quantity
            
            if payment_amount < total_cost:
                raise PaymentFailedError("Insufficient payment amount.")
            
            self.payment_processor.process_payment(payment_amount)

            product.stock -= quantity

            order_details = (f"Product: {product.name}\n"
                             f"Quantity: {quantity}\n"
                             f"Total Cost: ${total_cost:.2f}\n"
                             f"Payment: ${payment_amount:.2f}")

            print(f"Order processed successfully for {quantity} unit(s) of {product.name}.")

        except InvalidProductIDError as e:
            print(f"Error: {e}")
        except OutOfStockError as e:
            print(f"Error: {e}")
        except PaymentFailedError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except TypeError as e:
            print(f"Type error: {e}")
        except KeyError as e:
            print(f"Key error: {e}")
        except ZeroDivisionError as e:
            print(f"Zero division error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
           
            self.receipt.generate_receipt(order_details)
        finally:
            print("Cleaning up resources...\n")

def main():
    order_processor = OrderProcessor()

    orders = [
        (1, 2, 2000.00),  
        (2, 1, 300.00),  
        (3, 1, 200.00),  
        (4, 1, 100.00),  
        (2, 1, 600.00),  
        ('a', 1, 500.00), 
        (2, '1', 500.00), 
        (2, 1, 'five'),   
        (2, 1, 0),        
    ]

    for product_id, quantity, payment_amount in orders:
        print(f"Processing order: Product ID={product_id}, Quantity={quantity}, Payment=${payment_amount:.2f}")
        order_processor.process_order(product_id, quantity, payment_amount)

if __name__ == "__main__":
    main()

# # cLibrary Management System with Custom Exceptions

# In[6]:
class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
   
    def __init__(self, book_title):
        super().__init__(f"Book '{book_title}' not found in the library.")
        self.book_title = book_title


class BookAlreadyBorrowedError(LibraryError):
   
    def __init__(self, book_title):
        super().__init__(f"Book '{book_title}' is already borrowed.")
        self.book_title = book_title


class BookNotBorrowedError(LibraryError):
   
    def __init__(self, book_title):
        super().__init__(f"Book '{book_title}' was not borrowed by the user.")
        self.book_title = book_title


class OverdueBookError(LibraryError):
   
    def __init__(self, book_title, days_overdue):
        super().__init__(f"Book '{book_title}' is overdue by {days_overdue} days.")
        self.book_title = book_title
        self.days_overdue = days_overdue


class Book:
   
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None


class User:
   
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book, library, current_date):
        if book.title in self.borrowed_books:
            raise BookAlreadyBorrowedError(book.title)
        
        library.lend_book(book, self, current_date)
        self.borrowed_books[book.title] = book
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book, library, return_date):
        if book.title not in self.borrowed_books:
            raise BookNotBorrowedError(book.title)
        
        overdue_days = library.receive_book(book, return_date)
        if overdue_days > 0:
            raise OverdueBookError(book.title, overdue_days)
        
        del self.borrowed_books[book.title]
        print(f"{self.name} returned '{book.title}'.")


class Library:
   
    def __init__(self):
        self.books = {}
        self.borrow_period = 14  

    def add_book(self, book):
        self.books[book.title] = book
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def find_book(self, title):
        if title not in self.books:
            raise BookNotFoundError(title)
        return self.books[title]

    def lend_book(self, book, user, current_date):
        if book.is_borrowed:
            raise BookAlreadyBorrowedError(book.title)
        book.is_borrowed = True
        book.borrowed_by = user
        book.due_date = current_date + self.borrow_period
        print(f"Book '{book.title}' lent to {user.name}. Due date: {book.due_date}")

    def receive_book(self, book, return_date):
        if not book.is_borrowed:
            raise BookNotBorrowedError(book.title)
        
        book.is_borrowed = False
        book.borrowed_by = None
        overdue_days = return_date - book.due_date
        book.due_date = None
        if overdue_days > 0:
            return overdue_days
        return 0

def main():
  
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    user1 = User("Alice")
    user2 = User("Bob")

    current_date = 1

    try:
        user1.borrow_book(book1, library, current_date)
        user2.borrow_book(book2, library, current_date)
        user2.borrow_book(book3, library, current_date)
        user2.borrow_book(book1, library, current_date)  
    except LibraryError as e:
        print(f"Error: {e}")

    return_date = 20 
    try:
        user1.return_book(book1, library, return_date)  
    except LibraryError as e:
        print(f"Error: {e}")

    try:
        user2.return_book(book2, library, return_date)
        user2.return_book(book1, library, return_date)  
    except LibraryError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

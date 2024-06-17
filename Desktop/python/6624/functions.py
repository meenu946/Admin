
# # parameters

# In[ ]:


def example_function(positional1, positional2, keyword1="default1", keyword2="default2", *args, **kwargs):
    
    print(f"Positional1: {positional1}")
    print(f"Positional2: {positional2}")
    
    print(f"Keyword1: {keyword1}")
    print(f"Keyword2: {keyword2}")
    
    if args:
        print("Additional positional arguments (args):")
        for i, arg in enumerate(args, start=1):
            print(f"  arg{i}: {arg}")
    else:
        print("No additional positional arguments (args).")
    
    if kwargs:
        print("Additional keyword arguments (kwargs):")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    else:
        print("No additional keyword arguments (kwargs).")
    
    print("\nFunction execution completed.\n")


# # logging system - passing function as arguments

# In[3]:


import datetime

def log_to_console(message):
    print(f"{datetime.datetime.now()} - CONSOLE: {message}")

def log_to_file(message, filename="log.txt"):
    with open(filename, "a") as file:
        file.write(f"{datetime.datetime.now()} - FILE: {message}\n")

# Define the logging handler function
def log_message(message, log_function, *args, **kwargs):
    log_function(message, *args, **kwargs)

log_message("This is a console log message.", log_to_console)

log_message("This is a file log message.", log_to_file, filename="my_log.txt")


# # sorting - lambda function

# In[4]:

students = [
    ("Alice", 85),
    ("Bob", 75),
    ("Claire", 92),
    ("David", 88),
    ("Eva", 78)
]

students_sorted = sorted(students, key=lambda x: x[1])

for student in students_sorted:
    print(f"{student[0]}: {student[1]}")


# # processing - map, reduce and filter

# In[5]:


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x**2, numbers))

filtered_numbers = list(filter(lambda x: x > 10, squared_numbers))

product = reduce(lambda x, y: x * y, filtered_numbers)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Filtered numbers (greater than 10):", filtered_numbers)
print("Product of filtered numbers:", product)


# # local and global variables

# In[6]:

global_var = 10

def example_function():
   
    local_var = 20
    print(f"Inside the function: global_var = {global_var}, local_var = {local_var}")

    global global_var
    global_var = 30
    print(f"After modifying global_var inside the function: global_var = {global_var}")

example_function()

print(f"Outside the function: global_var = {global_var}")

try:
    print(f"Trying to access local_var outside the function: local_var = {local_var}")
except NameError as e:
    print("Error:", e)


# # parameters

# In[ ]:


def example_function(positional1, positional2, keyword1="default1", keyword2="default2", *args, **kwargs):
    
    print(f"Positional1: {positional1}")
    print(f"Positional2: {positional2}")
    
    print(f"Keyword1: {keyword1}")
    print(f"Keyword2: {keyword2}")
    
    if args:
        print("Additional positional arguments (args):")
        for i, arg in enumerate(args, start=1):
            print(f"  arg{i}: {arg}")
    else:
        print("No additional positional arguments (args).")
    
    if kwargs:
        print("Additional keyword arguments (kwargs):")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    else:
        print("No additional keyword arguments (kwargs).")
    
    print("\nFunction execution completed.\n")


# # logging system - passing function as arguments

# In[3]:


import datetime

def log_to_console(message):
    print(f"{datetime.datetime.now()} - CONSOLE: {message}")

def log_to_file(message, filename="log.txt"):
    with open(filename, "a") as file:
        file.write(f"{datetime.datetime.now()} - FILE: {message}\n")

# Define the logging handler function
def log_message(message, log_function, *args, **kwargs):
    log_function(message, *args, **kwargs)

log_message("This is a console log message.", log_to_console)

log_message("This is a file log message.", log_to_file, filename="my_log.txt")


# # sorting - lambda function

# In[4]:

students = [
    ("Alice", 85),
    ("Bob", 75),
    ("Claire", 92),
    ("David", 88),
    ("Eva", 78)
]

students_sorted = sorted(students, key=lambda x: x[1])

for student in students_sorted:
    print(f"{student[0]}: {student[1]}")


# # processing - map, reduce and filter

# In[5]:


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x**2, numbers))

filtered_numbers = list(filter(lambda x: x > 10, squared_numbers))

product = reduce(lambda x, y: x * y, filtered_numbers)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Filtered numbers (greater than 10):", filtered_numbers)
print("Product of filtered numbers:", product)


# # local and global variables

# In[6]:

global_var = 10

def example_function():
   
    local_var = 20
    print(f"Inside the function: global_var = {global_var}, local_var = {local_var}")

    global global_var
    global_var = 30
    print(f"After modifying global_var inside the function: global_var = {global_var}")

example_function()

print(f"Outside the function: global_var = {global_var}")

try:
    print(f"Trying to access local_var outside the function: local_var = {local_var}")
except NameError as e:
    print("Error:", e)



# # student statistics calculator with integrated functions

# In[ ]:


from functools import reduce
import datetime

global_var = 10

students = ["Alice", "Bob", "Claire", "David", "Eva"]
scores = [85, 75, 92, 88, 78]

def calculate_average(scores):
   
    if not scores:
        return 0
    
    total_sum = sum(scores)
    average = total_sum / len(scores)
    return average

def find_highest_score(scores):
   
    if not scores:
        return 0
    
    highest_score = max(scores)
    return highest_score

def find_passing_students(students, scores, threshold=60):
   
    if not students or not scores:
        return []
    
    passing_students = [students[i] for i in range(len(scores)) if scores[i] >= threshold]
    return passing_students

def log_to_console(message):
   
    print(f"{datetime.datetime.now()} - CONSOLE: {message}")

def log_to_file(message, filename="log.txt"):
   
    with open(filename, "a") as file:
        file.write(f"{datetime.datetime.now()} - FILE: {message}\n")

def log_message(message, log_function, *args, **kwargs):
    
    log_function(message, *args, **kwargs)

def main():
   
    average_score = calculate_average(scores)
    highest_score = find_highest_score(scores)
    passing_students = find_passing_students(students, scores)
    
    print("Student Scores and Statistics:")
    print("-----------------------------")
    for i, student in enumerate(students):
        print(f"{student}: {scores[i]}")
    
    print("\nStatistics:")
    print(f"Average Score: {average_score}")
    print(f"Highest Score: {highest_score}")
    print(f"Passing Students: {passing_students}")
    
    log_message("Logging to console.", log_to_console)
    log_message("Logging to file.", log_to_file, filename="my_log.txt")

if __name__ == "__main__":
    main()



# # String manipulation

# In[3]:


def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    reversed_text = ' '.join(reversed_words)
    return reversed_text

example_text = "Hello world this is a test"
reversed_text = reverse_words(example_text)
print(f"Original text: {example_text}")
print(f"Reversed words: {reversed_text}")


# # List statistics

# In[4]:


def analyze_list(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    average_value = sum(numbers) / len(numbers)
    
    stats = {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }
    
    return stats

numbers = [10, 20, 30, 40, 50]
stats = analyze_list(numbers)
print(f"List statistics: {stats}")


# # Filtering with lambda

# In[5]:


def filter_short_names(names, max_length):
    filtered_names = filter(lambda name: len(name) < max_length, names)
    filtered_names_list = list(filtered_names)
    return filtered_names_list

product_names = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]

short_names = filter_short_names(product_names, 6)
print("Product names shorter than 6 characters:", short_names)


# # Text analyzer

# In[6]:


def analyze_text(text):
    words = text.split()
    word_count = len(words)
    
    char_count = len(text.replace(" ", ""))
    
    word_freq = {}
    for word in words:
        word = word.lower()  
        word_freq[word] = word_freq.get(word, 0) + 1
    
    most_frequent_word = max(word_freq, key=word_freq.get)
    
    analysis_results = {
        "word_count": word_count,
        "char_count": char_count,
        "most_frequent_word": most_frequent_word
    }
    
    return analysis_results

text = "This is a test text. This text contains some words. Words are repeated in this text."
analysis = analyze_text(text)
print("Analysis results:")
print("Word count:", analysis["word_count"])
print("Character count (excluding whitespaces):", analysis["char_count"])
print("Most frequent word:", analysis["most_frequent_word"])

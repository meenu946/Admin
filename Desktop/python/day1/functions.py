
# # Area calculator

# In[ ]:


import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        return "Unknown shape"

rect_area = calculate_area("rectangle", (5, 3))  
circle_area = calculate_area("circle", (4,))    

print(f"Rectangle area: {rect_area}")
print(f"Circle area: {circle_area}")


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





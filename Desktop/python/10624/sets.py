
# # Creating and Manipulating Sets
# In[ ]:

student_ids = {101, 102, 103, 104, 105}

print("Set of Student IDs:")
print(student_ids)

student_ids.add(106)
student_ids.add(107)

print("\nUpdated Set of Student IDs after Adding Elements:")
print(student_ids)

student_ids.remove(102)

print("\nUpdated Set of Student IDs after Removing Element 102:")
print(student_ids)

if 101 in student_ids:
    print("\n101 is present in the set of student IDs.")

other_student_ids = {105, 108, 109}

union_ids = student_ids.union(other_student_ids)
print("\nUnion of Student IDs Sets:")
print(union_ids)

intersection_ids = student_ids.intersection(other_student_ids)
print("\nIntersection of Student IDs Sets:")
print(intersection_ids)

difference_ids = student_ids.difference(other_student_ids)
print("\nDifference of Student IDs Sets:")
print(difference_ids)

# # Set Operations on Course Enrollments

# In[3]:

math_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
physics_students = {"Bob", "Eve", "Grace", "Frank", "David"}
chemistry_students = {"David", "Eve", "Mallory", "Nancy", "Oliver"}

print("Math Students:", math_students)
print("Physics Students:", physics_students)
print("Chemistry Students:", chemistry_students)

all_students = math_students.union(physics_students, chemistry_students)
print("\nAll Students (Union of Sets):", all_students)

common_students = math_students.intersection(physics_students, chemistry_students)
print("\nCommon Students (Intersection of Sets):", common_students)

math_only_students = math_students.difference(physics_students, chemistry_students)
print("\nMath Only Students (Difference of Sets):", math_only_students)

unique_students = math_students.symmetric_difference(physics_students).symmetric_difference(chemistry_students)
print("\nUnique Students (Symmetric Difference of Sets):", unique_students)
 

# # Set Methods for Managing Employee Roles

# In[4]:

current_roles = {"Manager", "Developer", "Designer", "Tester"}

print("Initial Set of Roles:", current_roles)

current_roles.add("Administrator")
print("\nUpdated Set of Roles after Adding 'Administrator':", current_roles)

current_roles.remove("Tester")
print("\nUpdated Set of Roles after Removing 'Tester':", current_roles)

current_roles.discard("Designer")
print("\nUpdated Set of Roles after Discarding 'Designer':", current_roles)

removed_role = current_roles.pop()
print("\nRemoved Role using pop():", removed_role)
print("Updated Set of Roles after pop():", current_roles)

current_roles.clear()
print("\nCleared Set of Roles:", current_roles)

new_roles = {"Manager", "Developer", "Tester"}
copied_roles = new_roles.copy()
print("\nCopied Set of Roles:", copied_roles)

new_roles.update(["Designer", "Support"])
print("\nUpdated Set of Roles after update():", new_roles)

team_roles = {"Developer", "Designer"}
print("\nTeam Roles:", team_roles)
print("Is team_roles subset of new_roles?", team_roles.issubset(new_roles))

print("\nIs new_roles superset of team_roles?", new_roles.issuperset(team_roles))

other_roles = {"HR", "Finance"}
print("\nOther Roles:", other_roles)
print("Are team_roles and other_roles disjoint?", team_roles.isdisjoint(other_roles))

# #  Using in Keyword with Sets
# In[5]:

programming_languages = {"Python", "Java", "C++", "JavaScript", "Ruby"}

print("Set of Programming Languages:", programming_languages)

language = "Python"
if language in programming_languages:
    print(f"\nYes, '{language}' is in the set of programming languages.")

language = "Go"
if language not in programming_languages:
    print(f"\nNo, '{language}' is not in the set of programming languages.")

print("\nIterating through the set of programming languages:")
for lang in programming_languages:
    print(lang)

short_names = {"C", "Java", "Go"}
long_names = {lang for lang in programming_languages if len(lang) > 4}

print("\nShort Names Set:", short_names)
print("Long Names Set:", long_names)

# # Set Comprehension for Filtering Unique Elements

# In[6]:

numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 7, 2]

unique_numbers = {num for num in numbers}

print("Original List of Numbers:", numbers)
print("Set of Unique Numbers:", unique_numbers)

even_numbers = {num for num in numbers if num % 2 == 0}
odd_numbers = {num for num in numbers if num % 2 != 0}

print("\nSet of Even Numbers:", even_numbers)
print("Set of Odd Numbers:", odd_numbers)

squared_numbers = {num ** 2 for num in numbers}

print("\nSet of Squared Numbers:", squared_numbers)




# #   Advanced Set Operations
# In[5]:
from itertools import product, combinations

colors = {"Red", "Green", "Blue"}

shapes = {"Circle", "Square"}

cartesian_product = set(product(colors, shapes))

print("Cartesian Product of Colors and Shapes:")
for pair in cartesian_product:
    print(pair)

elements = {1, 2, 3}

def power_set(s):
    power_set = []
    for r in range(len(s) + 1):
        power_set.extend(combinations(s, r))
    return [set(subset) for subset in power_set]

powerset = power_set(elements)

print("\nPower Set of Elements:", powerset)

frozen_set = frozenset({1, 2, 3})

print("\nFrozen Set:", frozen_set)
print("Frozen Set Hash:", hash(frozen_set)) 

# # Advanced Set Algebra with SymPy

# In[6]:
from sympy import symbols, Union, Intersection, Complement

x, y, z = symbols('x y z')
A = symbols('A', cls=set)
B = symbols('B', cls=set)
C = symbols('C', cls=set)

A = {x, y}
B = {y, z}
C = {x, z}

union_AB = Union(A, B)
intersection_BC = Intersection(B, C)
complement_A = Complement({x, y, z}, A)

print("Set A:", A)
print("Set B:", B)
print("Set C:", C)
print("\nUnion of A and B:", union_AB)
print("Intersection of B and C:", intersection_BC)
print("Complement of A:", complement_A)

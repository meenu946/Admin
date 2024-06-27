
# # install numpy

# In[ ]:

import numpy as np
print(np.__version__)

# # numpy arrays

# In[ ]:

import numpy as np

grades = np.array([
    [85, 90, 88, 92],
    [78, 83, 85, 80],
    [90, 92, 91, 95],
    [70, 75, 72, 68],
    [88, 89, 85, 90]
])

print("Grades Array:")
print(grades)

print("\nShape of the array:", grades.shape)

print("Size of the array:", grades.size)

print("Data type of the array:", grades.dtype)

average_grades_per_student = np.mean(grades, axis=1)
print("\nAverage grade per student:", average_grades_per_student)

average_grades_per_subject = np.mean(grades, axis=0)
print("Average grade per subject:", average_grades_per_subject)

overall_average_grade = np.mean(grades)
print("Overall average grade:", overall_average_grade)

highest_grades_per_subject = np.max(grades, axis=0)
print("Highest grade per subject:", highest_grades_per_subject)

lowest_grades_per_subject = np.min(grades, axis=0)
print("Lowest grade per subject:", lowest_grades_per_subject)

new_student_grades = np.array([[82, 88, 90, 85]])
grades = np.vstack([grades, new_student_grades])

print("\nUpdated Grades Array with New Student:")
print(grades)

# # Business Operations Data Analysis with NumPy

# In[3]:

import numpy as np

sales_data = np.array([
    [100, 120, 110, 130, 125],
    [150, 160, 155, 165, 170],
    [200, 210, 205, 215, 220],
    [250, 260, 255, 265, 270]
])

print("Sales Data Array:")
print(sales_data)

inventory_data = np.asarray([
    [500, 480, 460, 440, 420],
    [400, 380, 360, 340, 320],
    [300, 280, 260, 240, 220],
    [200, 180, 160, 140, 120]
])

print("\nInventory Data Array:")
print(inventory_data)

increase_rate = np.ones((4, 5)) * 0.1

print("\nIncrease Rate Array:")
print(increase_rate)

expenses_data = np.zeros((4, 5))

print("\nExpenses Data Array:")
print(expenses_data)

forecast_data = np.empty((4, 5))

print("\nForecast Data Array (Uninitialized Values):")
print(forecast_data)

days_of_month = np.arange(1, 31)

print("\nDays of Month Array:")
print(days_of_month)

temperature_readings = np.linspace(20, 35, 8)

print("\nTemperature Readings Throughout the Day:")
print(temperature_readings)

identity_matrix = np.eye(4)

print("\nIdentity Matrix:")
print(identity_matrix)

total_sales_per_product = np.sum(sales_data, axis=1)
print("\nTotal Sales Per Product:")
print(total_sales_per_product)

average_inventory_per_product = np.mean(inventory_data, axis=1)
print("\nAverage Inventory Per Product:")
print(average_inventory_per_product)

forecast_sales = sales_data * (1 + increase_rate)
print("\nForecast Sales with Increase Rate:")
print(forecast_sales)

expenses_data = np.array([
    [50, 55, 53, 58, 57],
    [60, 63, 61, 66, 65],
    [70, 73, 71, 76, 75],
    [80, 83, 81, 86, 85]
])
print("\nUpdated Expenses Data Array:")
print(expenses_data)

net_profit = sales_data - expenses_data
print("\nNet Profit:")
print(net_profit)


# # Financial Analysis with NumPy array operations

# In[4]:
import numpy as np

revenue = np.array([12000, 15000, 18000, 20000, 21000, 25000, 23000, 24000, 26000, 27000, 30000, 32000])
expenses = np.array([8000, 9000, 10000, 12000, 11000, 13000, 14000, 15000, 16000, 18000, 20000, 22000])

print("Revenue Array:")
print(revenue)

print("\nExpenses Array:")
print(expenses)

profit = revenue - expenses
print("\nProfit Array:")
print(profit)

profit_margin = (profit / revenue) * 100
print("\nProfit Margin Array (%):")
print(profit_margin)

sqrt_revenue = np.sqrt(revenue)
print("\nSquare Root of Revenue:")
print(sqrt_revenue)

exp_revenue = np.exp(revenue / 10000)  
print("\nExponential of Revenue:")
print(exp_revenue)

bonus = np.array([500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600])
revenue_with_bonus = revenue + bonus
print("\nRevenue with Bonus:")
print(revenue_with_bonus)

tax = np.array([1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2200, 2400])
profit_after_tax = profit - tax
print("\nProfit after Tax:")
print(profit_after_tax)

growth_factor = 1.1
projected_revenue = revenue * growth_factor
print("\nProjected Revenue with Growth Factor:")
print(projected_revenue)

cost_reduction_factor = 0.9
reduced_expenses = expenses / cost_reduction_factor
print("\nReduced Expenses with Cost Reduction Factor:")
print(reduced_expenses)

employees = np.array([10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17])
revenue_per_employee = revenue / employees
print("\nRevenue per Employee:")
print(revenue_per_employee)

# # Weather Data Analysis with NumPy Broadcasting

# In[5]:

import numpy as np

temperatures = np.array([
    [22, 24, 19, 21, 25, 23, 20], 
    [28, 27, 29, 30, 31, 32, 28],  
    [18, 20, 17, 19, 21, 18, 16], 
    [25, 26, 24, 23, 27, 26, 25],  
    [30, 31, 29, 28, 32, 31, 30]   
])

print("Temperature Data (Celsius):")
print(temperatures)

temperatures_fahrenheit = temperatures * 9/10 + 32
print("\nTemperature Data (Fahrenheit):")
print(temperatures_fahrenheit)

average_temperatures = np.mean(temperatures, axis=1)
print("\nAverage Temperature for Each City (Celsius):")
print(average_temperatures)

temperature_deviation = temperatures - average_temperatures[:, np.newaxis]
print("\nTemperature Deviation from Average for Each City:")
print(temperature_deviation)

heatwave_adjusted_temperatures = temperatures + 2
print("\nHeatwave Adjusted Temperatures (Celsius):")
print(heatwave_adjusted_temperatures)

min_temperatures = np.min(temperatures, axis=1)
max_temperatures = np.max(temperatures, axis=1)
normalized_temperatures = (temperatures - min_temperatures[:, np.newaxis]) / (max_temperatures[:, np.newaxis] - min_temperatures[:, np.newaxis])
print("\nNormalized Temperatures:")
print(normalized_temperatures)

hot_days = temperatures > 25
print("\nDays with Temperatures Above 25 Degrees (Boolean Indexing):")
print(hot_days)

print("\nTemperatures on Hot Days:")
print(temperatures[hot_days])

increase_needed = 30 - temperatures
print("\nTemperature Increase Needed to Reach 30 Degrees:")
print(increase_needed)

adjusted_temperatures = temperatures.copy()
adjusted_temperatures[adjusted_temperatures < 20] += 5
print("\nAdjusted Temperatures (Celsius) - Increase Temperatures Below 20 Degrees by 5:")
print(adjusted_temperatures)


# # Financial Data Analysis with NumPy Element-Wise Operations

# In[6]:
import numpy as np
import time

np.random.seed(0)
stock_prices = np.random.rand(365, 5) * 100 

print("Stock Prices Data (First 5 Days):")
print(stock_prices[:5])

daily_returns = (stock_prices[1:] - stock_prices[:-1]) / stock_prices[:-1] * 100
print("\nDaily Returns (First 5 Days):")
print(daily_returns[:5])

average_prices = np.mean(stock_prices, axis=0)
print("\nAverage Stock Prices:")
print(average_prices)

max_prices = np.max(stock_prices, axis=0)
print("\nMaximum Stock Prices:")
print(max_prices)

min_prices = np.min(stock_prices, axis=0)
print("\nMinimum Stock Prices:")
print(min_prices)

normalized_prices = (stock_prices - min_prices) / (max_prices - min_prices)
print("\nNormalized Stock Prices (First 5 Days):")
print(normalized_prices[:5])

large_data = np.random.rand(1000000)

start_time = time.time()
numpy_result = large_data * 2 + 3
numpy_time = time.time() - start_time

start_time = time.time()
python_result = [x * 2 + 3 for x in large_data]
python_time = time.time() - start_time

print(f"\nNumPy operation time: {numpy_time:.6f} seconds")
print(f"Native Python operation time: {python_time:.6f} seconds")

annual_return = np.prod(daily_returns / 100 + 1, axis=0) - 1
print("\nAnnual Return for Each Company:")
print(annual_return)

window_size = 5
moving_averages = np.convolve(stock_prices[:, 0], np.ones(window_size) / window_size, mode='valid')
print("\nMoving Average of Stock Prices for the First Company (First 10 Days):")
print(moving_averages[:10])


# #  Analyzing Weather Data with NumPy Indexing

# In[ ]:

import numpy as np

np.random.seed(0)
temperature_data = np.random.rand(365, 5) * 40 - 10 

print("Temperature Data (First 5 Days):")
print(temperature_data[:5])

first_week_temperatures = temperature_data[:7]
print("\nFirst Week Temperatures:")
print(first_week_temperatures)

first_station_temperatures = temperature_data[:, 0]
print("\nFirst Station Temperatures (First 10 Days):")
print(first_station_temperatures[:10])

specific_days = [0, 49, 99, 149, 199, 249, 299, 349]
specific_days_temperatures = temperature_data[specific_days]
print("\nTemperatures on Specific Days:")
print(specific_days_temperatures)

selected_stations_temperatures = temperature_data[:, [0, 2]]
print("\nTemperatures for Selected Stations (First 5 Days):")
print(selected_stations_temperatures[:5])

hot_days = temperature_data > 25
hot_temperatures = temperature_data[hot_days]
print("\nTemperatures Above 25 Degrees Celsius:")
print(hot_temperatures)

cold_days_first_station = temperature_data[:, 0] < 0
cold_temperatures_first_station = temperature_data[cold_days_first_station, 0]
print("\nTemperatures Below 0 Degrees Celsius for the First Station:")
print(cold_temperatures_first_station)

average_temperatures = np.mean(temperature_data, axis=0)
print("\nAverage Temperatures for Each Weather Station:")
print(average_temperatures)

hottest_temperatures = np.max(temperature_data, axis=0)
print("\nHottest Temperatures for Each Weather Station:")
print(hottest_temperatures)

coldest_days = np.argmin(temperature_data, axis=0)
print("\nDay with the Lowest Temperature for Each Weather Station:")
print(coldest_days)

freezing_days = np.sum(temperature_data < 0, axis=0)
print("\nNumber of Freezing Days for Each Weather Station:")
print(freezing_days)


# # Working with Sales Data using NumPy Slicing

# In[3]:

import numpy as np

np.random.seed(0)
sales_data = np.random.randint(100, 500, (12, 3))

print("Sales Data (All 12 Months):")
print(sales_data)

first_product_sales = sales_data[:, 0]
print("\nFirst Product Sales (All 12 Months):")
print(first_product_sales)

first_product_first_half_sales = sales_data[:6, 0]
print("\nFirst Product Sales (First 6 Months):")
print(first_product_first_half_sales)

first_half_sales = sales_data[:6, :]
print("\nSales Data (First 6 Months for All Products):")
print(first_half_sales)

first_two_products_sales = sales_data[:, :2]
print("\nSales Data (All Months for First Two Products):")
print(first_two_products_sales)

first_product_alternate_months_sales = sales_data[::2, 0]
print("\nFirst Product Sales (Every Other Month):")
print(first_product_alternate_months_sales)

first_product_second_half_reverse_sales = sales_data[11:5:-1, 0]
print("\nFirst Product Sales (Second Half of the Year in Reverse):")
print(first_product_second_half_reverse_sales)

sales_data[:6, :] = sales_data[:6, :] * 1.10
print("\nSales Data After 10% Increase for First 6 Months:")
print(sales_data)

sales_data[-1, :] = 0
print("\nSales Data After Setting Last Month Sales to Zero:")
print(sales_data)

first_half_alternate_months_first_two_products_sales = sales_data[:6:2, :2]
print("\nSales Data (First Two Products for Every Other Month in the First Half of the Year):")
print(first_half_alternate_months_first_two_products_sales)

# # Customer Purchase Data Manipulation using NumPy

# In[4]:
import numpy as np

np.random.seed(0)
purchase_data = np.random.randint(1, 100, (4, 12, 3))

print("Original Purchase Data (4 customers, 12 months, 3 products):")
print(purchase_data)

reshaped_data = purchase_data.reshape(12, 4, 3)
print("\nReshaped Purchase Data (12 months, 4 customers, 3 products):")
print(reshaped_data)

reshaped_data_2d = purchase_data.reshape(4, -1)
print("\nReshaped Purchase Data to 2D Array (4 customers, all months concatenated):")
print(reshaped_data_2d)

flattened_data = purchase_data.flatten()
print("\nFlattened Purchase Data (1D array):")
print(flattened_data)

flattened_along_axis0 = np.concatenate(purchase_data, axis=0).flatten()
print("\nFlattened Purchase Data along axis 0 (combining customers' data sequentially):")
print(flattened_along_axis0)

Q1_data = purchase_data[:, :3, :]
Q2_data = purchase_data[:, 3:6, :]
concatenated_data_Q1_Q2 = np.concatenate((Q1_data, Q2_data), axis=1)
print("\nConcatenated Q1 and Q2 Data (6 months data for each customer):")
print(concatenated_data_Q1_Q2)

concatenated_data_products = np.concatenate(purchase_data, axis=2)
print("\nConcatenated Data for All Products (4 customers, 12 months):")
print(concatenated_data_products)

reshaped_combined_data = concatenated_data_products.reshape(4, -1)
print("\nReshaped Combined Data for All Products to 2D Array:")
print(reshaped_combined_data)


# # Manipulating NumPy Arrays - Adding and Removing Elements

# In[5]:

import numpy as np

sales_data = np.array([35000, 42000, 38000, 41000, 39000, 40000, 37000, 39000, 40000, 41000, 43000, 42000])

print("Original Sales Data:")
print(sales_data)

new_sales_data = np.append(sales_data, 44000)
print("\nAppended Sales Data with New Month:")
print(new_sales_data)

index = 6
inserted_sales_data = np.insert(new_sales_data, index, 36000)
print("\nInserted Sales Data for a New Month:")
print(inserted_sales_data)

deleted_sales_data = np.delete(inserted_sales_data, 3)
print("\nDeleted Sales Data for a Specific Month (April):")
print(deleted_sales_data)

resized_sales_data = np.resize(deleted_sales_data, 10)
print("\nResized Sales Data to Include Only First 10 Months:")
print(resized_sales_data)



# # Given a 3D array a with shape (2, 3, 4) and a 2D array b with shape (3, 4), perform element-wise multiplication between a and b using broadcasting.

# In[6]:
import numpy as np

a = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])

b = np.array([
    [2, 3, 4, 5],
    [6, 7, 8, 9],
    [10, 11, 12, 13]
])

result = a * b

print("Result of element-wise multiplication:")
print(result)


# # Implement a function that takes two 2D arrays c and d with different shapes and performs element-wise operations (addition, subtraction, multiplication, and division) between them using broadcasting. Handle the case where broadcasting is not possible.

# In[ ]:

import numpy as np

def elementwise_operations(c, d, operation='+'):
    
    try:
        result = eval(f"c {operation} d")
    except ValueError:
        print(f"Error: Broadcasting is not possible between arrays with shapes {c.shape} and {d.shape}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    return result

c = np.array([[1, 2], [3, 4], [5, 6]]) 
d = np.array([[10, 20, 30], [40, 50, 60]])  

result_add = elementwise_operations(c, d, '+')
if result_add is not None:
    print("Element-wise Addition Result:")
    print(result_add)

result_mult = elementwise_operations(c, d, '*')
if result_mult is not None:
    print("\nElement-wise Multiplication Result:")
    print(result_mult)

result_sub = elementwise_operations(c, d, '-')
if result_sub is not None:
    print("\nElement-wise Subtraction Result:")
    print(result_sub)

result_div = elementwise_operations(c, d, '/')
if result_div is not None:
    print("\nElement-wise Division Result:")
    print(result_div)


# # Create a 2D array e with shape (5, 3) and a 1D array f with length 5. Compute the outer product of e and f using broadcasting.

# In[3]:

import numpy as np

e = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])

f = np.array([2, 3, 4, 5, 6])

outer_product = e[:, :, np.newaxis] * f[np.newaxis, np.newaxis, :]

print("Outer Product:")
print(outer_product)


# # Given a 3D array g with shape (4, 3, 2), extract every other element along the first and second dimensions, but keep all elements along the third dimension.

# In[4]:

import numpy as np

g = np.array([
    [[1, 2],
     [3, 4],
     [5, 6]],

    [[7, 8],
     [9, 10],
     [11, 12]],

    [[13, 14],
     [15, 16],
     [17, 18]],

    [[19, 20],
     [21, 22],
     [23, 24]]
])

result = g[::2, ::2, :]

print("Resulting array:")
print(result)


# # Create a function that takes a 2D array h and an array of row indices i and column indices j. The function should return a new array k where k[m, n] is the sum of the elements in h along the diagonal specified by i[m] and j[n].

# In[5]:

import numpy as np

def diagonal_sum(h, i, j):
    
    assert len(i) == len(j), "Length of i and j must be the same"

    m = len(i)
    n = len(j)

    k = np.zeros((m, n), dtype=h.dtype)

    for idx in range(m):
        row_idx = i[idx]
        col_idx = j[idx]
        k[idx, :] = np.diag(h, k=col_idx - row_idx).sum(axis=0)

    return k

h = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

i = np.array([0, 1, 2, 3])
j = np.array([0, 1, 2, 3])

result = diagonal_sum(h, i, j)

print("Resulting array 'k':")
print(result)


# # Implement a function that takes a 2D array l and returns a new array m where each element in m is the product of the corresponding row and column means in l.

# In[6]:

import numpy as np

def row_column_means_product(l):
    
    row_means = np.mean(l, axis=1, keepdims=True) 

    column_means = np.mean(l, axis=0, keepdims=True)  

    m = np.outer(row_means.flatten(), column_means.flatten())

    return m

l = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = row_column_means_product(l)

print("Resulting array 'm':")
print(result)

# # Given a 2D array n with shape (4, 6), reshape it into a 3D array with shape (2, 2, 6) and then flatten it back to a 2D array with shape (4, 6).

# In[3]:

import numpy as np

n = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
])

reshaped_n = np.reshape(n, (2, 2, 6))

flattened_n = reshaped_n.flatten()

print("Original 2D array 'n':")
print(n)

print("\nReshaped 3D array 'reshaped_n' (shape: {}):".format(reshaped_n.shape))
print(reshaped_n)

print("\nFlattened 2D array 'flattened_n' (shape: {}):".format(flattened_n.shape))
print(flattened_n)


# # Implement a function that takes a 2D array o and rolls it along the first axis by a specified number of positions. For example, if the input array is [[1, 2, 3], [4, 5, 6]] and the number of positions is 1, the output should be [[4, 5, 6], [1, 2, 3]].

# In[4]:
import numpy as np

def roll_2d_array(o, positions):
   
    rolled_array = np.roll(o, positions, axis=0)

    return rolled_array

o = np.array([[1, 2, 3], [4, 5, 6]])

positions = 1
rolled_result = roll_2d_array(o, positions)

print("Original array 'o':")
print(o)

print("\nRolled array by {} positions:".format(positions))
print(rolled_result)


# # Create a function that takes a 2D array p and replaces all occurrences of a specified value x with the mean of the neighboring elements (horizontally and vertically) in the array.

# In[5]:

import numpy as np

def replace_with_neighbor_mean(p, x):

    indices = np.where(p == x)

    for r, c in zip(indices[0], indices[1]):
        neighbors = []
        if r > 0:
            neighbors.append(p[r-1, c]) 
        if r < p.shape[0] - 1:
            neighbors.append(p[r+1, c]) 
        if c > 0:
            neighbors.append(p[r, c-1]) 
        if c < p.shape[1] - 1:
            neighbors.append(p[r, c+1])  

        if neighbors:
            mean_value = np.mean(neighbors)
            p[r, c] = mean_value 

    return p

p = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 2, 9]
])

x = 2

updated_array = replace_with_neighbor_mean(p, x)

print("Original array 'p':")
print(p)

print("\nUpdated array with replaced values:")
print(updated_array)

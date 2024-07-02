
# # pandas

# In[ ]:
import pandas as pd
import numpy as np

salaries_list = [45000, 54000, 58000, 72000, 90000]
salaries_series_list = pd.Series(salaries_list, name="Salaries")
print("Series from list:")
print(salaries_series_list)

salaries_array = np.array([46000, 55000, 59000, 73000, 91000])
salaries_series_array = pd.Series(salaries_array, name="Salaries")
print("\nSeries from array:")
print(salaries_series_array)

salaries_dict = {
    "John": 47000,
    "Jane": 56000,
    "Mike": 60000,
    "Sara": 74000,
    "Tom": 92000
}
salaries_series_dict = pd.Series(salaries_dict, name="Salaries")
print("\nSeries from dictionary:")
print(salaries_series_dict)

mean_salary_list = salaries_series_list.mean()
mean_salary_array = salaries_series_array.mean()
mean_salary_dict = salaries_series_dict.mean()

print(f"\nMean Salary (list): {mean_salary_list}")
print(f"Mean Salary (array): {mean_salary_array}")
print(f"Mean Salary (dict): {mean_salary_dict}")

john_salary = salaries_series_dict["John"]
print(f"\nJohn's Salary: {john_salary}")

has_null_list = salaries_series_list.isnull().any()
has_null_array = salaries_series_array.isnull().any()
has_null_dict = salaries_series_dict.isnull().any()

print(f"\nHas null (list): {has_null_list}")
print(f"Has null (array): {has_null_array}")
print(f"Has null (dict): {has_null_dict}")

salaries_series_dict["Mike"] = 65000
print("\nUpdated Series (dict):")
print(salaries_series_dict)

salaries_series_dict["Anna"] = 80000
print("\nSeries after adding a new employee (dict):")
print(salaries_series_dict)


# # common attributes

# In[ ]:
import pandas as pd

data = {
    'Name': ['John', 'Jane', 'Mike', 'Sara', 'Tom'],
    'Salary': [47000, 56000, 60000, 74000, 92000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'IT']
}

df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)

index = df.index
print("\nIndex of the DataFrame:")
print(index)

values = df.values
print("\nValues of the DataFrame:")
print(values)

dtypes = df.dtypes
print("\nData types of each column:")
print(dtypes)

size = df.size
print("\nTotal number of elements in the DataFrame:")
print(size)

mean_salary = df['Salary'].mean()
print(f"\nMean Salary: {mean_salary}")

has_null = df.isnull().any().any()
print(f"\nHas null values: {has_null}")

new_employee = pd.DataFrame({'Name': ['Anna'], 'Salary': [80000], 'Department': ['Finance']})
df = df.append(new_employee, ignore_index=True)
print("\nDataFrame after adding a new employee:")
print(df)


# # common methods

# In[3]:
import pandas as pd

data = {
    'OrderID': [101, 102, 103, 104, 105, 106],
    'Product': ['Laptop', 'Tablet', 'Laptop', 'Desktop', 'Tablet', 'Desktop'],
    'Quantity': [1, 2, 1, 3, 2, 1],
    'Price': [1200, 650, 1200, 800, 650, 800],
    'SalesPerson': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Charlie']
}

df = pd.DataFrame(data)
print("Sales DataFrame:")
print(df)

print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

print("\nLast 3 rows of the DataFrame:")
print(df.tail(3))

print("\nDataFrame sorted by Price in descending order:")
print(df.sort_values(by='Price', ascending=False))

print("\nMean of the Price column:")
print(df['Price'].mean())

print("\nMedian of the Price column:")
print(df['Price'].median())

print("\nStandard deviation of the Price column:")
print(df['Price'].std())

# 7. Str Method
print("\nSalesPerson names in uppercase:")
print(df['SalesPerson'].str.upper())

def total_sale(row):
    return row['Quantity'] * row['Price']

df['TotalSale'] = df.apply(total_sale, axis=1)
print("\nDataFrame with TotalSale column:")
print(df)


# # dataframe

# In[4]:
import pandas as pd

data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005, 1006],
    'CustomerName': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', 'Jessica Davis', 'Daniel Wilson'],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Tablet'],
    'Quantity': [1, 2, 1, 3, 2, 1],
    'Price': [1200, 800, 600, 1200, 800, 600],
    'OrderDate': ['2024-01-01', '2024-01-03', '2024-01-05', '2024-01-07', '2024-01-09', '2024-01-11']
}

df = pd.DataFrame(data)
print("Customer Orders DataFrame:")
print(df)

print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

print("\nLast 3 rows of the DataFrame:")
print(df.tail(3))

print("\nDescriptive statistics of the DataFrame:")
print(df.describe())

print("\nDataFrame sorted by Price in descending order:")
print(df.sort_values(by='Price', ascending=False))

print("\nOrders with Quantity greater than 1:")
print(df[df['Quantity'] > 1])

df['TotalPrice'] = df['Quantity'] * df['Price']
print("\nDataFrame with TotalPrice column:")
print(df)

print("\nTotal sales by Product:")
print(df.groupby('Product')['TotalPrice'].sum())

data_with_nan = {
    'OrderID': [1007],
    'CustomerName': ['Laura Martinez'],
    'Product': ['Laptop'],
    'Quantity': [2],
    'Price': [None],
    'OrderDate': ['2024-01-13']
}
df_nan = pd.DataFrame(data_with_nan)
df = pd.concat([df, df_nan], ignore_index=True)
print("\nDataFrame with a row having missing data:")
print(df)

df['Price'].fillna(df['Price'].mean(), inplace=True)
print("\nDataFrame after filling missing Price values with mean:")
print(df)

df.to_csv('customer_orders.csv', index=False)
print("\nDataFrame saved to 'customer_orders.csv'.")

df_loaded = pd.read_csv('customer_orders.csv')
print("\nDataFrame loaded from 'customer_orders.csv':")
print(df_loaded)

# # dataframe from dictionaries and csv file

# In[5]:
import pandas as pd

sales_data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Laptop', 'Smartwatch'],
    'Quantity': [2, 1, 3, 1, 2],
    'Price': [1200, 500, 800, 1200, 200],
    'OrderDate': ['2024-05-01', '2024-05-03', '2024-05-05', '2024-05-07', '2024-05-09']
}

df_dict = pd.DataFrame(sales_data)
print("DataFrame created from dictionary:")
print(df_dict)

df_dict.to_csv('sales_data.csv', index=False)
print("\nDataFrame saved to 'sales_data.csv'.")

df_csv = pd.read_csv('sales_data.csv')
print("\nDataFrame loaded from 'sales_data.csv':")
print(df_csv)

print("\nFirst 3 rows of the DataFrame:")
print(df_csv.head(3))

print("\nLast 3 rows of the DataFrame:")
print(df_csv.tail(3))

print("\nDescriptive statistics of the DataFrame:")
print(df_csv.describe())

print("\nDataFrame sorted by Price in descending order:")
print(df_csv.sort_values(by='Price', ascending=False))

print("\nOrders with Quantity greater than 1:")
print(df_csv[df_csv['Quantity'] > 1])

df_csv['TotalPrice'] = df_csv['Quantity'] * df_csv['Price']
print("\nDataFrame with TotalPrice column:")
print(df_csv)

print("\nTotal sales by Product:")
print(df_csv.groupby('Product')['TotalPrice'].sum())

data_with_nan = {
    'OrderID': [1006],
    'CustomerName': ['Frank'],
    'Product': ['Laptop'],
    'Quantity': [2],
    'Price': [None],
    'OrderDate': ['2024-05-11']
}
df_nan = pd.DataFrame(data_with_nan)
df_csv = pd.concat([df_csv, df_nan], ignore_index=True)
print("\nDataFrame with a row having missing data:")
print(df_csv)

df_csv['Price'].fillna(df_csv['Price'].mean(), inplace=True)
print("\nDataFrame after filling missing Price values with mean:")
print(df_csv)

# # data inspection

# In[6]:

import pandas as pd

employee_data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', 'Finance'],
    'Salary': [60000, 65000, 70000, 75000, 72000, 68000],
    'JoiningDate': ['2020-01-15', '2019-11-23', '2018-03-01', '2017-07-12', '2021-05-23', '2020-06-19'],
    'Age': [25, 28, 30, 35, 24, 27]
}

df = pd.DataFrame(employee_data)
print("Employee DataFrame:")
print(df)

print("\nInformation about the DataFrame:")
df.info()

print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

print("\nDescriptive statistics of the DataFrame:")
print(df.describe())

print("\nChecking for missing values in the DataFrame:")
print(df.isnull())

print("\nSum of missing values for each column:")
print(df.isnull().sum())

print("\nColumn names in the DataFrame:")
print(df.columns)

print("\nData types of each column:")
print(df.dtypes)


# #  data exploration

# In[ ]:
import pandas as pd

sales_data = {
    'ProductID': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
    'ProductName': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'North', 'South'],
    'Sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
    'Profit': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
}

df = pd.DataFrame(sales_data)
print("Sales DataFrame:")
print(df)

print("\nCount of each ProductID:")
print(df['ProductID'].value_counts())

print("\nCount of each Region:")
print(df['Region'].value_counts())

print("\nUnique Product Names:")
print(df['ProductName'].unique())

print("\nUnique Regions:")
print(df['Region'].unique())

print("\nCorrelation matrix:")
print(df.corr())


# # indexing and slicing 

# In[3]:
import pandas as pd

sales_data = {
    'ProductID': [1, 2, 3, 4, 5],
    'ProductName': ['A', 'B', 'C', 'D', 'E'],
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Sales': [100, 150, 200, 250, 300],
    'Profit': [20, 30, 40, 50, 60]
}

df = pd.DataFrame(sales_data)
print("Sales DataFrame:")
print(df)

print("\nUsing loc to select specific rows and columns:")
print(df.loc[[0, 1], ['ProductName', 'Sales']])

print("\nUsing loc to select all rows where Region is 'North':")
print(df.loc[df['Region'] == 'North'])

print("\nUsing iloc to select specific rows and columns:")
print(df.iloc[[0, 1], [1, 3]])

print("\nUsing iloc to select a range of rows and columns:")
print(df.iloc[1:4, 1:4])

print("\nUsing boolean indexing to select rows where Sales is greater than 200:")
print(df[df['Sales'] > 200])

print("\nUsing boolean indexing to select rows where ProductName is 'A' or 'E':")
print(df[(df['ProductName'] == 'A') | (df['ProductName'] == 'E')])

# # data manipulation 

# In[4]:

import pandas as pd

sales_data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01'],
    'Region': ['North', 'South', 'North', 'South', 'North'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 150, 200, 180, 120],
    'Profit': [20, 30, 40, 35, 25]
}

df = pd.DataFrame(sales_data)
print("Original DataFrame:")
print(df)

pivot_df = df.pivot_table(index='Date', columns='Region', values='Sales', aggfunc='sum')
print("\nPivot Table - Sum of Sales by Date and Region:")
print(pivot_df)

melted_df = pd.melt(df, id_vars=['Date', 'Region'], value_vars=['Sales', 'Profit'], var_name='Metric', value_name='Value')
print("\nMelted DataFrame:")
print(melted_df)

stacked_df = df.set_index(['Date', 'Region', 'Product']).stack().reset_index()
stacked_df.columns = ['Date', 'Region', 'Product', 'Metric', 'Value']
print("\nStacked DataFrame:")
print(stacked_df)

unstacked_df = stacked_df.set_index(['Date', 'Region', 'Product', 'Metric']).unstack('Metric').reset_index()
print("\nUnstacked DataFrame:")
print(unstacked_df)


# # data transformation

# In[5]:
import pandas as pd
import numpy as np

np.random.seed(0)
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
regions = np.random.choice(['North', 'South', 'East', 'West'], 100)
products = np.random.choice(['A', 'B', 'C'], 100)
sales = np.random.randint(100, 1000, 100)
profits = np.random.randint(10, 100, 100)

sales_data = {
    'Date': dates,
    'Region': regions,
    'Product': products,
    'Sales': sales,
    'Profit': profits
}

df = pd.DataFrame(sales_data)
print("Original DataFrame:")
print(df.head())

grouped_df = df.groupby(['Region', 'Product']).agg({
    'Sales': 'sum',
    'Profit': 'mean'
}).reset_index()

print("\nGrouped DataFrame - Total Sales and Average Profit by Region and Product:")
print(grouped_df.head())

monthly_df = df.set_index('Date').resample('M').agg({
    'Sales': 'sum',
    'Profit': 'sum'
}).reset_index()

print("\nMonthly Resampled DataFrame - Total Sales and Profit per Month:")
print(monthly_df.head())

def calculate_sales_ratio(group):
    total_sales = group['Sales'].sum()
    group['SalesRatio'] = group['Sales'] / total_sales
    return group

sales_ratio_df = df.groupby(['Region', 'Product']).apply(calculate_sales_ratio)
print("\nDataFrame with Sales Ratio per Product per Region:")
print(sales_ratio_df.head())

df_no_duplicates = df.drop_duplicates(subset=['Date', 'Region'])

df_no_duplicates = df_no_duplicates.rename(columns={'Sales': 'TotalSales', 'Profit': 'AverageProfit'})

print("\nDataFrame after Dropping Duplicates and Renaming Columns:")
print(df_no_duplicates.head())

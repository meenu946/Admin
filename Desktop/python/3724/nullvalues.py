
# # Handling Null Values in Numerical and Categorical Columns 

# In[ ]:


import pandas as pd
import numpy as np

data = {
    'Age': [25, 30, np.nan, 45, 22, np.nan, 35],
    'Salary': [50000, 54000, 58000, np.nan, 60000, 62000, np.nan],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', np.nan, 'Finance'],
    'Gender': ['Male', 'Female', np.nan, 'Male', 'Female', 'Male', np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(0, inplace=True)

df['Department'].fillna(df['Department'].mode()[0], inplace=True)
df['Gender'].fillna('Unknown', inplace=True)

print("\nDataFrame after handling null values:")
print(df)

df_cleaned = df.dropna()
print("\nDataFrame after dropping rows with null values:")
print(df_cleaned)

df_cleaned_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with null values:")
print(df_cleaned_cols)



# # Identifying Null Values in a Real-World Dataset

# In[ ]:

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, np.nan, 45, 22, np.nan, 35],
    'Salary': [50000, 54000, 58000, np.nan, 60000, 62000, np.nan],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', np.nan, 'Finance'],
    'Gender': ['Female', 'Male', np.nan, 'Male', 'Female', 'Male', np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

null_values = df.isnull()
print("\nNull values identified using 'isnull()':")
print(null_values)

null_values_sum = df.isnull().sum()
print("\nSum of null values per column:")
print(null_values_sum)

print("\nDataFrame information using 'info()':")
df.info()

null_values_percentage = (df.isnull().sum() / len(df)) * 100
print("\nPercentage of null values per column:")
print(null_values_percentage)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Heatmap of Null Values in the DataFrame")
plt.show()

rows_with_nulls = df[df.isnull().any(axis=1)]
print("\nRows with any null values:")
print(rows_with_nulls)

rows_all_nulls = df[df.isnull().all(axis=1)]
print("\nRows with all null values:")
print(rows_all_nulls)

rows_no_nulls = df.dropna()
print("\nRows with no null values:")
print(rows_no_nulls)


# # Handling Missing Data by Removing Observations and Variables

# In[3]:

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, np.nan, 45, 22, np.nan, 35],
    'Salary': [50000, 54000, 58000, np.nan, 60000, 62000, np.nan],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', np.nan, 'Finance'],
    'Gender': ['Female', 'Male', np.nan, 'Male', 'Female', 'Male', np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_removed_observations = df.dropna()
print("\nDataFrame after removing observations with any missing values:")
print(df_removed_observations)

df_removed_variables = df.dropna(axis=1)
print("\nDataFrame after removing variables with any missing values:")
print(df_removed_variables)

correlation_matrix = df.corr(method='pearson', min_periods=1)
print("\nCorrelation matrix with pairwise deletion:")
print(correlation_matrix)

df_removed_all_missing_rows = df.dropna(how='all')
print("\nDataFrame after removing rows with all missing values:")
print(df_removed_all_missing_rows)

df_removed_all_missing_columns = df.dropna(axis=1, how='all')
print("\nDataFrame after removing columns with all missing values:")
print(df_removed_all_missing_columns)

df_removed_threshold = df.dropna(thresh=3)
print("\nDataFrame after removing rows with less than 3 non-missing values:")
print(df_removed_threshold)

df_removed_columns_threshold = df.dropna(axis=1, thresh=5)
print("\nDataFrame after removing columns with less than 5 non-missing values:")
print(df_removed_columns_threshold)


# # Handling Missing Data with Various Imputation Techniques

# In[4]:


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, np.nan, 45, 22, np.nan, 35],
    'Salary': [50000, 54000, 58000, np.nan, 60000, 62000, np.nan],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', np.nan, 'Finance'],
    'Gender': ['Female', 'Male', np.nan, 'Male', 'Female', 'Male', np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

mean_imputer = SimpleImputer(strategy='mean')
df['Age_Mean_Impute'] = mean_imputer.fit_transform(df[['Age']])

median_imputer = SimpleImputer(strategy='median')
df['Age_Median_Impute'] = median_imputer.fit_transform(df[['Age']])

mode_imputer = SimpleImputer(strategy='most_frequent')
df['Gender_Mode_Impute'] = mode_imputer.fit_transform(df[['Gender']])

constant_imputer = SimpleImputer(strategy='constant', fill_value=-999)
df['Salary_Constant_Impute'] = constant_imputer.fit_transform(df[['Salary']])
df['Salary_Missing_Indicator'] = df['Salary'].isnull().astype(int)

percentile_imputer = SimpleImputer(strategy='constant', fill_value=df['Age'].quantile(0.01))
df['Age_Lower_Tail_Impute'] = percentile_imputer.fit_transform(df[['Age']])

percentile_imputer = SimpleImputer(strategy='constant', fill_value=df['Age'].quantile(0.99))
df['Age_Upper_Tail_Impute'] = percentile_imputer.fit_transform(df[['Age']])

print("\nDataFrame after various imputations:")
print(df)



# # Handling Missing Data with KNN and MICE Imputation

# In[5]:

import pandas as pd
import numpy as np
from fancyimpute import KNN
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

data = {
    'Age': [25, 30, np.nan, 45, 22, np.nan, 35],
    'Salary': [50000, 54000, 58000, np.nan, 60000, 62000, np.nan],
    'YearsExperience': [2, 3, 4, np.nan, 5, 6, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

knn_imputer = KNN(k=3)
df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)

print("\nDataFrame after KNN imputation:")
print(df_knn_imputed)

mice_imputer = IterativeImputer(max_iter=10, random_state=0)
df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(df), columns=df.columns)

print("\nDataFrame after MICE imputation:")
print(df_mice_imputed)


# # Handling Missing Data with fillna

# In[6]:


import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [24, np.nan, 22, np.nan, 29],
    'Salary': [50000, 54000, np.nan, 58000, 62000],
    'City': ['New York', 'Los Angeles', 'New York', np.nan, 'Los Angeles']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_constant_filled = df.fillna(value={'Age': 25, 'Salary': 55000, 'City': 'Unknown'})

print("\nDataFrame after filling missing values with a constant value:")
print(df_constant_filled)

df_ffill = df.fillna(method='ffill')

print("\nDataFrame after forward fill:")
print(df_ffill)

df_bfill = df.fillna(method='bfill')

print("\nDataFrame after backward fill:")
print(df_bfill)

df_mean_filled = df.copy()
df_mean_filled['Age'] = df['Age'].fillna(df['Age'].mean())
df_mean_filled['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\nDataFrame after filling missing values with mean:")
print(df_mean_filled)

def fill_city_mode(series):
    mode = series.mode()[0]
    return series.fillna(mode)

df_custom_filled = df.copy()
df_custom_filled['City'] = fill_city_mode(df['City'])

print("\nDataFrame after filling missing values with mode:")
print(df_custom_filled)

df_conditional_filled = df.copy()
df_conditional_filled['Age'] = df['Age'].fillna(df['Age'].median())
df_conditional_filled['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\nDataFrame after filling missing values conditionally:")
print(df_conditional_filled)



# #  Handling Missing Data with dropna

# In[ ]:

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Fiona', 'George'],
    'Age': [24, np.nan, 22, 25, 29, np.nan, 34],
    'Salary': [50000, 54000, np.nan, 58000, 62000, 60000, np.nan],
    'City': ['New York', 'Los Angeles', 'New York', np.nan, 'Los Angeles', 'Boston', 'San Francisco']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_dropna_any = df.dropna()

print("\nDataFrame after dropping rows with any missing values:")
print(df_dropna_any)

df_with_all_nan = df.append({'Name': np.nan, 'Age': np.nan, 'Salary': np.nan, 'City': np.nan}, ignore_index=True)
df_dropna_all = df_with_all_nan.dropna(how='all')

print("\nDataFrame after dropping rows with all missing values:")
print(df_dropna_all)

df_dropna_columns = df.dropna(axis=1)

print("\nDataFrame after dropping columns with any missing values:")
print(df_dropna_columns)

df_dropna_specific = df.dropna(subset=['Age'])

print("\nDataFrame after dropping rows with missing values in 'Age' column:")
print(df_dropna_specific)

df_dropna_threshold = df.dropna(thresh=3)

print("\nDataFrame after dropping rows with less than 3 non-NaN values:")
print(df_dropna_threshold)

df.dropna(inplace=True)

print("\nDataFrame after dropping rows with any missing values (inplace):")
print(df)


# #  Handling Missing Data with Interpolation

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=15, freq='D'),
    'Temperature': [30, 32, np.nan, 35, 36, np.nan, np.nan, 38, 37, 35, np.nan, 33, 32, 31, np.nan]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

print("Original DataFrame:")
print(df)

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', label='Original Data')
plt.title('Temperature Data with Missing Values')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.show()

df_linear = df.interpolate(method='linear')

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', label='Original Data')
plt.plot(df_linear.index, df_linear['Temperature'], marker='x', linestyle='--', label='Linear Interpolation')
plt.title('Linear Interpolation')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.show()

df_polynomial = df.interpolate(method='polynomial', order=2)

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', label='Original Data')
plt.plot(df_polynomial.index, df_polynomial['Temperature'], marker='x', linestyle='--', label='Polynomial Interpolation')
plt.title('Polynomial Interpolation')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.show()

df_spline = df.interpolate(method='spline', order=3)

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', label='Original Data')
plt.plot(df_spline.index, df_spline['Temperature'], marker='x', linestyle='--', label='Spline Interpolation')
plt.title('Spline Interpolation')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.show()

df_nearest = df.interpolate(method='nearest')

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', label='Original Data')
plt.plot(df_nearest.index, df_nearest['Temperature'], marker='x', linestyle='--', label='Nearest Neighbor Interpolation')
plt.title('Nearest Neighbor Interpolation')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.show()

print("\nDataFrame after Linear Interpolation:")
print(df_linear)
print("\nDataFrame after Polynomial Interpolation:")
print(df_polynomial)
print("\nDataFrame after Spline Interpolation:")
print(df_spline)
print("\nDataFrame after Nearest Neighbor Interpolation:")
print(df_nearest)



# #  Handling Missing Data by Replacing Values

# In[ ]:

import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2023-01-01', periods=15, freq='D'),
    'Temperature': [30, 32, np.nan, 35, 36, np.nan, np.nan, 38, 37, 35, np.nan, 33, 32, 31, np.nan],
    'Humidity': [45, 50, 48, np.nan, 55, 53, np.nan, 50, 49, np.nan, 46, 44, np.nan, 43, 42]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

print("Original DataFrame:")
print(df)

df_replace_0 = df.fillna(0)

df_replace_mean = df.fillna(df.mean())

df_replace_median = df.fillna(df.median())

df_replace_mode = df.apply(lambda x: x.fillna(x.mode()[0]))

df_ffill = df.fillna(method='ffill')

df_bfill = df.fillna(method='bfill')

print("\nDataFrame after replacing missing values with 0:")
print(df_replace_0)

print("\nDataFrame after replacing missing values with mean:")
print(df_replace_mean)

print("\nDataFrame after replacing missing values with median:")
print(df_replace_median)

print("\nDataFrame after replacing missing values with mode:")
print(df_replace_mode)

print("\nDataFrame after forward filling missing values:")
print(df_ffill)

print("\nDataFrame after backward filling missing values:")
print(df_bfill)

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 10))

plt.subplot(3, 2, 1)
plt.plot(df.index, df['Temperature'], marker='o', label='Original Temperature')
plt.plot(df.index, df['Humidity'], marker='x', label='Original Humidity')
plt.title('Original Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(df_replace_0.index, df_replace_0['Temperature'], marker='o', label='Replaced with 0')
plt.plot(df_replace_0.index, df_replace_0['Humidity'], marker='x', label='Replaced with 0')
plt.title('Replaced with 0')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(df_replace_mean.index, df_replace_mean['Temperature'], marker='o', label='Replaced with Mean')
plt.plot(df_replace_mean.index, df_replace_mean['Humidity'], marker='x', label='Replaced with Mean')
plt.title('Replaced with Mean')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(df_replace_median.index, df_replace_median['Temperature'], marker='o', label='Replaced with Median')
plt.plot(df_replace_median.index, df_replace_median['Humidity'], marker='x', label='Replaced with Median')
plt.title('Replaced with Median')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.subplot(3, 2, 5)
plt.plot(df_ffill.index, df_ffill['Temperature'], marker='o', label='Forward Fill')
plt.plot(df_ffill.index, df_ffill['Humidity'], marker='x', label='Forward Fill')
plt.title('Forward Fill')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.subplot(3, 2, 6)
plt.plot(df_bfill.index, df_bfill['Temperature'], marker='o', label='Backward Fill')
plt.plot(df_bfill.index, df_bfill['Humidity'], marker='x', label='Backward Fill')
plt.title('Backward Fill')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()



# #   Handling Missing Data Using Quartiles

# In[ ]:

import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2023-01-01', periods=15, freq='D'),
    'Temperature': [30, 32, np.nan, 35, 36, np.nan, np.nan, 38, 37, 35, np.nan, 33, 32, 31, np.nan],
    'Humidity': [45, 50, 48, np.nan, 55, 53, np.nan, 50, 49, np.nan, 46, 44, np.nan, 43, 42]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

print("Original DataFrame:")
print(df)

def impute_with_quartiles(df):
    df_imputed = df.copy()
    for column in df_imputed.columns:
        Q1 = df_imputed[column].quantile(0.25)
        Q2 = df_imputed[column].quantile(0.50)
        Q3 = df_imputed[column].quantile(0.75)
        
        df_imputed[column] = df_imputed[column].fillna(Q2) 
        df_imputed[column] = df_imputed[column].fillna(Q1)  
        df_imputed[column] = df_imputed[column].fillna(Q3)  
    
    return df_imputed

df_quartiles = impute_with_quartiles(df)

print("\nDataFrame after imputing missing values with quartiles:")
print(df_quartiles)

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 10))

plt.subplot(2, 1, 1)
plt.plot(df.index, df['Temperature'], marker='o', label='Original Temperature')
plt.plot(df.index, df['Humidity'], marker='x', label='Original Humidity')
plt.title('Original Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df_quartiles.index, df_quartiles['Temperature'], marker='o', label='Imputed Temperature')
plt.plot(df_quartiles.index, df_quartiles['Humidity'], marker='x', label='Imputed Humidity')
plt.title('Imputed Data (Using Quartiles)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()



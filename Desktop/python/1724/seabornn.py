
# # lineplot

# In[ ]:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

months = range(1, 13)
sales = [15000, 18000, 21000, 22000, 20000, 25000, 28000, 30000, 32000, 35000, 38000, 40000]

sales_data = pd.DataFrame({
    'Month': months,
    'Sales': sales
})

plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sales', data=sales_data, marker='o', color='b', linewidth=2, linestyle='-', label='Monthly Sales')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()


# # histogram

# In[ ]:

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(0)
data1 = np.random.normal(loc=0, scale=1, size=1000)
data2 = np.random.normal(loc=2, scale=1.5, size=1000)

plt.figure(figsize=(10, 6))
sns.histplot(data1, kde=True, color='blue', label='Data 1', stat='density')
sns.histplot(data2, kde=True, color='orange', label='Data 2', stat='density')
plt.title('Histogram with KDE')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()


# # barplot

# In[3]:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

regions = ['North', 'South', 'East', 'West']
sales = [45000, 30000, 35000, 40000]

sales_data = pd.DataFrame({
    'Region': regions,
    'Sales': sales
})

plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=sales_data, palette='viridis')

ax = plt.gca()
for bar in ax.containers:
    ax.bar_label(bar, fmt='%.0f', label_type='edge') 
    ax.bar_label(bar, fmt='%.0f')  

plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


# # heatmap

# In[4]:

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(0)
data = np.random.rand(10, 5)  
columns = ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5']
df = pd.DataFrame(data, columns=columns)

corr_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# # scatter plot

# In[5]:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(0)
size = 100
x = np.random.normal(size=size)
y = 2 * x + np.random.normal(size=size)
z = np.random.choice(['A', 'B', 'C'], size=size)
df = pd.DataFrame({'X': x, 'Y': y, 'Category': z})

plt.figure(figsize=(10, 6))
sns.scatterplot(x='X', y='Y', hue='Category', data=df, s=100, alpha=0.7, marker='o', edgecolor='k')

plt.title('Scatter Plot with Formatting')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(title='Category')
plt.grid(True)
plt.show()


# # kde plot

# In[6]:

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(10, 6))
sns.kdeplot(data, shade=True, color='b', alpha=0.7)

plt.title('KDE Plot')
plt.xlabel('Values')
plt.ylabel('Density')
plt.grid(True)
plt.show()


# #  rug plot

# In[ ]:

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=100)

plt.figure(figsize=(10, 6))
sns.rugplot(data, height=0.5, color='g', alpha=0.6)

plt.title('Rug Plot')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# # box plot

# In[3]:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(0)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value': np.random.normal(loc=0, scale=1, size=100)
})

plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Value', data=data, palette='Set2')

plt.title('Box Plot of Value by Category')
plt.xlabel('Category')
plt.ylabel('Value')

plt.grid(True)
plt.show()

# # violin plot

# In[4]:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(0)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value': np.random.normal(loc=0, scale=1, size=100)
})

plt.figure(figsize=(10, 6))
sns.violinplot(x='Category', y='Value', data=data, palette='Set2', inner='quartile')

plt.title('Violin Plot of Value by Category')
plt.xlabel('Category')
plt.ylabel('Value')

plt.grid(True)
plt.show()


# # pair plot

# In[5]:
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
data = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

data['Category'] = np.random.choice(['X', 'Y'], size=100)

sns.pairplot(data, hue='Category', palette='Set2', markers=['o', 's'])

plt.suptitle('Pair Plot of Numerical Variables with Categorical Hue')

plt.show()


# # pie chart 

# In[ ]:


import matplotlib.pyplot as plt

labels = ['Apples', 'Oranges', 'Bananas', 'Grapes']
sizes = [25, 30, 20, 25]  
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0) 

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')

plt.axis('equal')

plt.title('Fruit distribution')

plt.show()


# # line chart

# In[ ]:

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100) 
y1 = np.sin(x)
y2 = np.cos(x) 

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Sin(x)', color='blue', linestyle='-', linewidth=2, marker='o', markersize=5)
plt.plot(x, y2, label='Cos(x)', color='green', linestyle='--', linewidth=2, marker='s', markersize=5)

median_y1 = np.median(y1)
median_y2 = np.median(y2)
plt.axhline(y=median_y1, color='blue', linestyle='-', label=f'Median Sin(x)={median_y1:.2f}')
plt.axhline(y=median_y2, color='green', linestyle='--', label=f'Median Cos(x)={median_y2:.2f}')

plt.title('Sine and Cosine Functions')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()

plt.grid(True)

plt.show()


# # bar chart

# In[3]:

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5) 
y1 = np.array([3, 7, 2, 5, 8]) 
y2 = np.array([5, 6, 4, 9, 3]) 

fig, ax1 = plt.subplots(figsize=(10, 6))

bars = ax1.bar(x, y1, color='b', alpha=0.6, label='Bar Chart')

ax2 = ax1.twinx()
line, = ax2.plot(x, y2, color='r', marker='o', linestyle='-', linewidth=2, markersize=8, label='Line Chart')

ax1.set_xlabel('Categories')
ax1.set_ylabel('Bar Chart Data', color='b')
ax2.set_ylabel('Line Chart Data', color='r')
ax1.set_title('Bar Chart and Line Chart')

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

lines = [line]
ax1.legend(handles=[bar, line], loc='upper left')

plt.show()


# # scatter plot

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.randn(100)
y = 2.0 * x + np.random.randn(100)

sizes = np.abs(x) * 100
colors = np.abs(y)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolors='k')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Sizes and Colors')

plt.colorbar(label='Sizes')

plt.grid(True)

plt.show()


# # histogram

# In[5]:

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data1 = np.random.normal(0, 1, 1000) 
data2 = np.random.normal(2, 1.5, 1000) 

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(data1, bins=30, edgecolor='black')
axes[0, 0].set_title('Histogram of Data1 (Normal Distribution)')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].hist(data2, bins=30, color='green', alpha=0.6, edgecolor='black')
axes[0, 1].set_title('Histogram of Data2 (Normal Distribution)')
axes[0, 1].set_xlabel('Value')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(data1, bins=30, alpha=0.5, label='Data1', edgecolor='black')
axes[1, 0].hist(data2, bins=30, alpha=0.5, label='Data2', color='green', edgecolor='black')
axes[1, 0].set_title('Overlay Histograms of Data1 and Data2')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].legend()

axes[1, 1].hist(data1, bins=30, orientation='horizontal', edgecolor='black')
axes[1, 1].hist(data2, bins=30, orientation='horizontal', color='green', alpha=0.6, edgecolor='black')
axes[1, 1].set_title('Horizontal Histograms of Data1 and Data2')
axes[1, 1].set_xlabel('Frequency')
axes[1, 1].set_ylabel('Value')

plt.tight_layout()

plt.show()


# # area plot

# In[6]:


import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
sales = np.array([10, 15, 18, 22, 25, 30, 35, 40, 38, 36])
expenses = np.array([8, 10, 12, 15, 18, 20, 25, 28, 30, 32])

plt.figure(figsize=(10, 6))

plt.fill_between(years, sales, color='skyblue', alpha=0.4, label='Sales')

plt.fill_between(years, expenses, color='salmon', alpha=0.4, label='Expenses')

plt.title('Sales and Expenses Over Years')
plt.xlabel('Years')
plt.ylabel('Amount ($)')
plt.xticks(years)  
plt.grid(True)  
plt.legend()

plt.tight_layout()
plt.show()


# #  box plot

# In[ ]:

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.normal(0, 1, 100)

np.random.seed(20)
data1 = np.random.normal(0, 1, 100)
np.random.seed(30)
data2 = np.random.normal(1, 2, 100)
np.random.seed(40)
data3 = np.random.normal(2, 3, 100)

data_multiple = [data1, data2, data3]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].boxplot(data)
axs[0].set_title('Simple Boxplot')

axs[1].boxplot(data_multiple, patch_artist=True, notch=True, vert=True, widths=0.7, meanline=True,
               showmeans=True, showcaps=True, showbox=True, showfliers=True,
               boxprops={'facecolor': 'lightblue'},
               whiskerprops={'linewidth': 2, 'color': 'purple'},
               capprops={'linewidth': 2, 'color': 'green'},
               medianprops={'linewidth': 2, 'color': 'orange'},
               flierprops={'marker': 'o', 'markersize': 8, 'markerfacecolor': 'red', 'markeredgecolor': 'red'},
               meanprops={'marker': 'D', 'markersize': 8, 'markerfacecolor': 'blue', 'markeredgecolor': 'blue'})
axs[1].set_title('Formatted Boxplot')

axs[2].boxplot(data_multiple, patch_artist=True, notch=False, vert=True, widths=0.7, meanline=True,
               showmeans=True, showcaps=True, showbox=True, showfliers=True,
               boxprops={'facecolor': 'lightgreen'},
               whiskerprops={'linewidth': 2, 'color': 'brown'},
               capprops={'linewidth': 2, 'color': 'blue'},
               medianprops={'linewidth': 2, 'color': 'purple'},
               flierprops={'marker': 'o', 'markersize': 8, 'markerfacecolor': 'red', 'markeredgecolor': 'red'},
               meanprops={'marker': 'D', 'markersize': 8, 'markerfacecolor': 'blue', 'markeredgecolor': 'blue'})
axs[2].set_title('Multiple Dataset Boxplot')

plt.tight_layout()

plt.show()


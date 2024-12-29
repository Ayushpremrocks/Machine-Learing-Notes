# -*- coding: utf-8 -*-
"""seaborn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nk-m5ncuZZeQcTYs2_rnNIpEfRHTJXoT

setup
"""

pip install seaborn

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

# Auto reloads notebook when changes are made
# %reload_ext autoreload
# %autoreload 2

"""import data"""

#we can import data or can use in built datasets in seaborn
x = sns.load_dataset("titanic")
x

"""joint plot"""

#Jointplot compares 2 distributions and plots a scatter plot by default
# As we can see as people tend to speed they also tend to drink & drive
# With kind you can create a regression line with kind='reg'
# You can create a 2D KDE with kind='kde'
# Kernal Density Estimation estimates the distribution of data
# You can create a hexagon distribution with kind='hex'
sns.jointplot(x="age", y="fare", data=x)

sns.jointplot(x="age", y="fare", data=x, kind='reg')

sns.jointplot(x="age", y="fare", data=x, kind='kde')

# Plots a single column of datapoints in an array as sticks on an axis
# With a rug plot you'll see a more dense number of lines where the amount is most common. This is like how a histogram is taller where values are more common
sns.jointplot(x="age", y="fare", data=x, kind ='hex')

"""KDE plot"""

#to get KDE plot
sns.kdeplot(x['age'])

"""pair plot"""

# Pair Plot plots relationships across the entire data frames numerical values
sns.pairplot(x)

"""rug plot"""

# Plots a single column of datapoints in an array as sticks on an axis
# With a rug plot you'll see a more dense number of lines where the amount is most common. This is like how a histogram is taller where values are more common
sns.rugplot(x['age'])

"""styling"""

# You can set styling for your axes and grids
sns.set_style('darkgrid')
sns.jointplot(x='age', y='fare', data=x,kind='reg')
plt.figure(figsize=(12,4))
sns.set_context('paper',font_scale = 1.1)
sns.despine(left=False, bottom=False)

"""categorical plots

bar plots
"""

# Focus on distributions using categorical data in reference to one of the numerical columns
# Aggregate categorical data based on a function (mean is the default)
# With estimator you can define functions to use other than the mean like those
# provided by NumPy : median, std, var, cov or make your own functions
sns.barplot(x='sex', y='survived', data=x)

"""count plot"""

# A count plot is like a bar plot, but the estimator is counting the number of occurances
sns.countplot(x='sex',data=x)

"""box plot"""

# A box plot allows you to compare different variables
# The box shows the quartiles of the data. The bar in the middle is the median and the box extends 1 standard deviation from the median
# The whiskers extend to all the other data aside from the points that are considered to be outliers
# Hue can add another category being sex
sns.boxplot(x='sex', y='age', data=x, hue='survived')

"""violin plot"""

# Violin Plot is a combination of the boxplot and KDE
# While a box plot corresponds to data points, the violin plot uses the KDE estimation
# of the data points
# Split allows you to compare how the categories compare to each other
sns.violinplot(x='sex', y='age', data=x, hue='survived',split=True)

"""strip plot"""

# The strip plot draws a scatter plot representing all data points where one
# variable is categorical. It is often used to show all observations with
# a box plot that represents the average distribution
# Jitter spreads data points out so that they aren't stacked on top of each other
# Hue breaks data into men and women
# Dodge separates the men and women data
sns.stripplot(x='sex', y='age', data=x, hue='survived',jitter=True)

sns.stripplot(x='sex', y='age', data=x, hue='survived',jitter=True,dodge=True)

"""swarm plot"""

# A swarm plot is like a strip plot, but points are adjusted so they don't overlap
# It looks like a combination of the violin and strip plots
sns.swarmplot(x='sex', y='age', data=x, hue='survived',dodge=True)

#You can stack a violin plot with a swarm
sns.violinplot(x='sex', y='age', data=x, hue='survived',split=True)
sns.swarmplot(x='sex', y='age', data=x, hue='survived',dodge=True,color='red')

"""palettes"""

# You can use Matplotlibs color maps for color styling
# https://matplotlib.org/3.3.1/tutorials/colors/colormaps.html
sns.stripplot(x='sex', y='age', data=x, hue='survived',palette='winter')
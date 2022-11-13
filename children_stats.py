from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_main = pd.read_csv('insurance.csv')

max_age = df_main['age'].max()  # max age
min_age = df_main['age'].min()  # min age

tuples = [(min_age - 1, 25), (25, 40), (40, 55), (55, max_age)]  # created list with intervals
bins = pd.IntervalIndex.from_tuples(tuples)  # added list to intervals

df_main['Interval'] = pd.cut(df_main['age'], bins=bins, include_lowest=True, precision=0)  # created new column of index

df = df_main.groupby('Interval')['children'].agg(
    ['count', 'mean', 'min', 'max'])  # found amount, average, min, max of amount of children

df.columns = ['Amount of children', 'Average amount of children', 'Min amount of children',
              'Max amount of children']  # changed names of columns
print(tabulate(df, headers='keys', tablefmt='psql'))

print()
print()
print()

df_groupby_region_and_counted_children = df_main.groupby(['region'])['children'].count()  # grouped by region and counted amount of children
df22 = pd.DataFrame(df_groupby_region_and_counted_children)
df22.columns = ['Sum of children']  # changed column name
df_max_children = df22.max().iloc[0]  # assigned max amount of children to variable
df_max_children_region = df22.loc[df22['Sum of children'] == df_max_children].iloc[[0]]  # get row of max amount of children
df_max_children_region_value = df_max_children_region.index[0]  # assigned name of region where is max amount of children

print()
print()
print(f'Most of the children {df_max_children} in the region "{df_max_children_region_value}"')
print()
print(tabulate(df22, headers='keys', tablefmt='psql'))

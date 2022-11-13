from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_main = pd.read_csv('insurance.csv')

df1 = df_main.groupby(['region'])['bmi'].mean()  # found average of bmi by regions
df2 = df_main.groupby(['age'])['bmi'].mean()  # found average of bmi by age
df3 = df_main.groupby(['sex'])['bmi'].mean()  # found average of bmi by gender

print()
print()

print('|Average(mean) of BMI grouped by region|')
print(df1.to_markdown())

print()
print()

print('|Average(mean) of BMI grouped by gender|')
print(df3.to_markdown())

df2.plot.bar(rot=0)
plt.xlabel('Ages')
plt.ylabel('Average(mean) of BMI')
plt.title('Average(mean) of BMI grouped by age')
plt.show()

from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_main = pd.read_csv('insurance.csv')
temp = df_main.groupby('region').age.mean()  # grouped by region

df1 = df_main.groupby(['region', 'sex'])['bmi'].max()  # found max of bmi
df2 = df_main.groupby(['region', 'sex'])['bmi'].min()  # found min of bmi
df3 = df_main.groupby(['region', 'sex'])['bmi'].median()  # found median of bmi
df4 = df_main.groupby(['region', 'sex'])['bmi'].std(ddof=0)  # found standard deviation of bmi

frames = [df1, df2, df3, df4]  # created list of dataframes

result = pd.concat(frames, axis=1, join='outer')  # added dataframes together
result.columns = ['Max BMI', 'Min BMI', 'Median of BMI', 'STD of BMI']  # changed names of columns

print()
print()
print()
print('+-------|Table of max, min, median, std of BMI grouped by region and gender|-------+')
print(tabulate(result, headers='keys', tablefmt='psql'))

import pandas as pd

df = pd.read_csv('insurance.csv')


maximum = df['charges'].max()
print(f'Maximum charges is {maximum}')

minimum = df['charges'].min()
print(f'Minimum charges is {minimum}')

mean = df['charges'].mean()
print(f'Average charges is {mean}')

median = df['charges'].median()
print(f'Median point of charges is {median}')




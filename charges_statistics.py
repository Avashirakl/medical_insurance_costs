import pandas as pd


df = pd.read_csv('insurance.csv')

by_regions = df.groupby(['region'])

region_stats = by_regions['charges'].agg(['min', 'max', 'mean'])

print('{:^47}'.format('Statistics for every region'))
print('{:_^47}'.format(''))
print(region_stats, "\n")  # Printing statistics by charges of every region
print('{:_^100}'.format(''))

largest_charges_count = df[df['charges'] > 27000].groupby(
    ['region'])['charges'].agg(['count']
                               )  # Count of people with more than 27000 charges by regions

print('Amount of people with more than 27000 charges by regions:', '\n')
print(largest_charges_count, "\n\n")

print('{:_^100}'.format(''))
print(f"Largest region by charges - "
      f"{largest_charges_count['count'].idxmax()}", '\n')  # Printing the largest region # by charges

largest_region = df[df['region'] == 'southeast']
avg_age = largest_region['age'].mean()
avg_bmi = largest_region['bmi'].mean()
smoker_count = largest_region[largest_region['smoker'] == 'yes'].shape[0]
children_count = largest_region['children'].sum()

print(f'Average age - {avg_age}')
print(f'Average bmi - {avg_bmi}')
print(f'Amount of smokers - {smoker_count}')
print(f'Amount of children - {children_count}')

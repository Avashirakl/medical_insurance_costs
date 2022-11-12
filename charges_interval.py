import pandas as pd
import numpy as np

df = pd.read_csv('insurance.csv')

tuples = [(0, 5000), (5000, 10000), (10000, 20000), (20000, 65000)]  # Interval tuples
bins = pd.IntervalIndex.from_tuples(tuples)  # making IntervalIndex from tuples

df['interval'] = pd.cut(df['charges'], bins=bins, include_lowest=True, precision=0)

df = df.groupby('interval')[['charges', 'bmi', 'age']].agg(['mean'])
df['mean_difference'] = [(df['charges']['mean'].iloc[1] - df['charges']['mean'].iloc[0]),
                         (df['charges']['mean'].iloc[2] - df['charges']['mean'].iloc[1]),
                         (df['charges']['mean'].iloc[3] - df['charges']['mean'].iloc[2]), np.nan]
order = [0, 3, 1, 2]
df = df[[df.columns[i] for i in order]]
print(df)


import pandas as pd

df = pd.read_csv('insurance.csv')
#  Task: add new column 'Weight' based on 'bmi' column add

df['weight'] = df.apply(  # .apply() method used to compute some values over an existing column
    lambda row: 'Underweight' if row.bmi < 18.5
    else ('Normal' if 18.5 <= row.bmi < 24.9
          else ('Overweight' if 25 <= row.bmi < 30
                else ('Obese' if 30 <= row.bmi < 35
                      else ('Extremely Obese' if row.bmi >= 35 else '')))), axis=1)

print(df)  # Printing updated DataFrame

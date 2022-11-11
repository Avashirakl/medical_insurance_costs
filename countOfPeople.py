import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/User/Desktop/DataAnalyz/medical_insurance_costs-main/insurance.csv')

gender = df['sex']
children = df['children']

male = []
female = []
mnogodetei = 0
malodetei = 0

for i in range(df.shape[0]):
    if gender.values[i] == 'male':
        male.append('male')
    else:
        female.append('female')
        
    if children.values[i] >= 3:
        mnogodetei += 1
    else:
        malodetei += 1
        
maleLen = len(male)
femLen = len(female)    

plt.subplot(2,1,1)
plt.title('Genders')
plt.bar('Male', maleLen, color = "skyblue", width = 0.4)
plt.bar('Female', femLen, color = "pink", width = 0.4)
plt.xlabel("Gender")
plt.ylabel("Count")

plt.subplot(2,1,2)
plt.title('Family')
plt.bar('Large families', mnogodetei, width = 0.4)
plt.bar('Smal families', malodetei, width = 0.4)

plt.show()

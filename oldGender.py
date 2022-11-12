import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('insurance.csv')

gender = df['sex']
age = df['age']

youngF = 0; youngM = 0
mediumF = 0; mediumM = 0
dediF = 0; dediM = 0

for i in range(df.shape[0]):
    if(age.values[i] >= 10) & (age.values[i] <= 30):
        
        if(gender.values[i] == 'male'):
            youngM += 1
        else:
            youngF += 1
       
    elif(age.values[i] > 60):
        
        if(gender.values[i] == 'male'):
            dediM += 1
        else:
            dediF += 1
            
    else:
        
        if(gender.values[i] == 'male'):
            mediumM += 1
        else:
            mediumF += 1

# Man
plt.bar('Male 10-30', youngM, color = "skyblue", width = 0.5)
plt.bar('Male 30-60', mediumM, color = "blue", width = 0.5)
plt.bar('Male 60+', dediM, color = "darkblue", width = 0.5)
#Women
plt.bar('Female 10-30', youngF, color = "pink", width = 0.5)
plt.bar('Female 30-60', mediumF, color = "red", width = 0.5)
plt.bar('Female 60+', dediF, color = "brown", width = 0.5)
# plt.xlim(0, 0)
plt.xlabel("Gender")
plt.ylabel("Count")


plt.show()

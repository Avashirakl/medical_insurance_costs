import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('insurance.csv')

gender = df['sex']
smok = df['smoker']
region = df['region']

smokM = 0; nosmokM = 0
smokF = 0; nosmokF = 0

# regions 
southeast = 0; northeast = 0; southwest = 0; northwest = 0 
NOsoutheast = 0; NOnortheast = 0; NOsouthwest = 0; NOnorthwest = 0 

for i in range(df.shape[0]):
    if(smok.values[i] == 'yes'):
        
        # COUNT OF REGION
        if(region.values[i] == 'southeast'):
            southeast += 1
        elif(region.values[i] == 'northeast'):
            northeast += 1
        elif(region.values[i] == 'southwest'):
            southwest += 1   
        elif(region.values[i] == 'northwest'):
            northwest += 1
        
        # COUNT OF GENDER
        if(gender.values[i] == 'male'):
            smokM += 1
        else:
            smokF += 1
    
    else:
        
        # COUNT OF REGION
        if(region.values[i] == 'southeast'):
            NOsoutheast += 1
        elif(region.values[i] == 'northeast'):
            NOnortheast += 1
        elif(region.values[i] == 'southwest'):
            NOsouthwest += 1   
        elif(region.values[i] == 'northwest'):
            NOnorthwest += 1
        
        # COUNT OF GENDER
        if(gender.values[i] == 'male'):
            nosmokM += 1
        else:
            nosmokF += 1
            
fig, ax = plt.subplots()

# Man
plt.subplot(2, 1, 2)
plt.title('INFO about Smoking')
plt.bar('Smoking males', smokM, color = "skyblue", width = 0.5)
plt.bar('No smoking males', nosmokM, color = "grey", width = 0.5)

#Women
plt.bar('Smoking females', smokF, color = "pink", width = 0.5)
plt.bar('No smoking females', nosmokF, color = "grey", width = 0.5)

plt.xlabel("Gender")
plt.ylabel("Count")

# REGION SMOKING
plt.subplot(2, 2, 1)
plt.title('Smoking people in the regions')
plt.bar('Southeast', southeast, width = 0.5)
plt.bar('Northeast', northeast, width = 0.5)
plt.bar('Southwest', southwest, width = 0.5)
plt.bar('Northwest', northwest, width = 0.5)

plt.xlabel("Gender")
plt.ylabel("Count")

# REGION NO SMOKING
plt.subplot(2, 2, 2)
plt.title('Non-smokers in the regions')
plt.bar('Southeast', NOsoutheast, width = 0.5)
plt.bar('Northeast', NOnortheast, width = 0.5)
plt.bar('Southwest', NOsouthwest, width = 0.5)
plt.bar('Northwest', NOnorthwest, width = 0.5)

plt.xlabel("Gender")
plt.ylabel("Count")
# plt.subplots_adjust(wspace=0.35)

plt.show()

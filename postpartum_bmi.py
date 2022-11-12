import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')

has_children = df.loc[(df['sex'] == 'female') & df['children'] > 0]['bmi']  # BMI of women who has children
has_children_mean = has_children.mean()  # Average BMI of women with children

no_children = df.loc[(df['sex'] == 'female') & df['children'] == 0]['bmi']  # BMI of childless women
no_children_mean = no_children.mean()  # Average BMI of childless women

print('BMI for women with children - ' + '{:.2f}'.format(has_children_mean))
print('BMI for women without children - ' + '{:.2f}'.format(no_children_mean), '\n')
print('Conclusion: Women without children has more BMI')  # 30.19 < 30.77, so women with children has less BMI

smokes = df.loc[(df['sex'] == 'female') & (df['smoker'] == 'no')]['bmi']  # DataFrame of Non-smoking women
doesnt_smoke = df.loc[(df['sex'] == 'female') & (df['smoker'] == 'yes')]['bmi']  # DataFrame of smoking women

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)  # making space between subplots

plt.subplot(1, 2, 1)  # first subplot
plt.hist(doesnt_smoke, bins=20)  # first histogram with 20 bins
plt.title("Non-smoking women")
plt.xlabel("BMI")
plt.ylabel("Amount")

plt.subplot(1, 2, 2)  # second subplot
plt.title("Smoking women")
plt.xlabel("BMI")
plt.ylabel("Amount")
plt.hist(smokes, color="gray", bins=20)  # second histogram with 20 bins and gray color
plt.show()

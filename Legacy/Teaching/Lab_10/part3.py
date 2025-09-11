import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'age': [24, 25, 40, 27, 60],
    'salary': [400, 540, 2000, 700, 8000]
}

data_df = pd.DataFrame(data)

#korrelációs mátrix
corr = data_df.corr()
print("Correlation matrix:")
print(corr)

#sns.heatmap(corr, annot=True, cmap='coolwarm')
#plt.title('Correlation matrix')
#plt.show()

from sklearn.linear_model import LinearRegression

x = data_df[['age']]
y = data_df['salary']

model = LinearRegression()
model.fit(x, y)
print(f"y = {model.coef_[0]}*x + {model.intercept_}")

# Predict
y_elorejelzes = model.predict([[30]])

plt.scatter(data_df['age'], data_df['salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.plot(data_df['age'], model.predict(x), color='red')
plt.legend()
plt.show()
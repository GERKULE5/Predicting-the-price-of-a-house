import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

repairIndex = {
    'Designed': 5,
    'Euro': 4,
    'Cosmetic': 3
}


data = pd.read_csv('src/dataset.csv')
print(f'Dataset:\n{data}')

x = data.drop(['price'], axis=1)
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=10, random_state=42)

model = LinearRegression()


model.fit(x_train, y_train)

preds = model.predict(x_test)

print(f'Predictions: {preds}')
print(f'Correct answers: {y_test.values}')

mae = mean_absolute_error(y_test, preds)
print(f'Average error: {mae}')


print(f'Coef: {model.coef_}')
print(f'Intercept: {model.intercept_}')

new_flat = pd.DataFrame([[35, 2, repairIndex['Euro']]], columns=['s', 'roomsCount', 'Repair'])

predictedPrice = model.predict(new_flat)

print(f'Predicted price: {predictedPrice[0]}')




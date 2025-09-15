import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import os
from repair_dict import repairLevelIndex



class Prediction: 

    def readData(self, path: str):
        try:
            data = pd.read_csv(path)
            
            print(f"Data: \n{data}")
            return data

        except FileNotFoundError as e:
            return (f'Error: {e}')

        except Exception as e:
            return (f'Critical error: Cant to read file. Please check the expansion of file must be .csv')
        
    def prepareData(self, data):
        try:
            x = data.drop(['price'], axis=1)
            y = data['price']
            return x, y

        except Exception as e:
            return e
    
    def trainModel(self, x, y):
        try: 
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=10, random_state=42)
            model = LinearRegression()
            model.fit(x_train, y_train)
            return model, x_test, y_test
        
        except Exception as e:
            return e

    def testingModel(self, model, x_test, y_test):
        preds = model.predict(x_test)

        print(f'Predictions: {preds}')
        print(f'Correct answers: {y_test.values}')

        mae = mean_absolute_error(y_test, preds)
        print(f'Average error: {mae}')


        print(f'Coef: {model.coef_}')
        print(f'Intercept: {model.intercept_}')
    
    def predicting(self, new_flat: list, model):
        inputData = pd.DataFrame([[new_flat[0], new_flat[1], repairLevelIndex[new_flat[2]]]], columns=['s', 'roomsCount', 'Repair'])
        predictedPrice = model.predict(inputData)

        print(f'Predicted price: {predictedPrice[0]}')


def main():
    pred = Prediction()

    data = pred.readData('src/dataset.csv')
    if data is not None:
        x,y = pred.prepareData(data)
        model, x_test, y_test = pred.trainModel(x,y)
        pred.testingModel(model, x_test, y_test)

    new_flat = []
    s = float(input('Area: '))
    roomsCount = int(input('Count of rooms(If its studio = 1): '))
    repairLevel = str(input('Repair level(Designed/Euro/Cosmetic): '))

    if repairLevel.strip() not in ['Designed','Euro', 'Cosmetic']:
        print('Unknown repair')
        return

    new_flat.append(s)
    new_flat.append(roomsCount)
    new_flat.append(repairLevel)

    pred.predicting(new_flat, model)


    
if __name__ == "__main__":
    main()




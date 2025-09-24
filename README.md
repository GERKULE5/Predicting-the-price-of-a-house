# Predicting-the-price-of-a-house
## Сервис для предсказания стоимости аренды жилья на основе её площади, количества комнат и уровне ремонта.
### Powered by [Python3](https://www.python.org), [scikit-learn](https://scikit-learn.org/stable/index.html), [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
## Иструкция по запуску

### 1. Клонирования репозитория
```bash
git clone https://github.com/GERKULE5/Predicting-the-price-of-a-house.git
```

### 2. Перейдите в директорию проекта и активируйте виртуальное окрудение
```bash
venv\Scripts\activate
```

### 3. Соберите контейнер
```bash
docker build -t rent-predictor .
```
### 4. Запуск контейнера

```bash
docker run -p 8000:8000 rent-predictor
```

### 5. Сервисе доступен на <http://localhost:8000/docs>

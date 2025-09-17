# Predicting-the-price-of-a-house
## Сервис для предсказания стоимости аренды жилья на основе её площади, количества комнат и уровне ремонта.

## Иструкция по запуску

### 1. Активируйте виртуальное окрудение
```bash
venv\Scripts\activate
```

### 2. Соберите контейнер
```bash
docker build -t rent-predictor .
```
### 3. Запуск контейнера

```bash
docker run -p 8000:8000 rent-predictor
```

# 4. Сервисе доступен на <http://localhost:8000/docs>

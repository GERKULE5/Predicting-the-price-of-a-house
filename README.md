# Predicting-the-price-of-a-house
## Сервис для предсказания стоимости **аренды жилья** на основе площади, количества комнат и уровня ремонта.  
### Powered by [Python3](https://www.python.org), [scikit-learn](https://scikit-learn.org/stable/index.html), [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

## Возможности
- REST API для предсказания стоимости аренды
- Документация Swagger (`/docs`)
- Обёрнут в Docker для удобного запуска
- Лёгкое расширение и переобучение модели

## Модель
Используется модель линейной регрессии:

**Входные признаки:**
- `area` — площадь квартиры (м²)
- `rooms` — количество комнат
- `repair_level` — уровень ремонта (3 — косметический, 4 — евроремонт, 5 — дизайнерский)

**Выход:**
- `repair_level` — предсказанная цена аренды

 ## 📚 Пример запроса/ответа

### POST `/predict`

**Запрос:**
```json
{
  "totalArea": 43,
  "rommsCount": 3,
  "repairLevel": 4
}
```
**Ответ:**
```json
{
  "price": 39729.66012417209
}
```

## Иструкция по запуску

### 1. Клонирования репозитория
```bash
git clone https://github.com/GERKULE5/Predicting-the-price-of-a-house.git
```

### 2. Перейдите в директорию проекта и активируйте виртуальное окружение

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


# Интернет-магазин товаров для реконструкторов.

Данный сервис представляет собой интернет магазин товаров для реконструкторов. В качестве сервиса приема платежей используется [Stripe](https://stripe.com/). Сам проект упакован в Docker контейнер. В качестве базы данных используется SQLite3.

## Установка:

### 1. Копируем содержимое проекта себе в рабочую директорию

### 2. Создаем внутри скопированного проекта образ нашего web-приложения и запускаем контейнеры с брокером очередей, stripe-cli и web-приложением:
```
docker-compose up -d
```

### 3. После запускаем следующую команду и смотрим, что все контейнеры работают:
```
docker ps -a
```

### 4. Далее заходим внутрь контейнера с нашим веб приложением:
```
docker exec -it <ID контейнера> bash
```

### 5. Создаем панель администратора внутри контейнера:

```
python manage.py createsuperuser
```


### 6. Переходим на http://127.0.0.1:8000/ и видим сайт.

## Цели проекта

Код написан в тестовых целях на вакансию компании ООО Ришат. 
 

# testovoe-al
Запуск проекта:
- Создание виртуального окружения
  `python -3.13 -m venv venv`
- Активация виртуального окружения
  `. venv/Scripts/activate`
- Обновление пакетного менеджера pip
  `python -m pip install --upgrade pip`
- Переход в папку с зависимостями
  `cd testvoe/` 
- Установка зависимостей
  `pip install -r requirements.txt`
>  Преобразование JSON схемы, скаченной с [портала открытых данных](https://opendata.mkrf.ru/opendata/7705851331-model_municipal_libraries), в фикстуру. <br>
>  Загрузка полученной фикстуры в базу данных. <br>
>  Запуск сервера <br>
```
python manage.py parsing -o data/data.json -n data/new.json
python manage,py loaddata new.json
python manage,py runserver
```
## Кастомная команда `parsing -o <old file name> -n <new file name>`:
Data after
```
{
  "_id": "5db82e90628b0e30ade6d9e9",
  "hash": "Myниципальное казенное учреждение культуры «Межпоселенческая централизованная библиотечная система» МО «Кошехабльский район» Детская библиотека",
  "nativeId": "Myниципальное казенное учреждение культуры «Межпоселенческая централизованная библиотечная система» МО «Кошехабльский район» Детская библиотека",
  "activated": "2019-10-29T12:20:32.698Z",
  "data": {
    "order": 1,
    "full_name": "Myниципальное казенное учреждение культуры «Межпоселенческая централизованная библиотечная система» МО «Кошехабльский район» Детская библиотека",
    "region": "Республика Адыгея (Адыгея)",
    "address": "Республика Адыгея,\r\nКошехабльский район, аул Кошехабль, ул.\r\nСоветская, дом 55\r\n",
    "year": 2019,
    "inter_budget_transfer_amount": 5000000
  },
  "status": 0,
  "updateSession": "5db82e86f3f3e5724c28af1e",
  "odSetVersions": [
    "5db82e86f3f3e5724c28af1d",
    "5f50f3c8edfe2c17628eb99c"
  ],
  "odSchema": "5daff55f458a0a7219edbcfb",
  "dataset": "5daff402f3f3e5724c283888",
  "created": "2019-10-29T12:20:32.726Z",
  "modified": "2020-09-03T13:46:59.486Z"
}
```
Data after:
```
"data": {
      "order": 1,
      "full_name": "Myниципальное казенное учреждение культуры «Межпоселенческая централизованная библиотечная система» МО «Кошехабльский район» Детская библиотека",
      "region": "Республика Адыгея (Адыгея)",
      "address": "Республика Адыгея,\r\nКошехабльский район, аул Кошехабль, ул.\r\nСоветская, дом 55\r\n",
      "year": 2019,
      "inter_budget_transfer_amount": 5000000
    }
```
Команда упрощает загрузку данных из JSON для работы с Django ORM

## Документация:
Swagger:  `http://127.0.0.1:8000/api/docs/swagger-ui/`
Redoc:  `http://127.0.0.1:8000/api/docs/redoc/`


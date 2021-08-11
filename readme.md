____
## Запуск:
:one: . Создается БД PostgreSQL.

:two: . На одном уровне с файлом dist.env создается файл .env с необходимыми данными:
   
- `PROJECT_STATUS` - принимает одно из значений - `DEVELOPMENT` или `PRODUCTION`,
   в зависимости от того, запускается сайт на сервере для разработки или на "боевом" сервере.  
  

- `ADMIN_URL` - принимает любое значение типа SLUG. Используется для построения 
   URL к сайту администрирования. 


- `SECRET_KEY` - `SECRET_KEY` для `setting.SECRET_KEY` 
 

- `ALLOWED_HOSTS` - `ALLOWED_HOSTS` для `setting.ALLOWED_HOST`. Несколько адресовразделяются запятой и пробелом 
  (<code>, </code>).
   

- `SITE_DOMAIN` - Домен сайта с указанием протокола.
   

- `DB_NAME` - Название базы данных
   

- `DB_USER` - Логин пользователя базы данных с правами управления базой данных `DB_NAME`.
   

- `DB_PASSWORD` - Пароль пользователя `DB_USER`.
   

- `DB_HOST` - Адрес сервера, на котором расположена база данных  `DB_NAME`.
   

- `DB_PORT` - Порт, через который устанавливается соединение с базой данных `DB_NAME`.
   

- `TG_BOT_TOKEN` - API ключ телеграм бота, который присылает уведомления. 
   (Для тестирования можно использавать `1337566022:AAERF4gct7FC3QJgW9fUvMyUmFfAOyCb5rE`).
   

- `TG_ADMIN_ID` - ID пользователя телеграм или канала (бот должен быть администратором канала с правами 
   отправлять сообщения). Для теста можно использовать `-1001531179352`. (Уведомления будут приходить сюда 
https://t.me/test_0091)
____
   
:grey_exclamation: Файл `.env` следует заполнять по примеру файла `dist.env`.
____

:exclamation:   Если `PROJECT_STATUS` установлен как `PRODUCTION` необходимо создать файл `production_settings.py` в папке `config`
   на одном уровне с файлом `settings.py`. Он должен содержать настройки:
   
   `DEBUG` 
   
   `ALLOWED_HOSTS`

   `CORS_ORIGIN_WHITELIST` - Список адресов, с которых будут приниматься запросы к API. Например: 
```python
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:63342']
```
   
   `STATIC_URL`

   `STATICFILES_DIRS`

   `STATIC_ROOT`

   `MEDIA_URL`
___
:three: . <code>pip install -r requirements.txt</code>


:exclamation: Если `PROJECT_STATUS = DEVELOPMENT`, необходимо 

дополнительно установить <code>pip install django-silk django-extensions</code>

ИЛИ

   в `config.local_settings.py` из  `INSTALLED_APPS_LOCAL` убрать приложения
   `silk', 'django_extensions'`. Из `MIDDLEWARE_LOCAL` удалить 
`'silk.middleware.SilkyMiddleware',`
   
в `config.local_urls.py` из `local_urlpatterns` удалить 
`path('silk/', include('silk.urls', namespace='silk')),`
___
:four: . <code>python manage.py makemigrations</code>
   
   <code>python manage.py migrate</code>
___

:five: . Создаем пользователя для доступа в админке:
   <code>python manage.py createsuperuser</code>
___

:six: . <code>python manage.py runserver</code>
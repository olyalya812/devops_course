## Lab_3: Вступ до моніторингу.

1. Створила папку з назвою лабораторної роботи у власному репозиторію ,ініціалізоване середовище pipenv та встановлені необхідні пакети.
2. За допомогою Django Framework створила заготовку проекту та винесла всі створені файли на один рівень вище :
```bash
    pipenv run django-admin startproject my_site
    
    mv my_site/my_site/* my_site/
    mv my_site/manage.py ./
   ``` 
3. Переконалась що все встановилось правильно
    ```bash
    pipenv run python manage.py runserver
    ```
4. Створила коміт з базовим темплейтом сайту
5. Cтворила темплейт додатку та коміт із новоствореними файлами темплейту додатка:
    ```bash
    pipenv run python manage.py startapp main
    ```
 6. Створила потрібні папки та файли)))
 7. Вказала Django frameworks його назву додатку та де шукати веб-сторінки.
 8. Створила .html сторінку та сторінку, яка буде повертати відповідь у форматі JSON;
 9. Результат 1 сторінка:
  ```bash
    You are at main page.
    test
```
Результат 2 стрінка:
```bash
{"date": "2020-11-29 22:13:19", "storinka": "http://127.0.0.1:8000/health/", "infa_pro_server": ["Linux", "olyalya-machine", "5.4.0-53-generic", "#59~18.04.1-Ubuntu SMP Wed Oct 21 12:14:56 UTC 2020", "x86_64"], "infa_pro_clienta": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
```
Все работає)
10. Створила файл monitoring.py та встановила бібліотеку
11. Модифікувала функцію health
```bash
def health(request):
    time = datetime.now()
    response = {'date': time.strftime("%Y-%m-%d %H:%M:%S"),
                'storinka': request.build_absolute_uri(),
                'infa_pro_server': os.uname(),
                'infa_pro_clienta': request.headers['User-Agent']}
    return JsonResponse(response)
```
12. Заповнила потрібні файли, перевірила правильність виконання.
13. Закомітила server.log
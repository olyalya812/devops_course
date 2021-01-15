# Lab 4
## Хід роботи
1. Ознайомилась з тим таке Docker та документацією до нього;
2. Для перевірки, чи ```docker``` встановлено на моїй поточній машині, запустила почергово наступні команди та перенаправила їх у файл ```my_work.log```:
        
       docker -v >> my_work.log
       docker -h >> my_work.log
       docker run docker/whalesay cowsay Docker is fun >> my_work.log
   Зробила коміт з усіма змінами до репозиторію
3. Ознайомилась з базовими принципами роботи ```docker``` та перейла до виконання наступних пунктів.
4. Створила імедж із Django сайтом зробленим у попередній роботі:
    * Використала команду щоб завантажити базовий імедж з репозиторію:
            
        docker pull python:3.7-slim
        docker images
        docker inspect python:3.7-slim
          
        MacBook-Pro:Lab_4 mac$ docker images
        REPOSITORY        TAG        IMAGE ID       CREATED       SIZE
        python            3.7-slim   36b080f01d18   2 days ago    112MB
        docker/whalesay   latest     6b362a9f73eb   5 years ago   247MB

    * Створила файл з іменем Dockerfile скопіювавши туди вміст файлу з основного репозиторію;
    * Ознайомилась із коментарями та зрозуміла структуру написання Dockerfile;
    * Замінила посилання на власний Git репозиторій із моїм веб-сайтом та закомітила даний Dockerfile
5. Створила власний [репозиторій](https://hub.docker.com/repository/docker/olyavalchak/lab4) на Docker Hub
6. Виконала білд (build) Docker імеджа та завантажила його до репозиторію.
        
        docker build -t olyavalchak/lab4:django .
        docker images
        docker push olyavalchak/lab4:django
       
        MacBook-Pro:Lab_4 mac$ docker images
        REPOSITORY         TAG        IMAGE ID       CREATED          SIZE
        olyavalchak/lab4   django     fe16fc1a68b5   11 seconds ago   319MB
        python             3.7-slim   36b080f01d18   2 days ago       112MB
        docker/whalesay    latest     6b362a9f73eb   5 years ago      247MB
    [Посилання на скачування імеджа](https://hub.docker.com/layers/olyavalchak/lab4/django/images/sha256-6c287a125f9898fe1866c69ba46ba45ffef682da18bde5d5afba60431e9e9ebb?context=repo)  
    Команда для скачування: ```docker pull olyavalchak/lab4:django```
7. Запустила щойностворений імедж:
        
        MacBook-Pro:Lab_4 mac$ docker run -it --name=django --rm -p 8000:8000 olyavalchak/lab4:django
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        January 15, 2021 - 09:04:14
        Django version 3.1.3, using settings 'my_site.settings'
        Starting development server at http://0.0.0.0:8000/
        Quit the server with CONTROL-C.
       
        Усе запустилось та веб-сайт за адресою 127.0.0.1:8000 успішно відобразився.
8. Створила файл ```Dockerfile.site``` та збілдила новий імедж для моніторингу серверу:
        
        docker build -t olyavalchak/lab4:monitoring --file Dockerfile.site .
        docker images
        docker push olyavalchak/lab4:monitoring
       
        MacBook-Pro:Lab_4 mac$ docker images
        REPOSITORY         TAG          IMAGE ID       CREATED       SIZE
        olyavalchak/lab4   django       fe16fc1a68b5   8 hours ago   319MB
        olyavalchak/lab4   monitoring   fe16fc1a68b5   8 hours ago   319MB
        python             3.7-slim     36b080f01d18   2 days ago    112MB
        docker/whalesay    latest       6b362a9f73eb   5 years ago   247MB
    
    Запустила обидва імеджі одночасно:
       
        docker run -it --name=django --rm -p 8000:8000 olyavalchak/lab4:django
        docker run --net=host --rm -it olyavalchak/lab4:monitoring
    
    Виконала команди:
       
        sudo docker ps
        sudo docker export 21111a914750 > latest.tar

    І витягла з архіву server.log
    
9. Закомітила усі зміни до репозиторію та створила пулл реквест.

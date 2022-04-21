# airflow1
      Клонировать нужно с ветки dev1

      Сперва нужно запустить сервис - https://github.com/shakhnoza-i/airflow
      
      Запуск в отдельных терминалах на одном уровне с файлом manage.py
      python manage.py runserver 9000
      celery -A core worker -l info
      celery -A core beat -l info

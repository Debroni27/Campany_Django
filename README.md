Запуск базы данных (надо сдлеать в первую очередь)

    docker-compose up db

Зайти в контейнер для конфигурции баз Postgres(при необходимости)

    docker exec -it {id контейнера} psql -U ${USER} ${NAME} bash

Запуск проекта

    docker-compose up web

Запуск тестов

    docker-compose up test

Запуск линтера (flaske8)
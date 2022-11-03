Зайти в контейнер для конфигурции баз Postgres

    docker exec -it {id контейнера} psql -U ${USER} ${NAME} bash
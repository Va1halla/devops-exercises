# База данных в контейнере

1. Запустите контейнер с базой данных любого типа на ваш выбор (MySql, PostgreSQL, Mongo и т.д.)
2. Убедитесь, что контейнер запущен
3. Подключитесь к контейнеру и создайте новую таблицу (или коллекцию — зависит от выбранного типа БД) для студентов
4. Вставьте строку (или документ) с данными студента
5. Убедитесь, что строка/документ добавлены


## Решение

```
# Запустить контейнер
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql

# Убедиться, что он запущен
podman ps

# Добавить строку со студентом в базу данных
podman exec -it mysql /bin/bash
mysql -u root
use university;
CREATE TABLE Students (id int NOT NULL, name varchar(255) DEFAULT NULL, PRIMARY KEY (id));
insert into Projects (id, name) values (1,'Luigi');
select * from Students;
```

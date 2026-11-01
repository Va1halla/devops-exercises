# База данных в контейнере с постоянным хранилищем

1. Запустите контейнер с базой данных любого типа на ваш выбор (MySql, PostgreSQL, Mongo и т.д.)
  1. Используйте для базы данных точку монтирования на хосте вместо хранилища контейнера
  2. Объясните, почему использование хранилища хоста вместо хранилища контейнера может быть более удачным выбором
2. Убедитесь, что контейнер запущен


## Решение

```
# Создать на хосте каталог для БД
mkdir -pv ~/local/mysql
sudo semanage fcontext -a -t container_file_t '/home/USERNAME/local/mysql(/.*)?'
sudo restorecon -R /home/USERNAME/local/mysql

# Запустить контейнер
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql -v /home/USERNAME/local/mysql:/var/lib/mysql/db

# Убедиться, что он запущен
podman ps
```

Лучше использовать хранилище хоста, потому что если контейнер когда-нибудь будет удалён (или его хранилище освобождено), данные БД останутся доступными.

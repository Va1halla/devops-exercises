# Создание образов на лету

## Требования

Иметь хотя бы один образ локально (для проверки выполните `podman image ls`).<br>
Если локальных образов нет, просто выполните `podman pull nginx:alpine`.

## Цели

1. Запустите контейнер из образа веб-сервера (например, httpd, nginx, ...)
  - Привяжите порт 80 контейнера к локальному порту 80
  - Запустите его в фоновом (detached) режиме
  - Имя должно быть nginx_container
2. Убедитесь, что веб-сервер работает и доступен
3. Создайте HTML-файл со следующим содержимым и скопируйте его в контейнер по пути, где он будет доступен как индексный файл

```
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
```

4. Создайте образ из запущенного контейнера и назовите его "nginx_mario"
5. Пометьте контейнер тегом "mario"
6. Удалите исходный контейнер (container_nginx) и убедитесь, что он удалён
7. Создайте новый контейнер из созданного образа (так же, как исходный контейнер)
8. Выполните `curl 127.0.0.1:80`. Что вы видите?
9. Выполните `podman diff` для нового образа. Объясните вывод

## Решение

```
# Запустить контейнер
podman run --name nginx_container -d -p 80:80 nginx:alpine

# Убедиться, что веб-сервер работает
curl 127.0.0.1:80
    #  <!DOCTYPE html>
    #  <html>
    #  <head>
    #  <title>Welcome to nginx!</title>

# Создать файл index.html
cat <<EOT >>index.html
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
EOT

# Скопировать index.html в контейнер
podman cp index.html nginx_container:/usr/share/nginx/html/index.html

# Создать новый образ из запущенного контейнера
podman commit nginx_container nginx_mario

# Пометить образ тегом
podman image ls
# localhost/nginx_mario     latest   dc7ed2343521   52 seconds ago   25 MB
podman tag dc7ed2343521 mario

# Удалить контейнер
podman stop nginx_container
podman rm nginx_container
podman ps -a # контейнера 'nginx_container' нет

# Создать контейнер из образа 
podman run -d -p 80:80 nginx_mario

# Проверить контейнер, созданный из нового образа
curl 127.0.0.1:80
#<html>
#<head>
#<title>It's a me</title>
#</head>
#<body>
#<h1>Mario</h1>
#</body>

# Выполнить diff
podman diff nginx_mario

C /etc
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
A /run/nginx.pid
C /usr/share/nginx/html
C /usr/share/nginx/html/index.html
C /var/cache/nginx
C /var
C /var/cache
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp

# Мы установили новый index.html, поэтому он изменён (C)
# Также мы создали образ во время работы веб-сервера, этим объясняются все файлы, созданные в /var
```

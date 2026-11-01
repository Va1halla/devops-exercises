## Контейнеризация приложения

1. Склонируйте проект с открытым исходным кодом, который хотите контейнеризировать. Пара вариантов:

```
https://github.com/bregman-arie/node-hello-world
https://github.com/bregman-arie/flask-hello-world
```

`git clone https://github.com/bregman-arie/node-hello-world`

2. Напишите Dockerfile для сборки образа приложения (можно использовать любой базовый образ)

```
FROM alpine
LABEL maintainer="your name/email"
RUN apk add --update nodejs npm
COPY . /src
WORKDIR /src
RUN npm install
EXPOSE 3000
ENTRYPOINT ["node", "./app.js"]
```

3. Соберите образ с помощью только что написанного Dockerfile

`docker image build -t web_app:latest .`

4. Убедитесь, что образ существует

`docker image ls`

5. [Необязательно] Отправьте (push) собранный образ в реестр (registry)

```
docker login
docker image tag web_app:latest <your username>/web_app:latest
# Проверьте с помощью "docker image ls"
docker image push <your username>/web_app:latest
```

6. Запустите приложение

```
docker container run -d -p 80:3000 web_app:latest
```

7. Убедитесь, что приложение работает

```
docker container ls
docker logs <container ID/name>
# В браузере откройте 127.0.0.1:80
```

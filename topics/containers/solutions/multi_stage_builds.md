## Многоэтапные сборки (multi-stage builds)

### Цель

Изучить многоэтапные сборки

### Инструкции

1. Не собирая образ и не запуская контейнеров, возьмите следующий Dockerfile и преобразуйте его в многоэтапный:

```
FROM nginx
RUN apt-get update \
 && apt-get install -y curl python build-essential \
 && apt-get install -y nodejs \
 && apt-get clean -y
RUN mkdir -p /my_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
ADD app/ /my_cool_app
WORKDIR /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
RUN apt-get update && apt-get install -y git \
 && npm install \
 && bower install \
RUN ember build — environment=prod
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]
```

2. Какие преимущества дают многоэтапные сборки?

### Решение

1. Одно из возможных решений (акцент на передаче приложения из первого этапа):

```
FROM node:6
RUN mkdir -p /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
WORKDIR /my_cool_app
RUN npm install
ADD app/ /my_cool_app
RUN bower install
RUN ember build — environment=prod

FROM nginx
RUN mkdir -p /my_cool_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
# Скопировать артефакты сборки из первого этапа
COPY — from=0 /my_cool_app/dist /my_cool_app/dist
WORKDIR /my_cool_app
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]
```

2. Многоэтапные сборки позволяют получать образы контейнеров меньшего размера за счёт разделения процесса сборки на несколько этапов, как сделано выше. Образ приложения не содержит ничего, связанного с процессом сборки, кроме самого приложения.

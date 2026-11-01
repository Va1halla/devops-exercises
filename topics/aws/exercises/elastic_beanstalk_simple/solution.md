## AWS Elastic Beanstalk - Node.js

### Предварительные условия
1. Убедиться, что в файле __package.json__ приложения node.js указана команда _npm start_, как в следующем примере
```
{

  "name": "application-name",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "start": "node app"
  },
  "dependencies": {
    "express": "3.1.0",
    "jade": "*",
    "mysql": "*",
    "async": "*",
    "node-uuid": "*"
} 
```
2. Упаковать приложение в zip, причём архивировать не родительскую папку, а только сами файлы, например:

```
\Parent - (exclude the folder itself from the the zip)
- file1 - (include in zip)
- subfolder1 (include in zip)
- file2 (include in zip)
- file3 (include in zip)
```

### Решение

1. Создать "New Environment"
2. Выбрать Environment => _Web Server Environment_
3. Заполнить раздел Create a web server environment
a. Заполнить "Application Name"
4. Заполнить раздел Environment information
a. Заполнить "Environment Name"
b. Domain — "оставить автоматически сгенерированное значение"
5. Platform
a. Выбрать Platform => _node.js_
6. Application Code => загрузить архив с кодом с локального компьютера
7. Create Environment
8. Дождаться запуска окружения
9. Проверить сайт
a. Перейти на вкладку _Applications_, 
b. выбрать только что созданное приложение node.js
c. нажать на выделенный URL

### Документация
[Elastic Beanstalk / Node.js: начало работы](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-getstarted.html)
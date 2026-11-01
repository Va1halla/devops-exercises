# Создание инстанса

## Цели

1. Создать VM-инстанс со следующими свойствами
   1. name: instance-1
   2. type: e2-micro
   3. labels:
      1. app: web
      2. env: dev
2. С помощью CLI (gcloud) выполнить следующие операции:
   1. Изменить метку "app" на "db"
   2. Удалить метку "env"

## Решение

### Консоль

1. Перейдите в Compute Engine -> VM instances
2. Нажмите "Create Instance"
   1. Введите имя "instance-1"
   2. Нажмите "Add label" и добавьте следующие метки:
      1. app: web
      2. env: dev
   3. Выберите тип машины: e2-micro
3. Нажмите "Create"
4. Выберите созданный инстанс и нажмите "show info panel"
   1. Перейдите на вкладку "labels" и измените значение метки "app" на "db"
   2. Удалите метку "env"

### Shell

```
gcloud config set project <PROJECT_ID>
gcloud config set compute/region <REGION NAME>
gcloud config set compute/zone <ZONE NAME>

gcloud compute instances create instance-1 --labels app=web,env=dev --machine-type=e2-micro
gcloud compute instances update instance-1 --update-labels app=db
gcloud compute instances update instance-1 --remove-labels env
```

### Terraform

Нажмите [здесь](main.tf), чтобы посмотреть файл main.tf
# Мой первый VPC

## Цели

1. Создать новый VPC
   1.  Его CIDR должен позволять использовать не менее 60 000 хостов
   2.  Он должен называться "exercise-vpc"

## Решение

### Консоль

1. В разделе "Virtual Private Cloud" нажать "Your VPCs"
2. Нажать "Create VPC"
3. Ввести имя — "exercise-vpc"
4. Ввести IPv4 CIDR block: 10.0.0.0/16
5. Оставить "Tenancy" в значении Default
6. Нажать "Create VPC"

### Terraform

Нажмите [здесь](terraform/main.tf), чтобы посмотреть решение

### Pulumi - Python

Нажмите [здесь](pulumi/__main__.py), чтобы посмотреть решение

### Проверка решения

Чтобы убедиться, что VPC создан, можно выполнить: `aws ec2 describe-vpcs -filters Name=tag:Name,Values=exercise-vpc`
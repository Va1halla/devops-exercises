# Создание собственного VPC и подсетей с помощью Terraform


## Задачи
1. Создать собственный VPC с заданным CIDR-блоком.
    Например, можно использовать `10.0.0.0/16`.
2. Создать две подсети внутри VPC, каждую со своим CIDR-блоком.
    Например, можно использовать `10.0.0.0/20` для первой подсети и `10.0.16.0/20` для второй.

    Обе подсети должны находиться в разных зонах доступности (availability zones), чтобы обеспечить высокую доступность.
3. Убедиться, что VPC и подсети отслеживаются Terraform.


## Решение



```sh
# Создать каталог для конфигурации Terraform
mkdir vpc_subnet_creation && cd vpc_subnet_creation 
```

```sh
# Создать файл main.tf с конфигурацией VPC и подсетей
touch main.tf
```

```terraform
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "your-region" # например, ap-south-1
}

resource "aws_vpc" "my_custom_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "my_custom_vpc_made_with_terraform"
  }
}

resource "aws_subnet" "Subnet_A" {
  cidr_block       = "10.0.0.0/20"
  vpc_id            = aws_vpc.my_custom_vpc.id
  availability_zone = "your-availability-zone-a" # например, ap-south-1a
  tags = {
    "Name" = "Subnet A"
  }
}
resource "aws_subnet" "Subnet_B" {
  cidr_block       = "10.0.16.0/20"
  vpc_id            = aws_vpc.my_custom_vpc.id
  availability_zone = "your-availability-zone-b" # например, ap-south-1b
  tags = {
    "Name" = "Subnet B"
  }
}
```

```sh
# Инициализировать Terraform, чтобы скачать провайдер AWS
terraform init
```

```sh
# Применить конфигурацию Terraform, чтобы создать VPC и подсети
terraform apply -auto-approve
```




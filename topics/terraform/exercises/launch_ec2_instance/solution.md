# Запуск инстанса EC2

## Требования

* Аккаунт AWS

## Задачи

1. Написать конфигурацию Terraform для запуска инстанса EC2
2. Выполнить команды, чтобы применить конфигурацию и создать инстанс EC2
3. Что произойдёт, если снова выполнить `terraform apply`?
4. Удалить созданный с помощью Terraform инстанс

## Решение

```
mkdir exercise

cat << EOT >> main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
EOT

terraform init
terraform validate
terraform plan

# В конце должна появиться строка: Plan: 1 to add, 0 to change, 0 to destroy

terraform apply -auto-approve

# Должен появиться следующий вывод:
# aws_instance.app_server: Creation complete after 49s [id=i-004651a9d4427d236

# Повторный запуск 'terraform apply' ничего не изменит, так как
# Terraform сравнит фактическую инфраструктуру с
# конфигурацией и не найдёт различий. Должна появиться следующая строка:
# Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

# Удалить инстанс
terraform destroy -auto-approve

# Destroy complete! Resources: 1 destroyed.
```
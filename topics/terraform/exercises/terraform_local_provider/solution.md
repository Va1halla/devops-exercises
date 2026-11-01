# Провайдер local

## Задачи

Научиться использовать и запускать базовые команды Terraform

1. Создать каталог с именем "my_first_run"
2. Внутри каталога создать файл "main.tf" со следующим содержимым

```terraform
resource "local_file" "mario_local_file" {
    content  = "It's a me, Mario!"
    filename = "/tmp/who_is_it.txt"
}
```
3. Выполнить `terraform init`. Что сделала команда?
4. Выполнить `terraform plan`. Что Terraform собирается сделать?
5. Наконец, выполнить 'terraform apply' и проверить, что файл был создан

## Решение

```sh
# Создать каталог
mkdir my_first_run && cd my_first_run

# Создать файл 'main.tf'
cat << EOT >>  main.tf
resource "local_file" "mario_local_file" {
    content  = "It's a me, Mario!"
    filename = "/tmp/who_is_it.txt"
}
EOT

# Выполнить 'terraform init'
terraform init
# Выполнив 'ls -la', можно увидеть, что были созданы '.terraform' и '.terraform.lock.hcl'
# Кроме того, команда инициализировала (скачала и установила) нужные плагины провайдеров. В данном случае — "hashicorp/local"

# Выполнить 'terraform plan'
terraform plan
# Показывает, что Terraform сделает при запуске 'terraform apply'

<< terraform_plan_output
Terraform will perform the following actions:

  # local_file.mario_local_file will be created
  + resource "local_file" "mario_local_file" {
      + content              = "It's a me, Mario!"
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "/tmp/who_is_it.txt"
      + id                   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.
terraform_plan_output

# Применить main.tf (если вы новичок в Terraform, лучше запускать без -auto-approve)
terraform apply -auto-approve

ls /tmp/who_is_it.txt
# /tmp/who_is_it.txt
```
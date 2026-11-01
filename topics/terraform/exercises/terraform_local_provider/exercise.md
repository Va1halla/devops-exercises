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
5. Наконец, выполнить `terraform apply` и проверить, что файл был создан

## Решение

Нажмите [здесь, чтобы посмотреть решение](solution.md)

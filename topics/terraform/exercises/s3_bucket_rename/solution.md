# Переименование S3-бакета

## Требования

* Существующий S3-бакет (bucket), отслеживаемый Terraform.
Если его нет, можно использовать следующий блок и выполнить `terraform apply`:

```terraform
resource "aws_s3_bucket" "some_bucket" {
    bucket = "some-old-bucket"
}
```

Внимание: поскольку имена S3-бакетов глобально уникальны, скорее всего, придётся переименовать бакет, так как кто-то другой мог уже занять это имя.

## Задачи

1. Переименовать существующий S3-бакет и убедиться, что он по-прежнему отслеживается Terraform

## Решение

```sh
# Имя бакета в AWS неизменяемо, поэтому придётся создать новый бакет
aws s3 mb s3://some-new-bucket-123

# Синхронизировать старый бакет с новым
aws s3 sync s3://some-old-bucket s3://some-new-bucket-123

# Вариант 1 (удаление и импорт)

## Удалить старый бакет из состояния (state) Terraform
terraform state rm aws_s3_bucket.some_bucket

## Импортировать новый бакет в состояние Terraform
terraform import aws_s3_bucket.some_bucket some-new-bucket-123

: '
aws_s3_bucket.some_bucket: Refreshing state... [id=some-new-bucket-123]

Import successful!
The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
'

# Вариант 2 (перемещение)

## Переместить старый бакет в состоянии Terraform на новый
terraform state mv aws_s3_bucket.some_bucket some-new-bucket-123

: '
Move "aws_s3_bucket.some_bucket" to "aws_s3_bucket.some-new-bucket-123"
Successfully moved 1 object(s).
'

# Изменить файл Terraform

# Изменить определение в Terraform, указав новое имя
# resource "aws_s3_bucket" "some_bucket" {
#    bucket = "some-new-bucket-123"
# }

# Удалить старый бакет
aws s3 rm s3://some-old-bucket --recursive
aws s3 rb s3://some-old-bucket
```

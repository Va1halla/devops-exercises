## IAM AWS - создание пользователя

### Цели

Как вы, вероятно, уже знаете, работать в AWS под root-аккаунтом не рекомендуется. Поэтому нужно создать новую учётную запись, которая будет регулярно использоваться как администраторская.

1. Создать пользователя с учётными данными в виде пароля
2. Добавить нового пользователя в группу "admin" и привязать к ней политику "Administrator Access"
3. Убедиться, что у пользователя есть тег с ключом `Role` и значением `DevOps`


### Решение

1. Перейти в сервис AWS IAM
2. Нажать "Users" в правом меню (сразу под "Access Management")
3. Нажать кнопку "Add users"
4. Ввести имя пользователя (например, mario)
5. Выбрать тип учётных данных: "Password"
6. Задать собственный пароль для консоли и нажать "Next"
7. Нажать "Add user to group"
8. Ввести "admin" в качестве имени группы
9. Отметить политику "AdministratorAccess" и нажать "Create group"
10. Нажать "Next: Tags"
11. Добавить тег с ключом `Role` и значением `DevOps`
12. Нажать "Review", а затем "Create user"

13. ### Решение с помощью Terraform
    
```
 
resource "aws_iam_group_membership" "team" {
  name = "tf-testing-group-membership"

  users = [
    aws_iam_user.newuser.name,

  ]

  group = aws_iam_group.admin.name
}

resource "aws_iam_group_policy_attachment" "test-attach" {
  group      = aws_iam_group.admin.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}
resource "aws_iam_group" "admin" {
  name = "admin"
}

resource "aws_iam_user" "newuser" {
  name = "newuser"
  path = "/system/"

  tags = {
    Role = "DevOps"
  }
}
```


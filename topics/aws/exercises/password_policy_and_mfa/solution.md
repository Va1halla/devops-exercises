## AWS IAM - политика паролей и MFA

Примечание: НЕ выполняйте это упражнение, если не понимаете, что делаете и к чему приведёт применение этих изменений к вашему аккаунту

### Цели

1. Создать политику паролей со следующими настройками:
  1. Минимум 8 символов
  2. Как минимум одна цифра
  3. Запрет повторного использования паролей

2. Затем включить MFA для аккаунта.

### Решение

Политика паролей:

1. Перейти в сервис IAM в AWS
2. Нажать "Account settings" в разделе "Access management"
3. Нажать "Change password policy"
  1. Отметить "Enforce minimum password length" и установить 8 символов
  1. Отметить "Require at least one number"
  1. Отметить "Prevent password reuse"
4. Нажать "Save changes"

MFA:

1. Нажать на имя аккаунта
2. Нажать "My Security Credentials"
3. Развернуть "Multi-factor authentication (MFA)" и нажать "Activate MFA"
4. Выбрать одно из устройств
5. Следовать инструкциям по настройке и нажать "Assign MFA"

6. ### Решение с помощью Terraform:

```
resource "aws_iam_account_password_policy" "strict" {
  minimum_password_length        = 8
  require_numbers                = true
  allow_users_to_change_password = true
  password_reuse_prevention      = 1
}
```

 **Примечание:** добавить MFA через terraform нельзя, это нужно сделать в GUI.


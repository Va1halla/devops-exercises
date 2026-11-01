## Функция Hello - решение

### Упражнение

Создать простую функцию AWS Lambda, которая получает имя и возвращает "Hello <NAME>"

### Решение

#### Определение функции

1. Открыть панель консоли Lambda и нажать `Create function`
  1. Задать функции имя, например `BasicFunction`
  2. Выбрать среду выполнения `Python3`
  3. Чтобы настроить разрешения функции, к ней можно привязать роль IAM — указав существующую или создав новую. Я выбрал "Create a new role from AWS policy templates"
  4. В "Policy Templates" выбрать "Simple Microservice Permissions"

1. Далее появится текстовый редактор, куда нужно вставить код наподобие следующего

#### Код функции
```
import json


def lambda_handler(event, context):
    firstName = event['name']
    return 'Hello ' + firstName
```
2. Нажать "Create Function"

#### Определение теста

1. Теперь протестируем функцию. Нажать "Test".
2. Выбрать "Create new test event"
3. Задать любое "Event name". Например, "TestEvent"
4. Указать ключи для теста

```
{
  "name": 'Spyro'
}
```
5. Нажать "Create"

#### Тестирование функции

1. Выбрать созданное тестовое событие (`TestEvent`)
2. Нажать кнопку `Test`
3. Должно появиться что-то вроде `Execution result: succeeded`
4. В AWS CloudWatch должен появиться соответствующий поток логов (log stream) 

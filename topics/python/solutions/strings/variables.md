## Строки и переменные

Используя переменную `fruit = "strawberry"`, вывести следующее:

1. `Best fruit is: strawberry`
2. `Yes, strawberry. Only strawberry`
3. `Hello, my name is Mr. Strawberry`
4. `fruit = 'strawberry'`

### Решение

1. `print(f'Best fruit is: {fruit}')`
2. `print(f'Yes, {fruit}. Only {fruit}')`
3. `print(f'Hello, my name is Mr. {fruit.capitalize()}')`
4. `print(f'{fruit = }')`  # Поддерживается только в Python 3.8+

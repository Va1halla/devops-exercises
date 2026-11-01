# Калькулятор — модульные тесты

Написать модульные тесты (unit tests) для следующих функций

```python
def add(x, y):
   """Add numbers"""
   return x + y

def substract(x, y):
   """Substract numbers"""
   return x - y

def multiply(x, y):
   """Multiply numbers"""
   return x * y

def divide(x, y):
   """Divide numbers"""
   if y == 0:
       raise ValueError('Can not divide by zero!')
   return x / y
```

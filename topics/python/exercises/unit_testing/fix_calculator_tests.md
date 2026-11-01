## Исправление тестов калькулятора

Исправить следующий файл тестов на Python так, чтобы тесты успешно запускались

```python
import unittest
import calc

class TestCalculator(unittest.TestCase):

def add_test(self):
    self.assertEqual(calculator.add(1, 1), 2)


def test_substract():
    self.assertEqual(calculator.substract(4, 3), 1)
```

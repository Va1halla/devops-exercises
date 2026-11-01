## Палиндром

1. Написать код, который определяет, является ли число палиндромом

## Решение

1.

```
from typing import Union

def isNumberPalindrome(number: Union[int, str]) -> bool:
    if isinstance(number, int):
        number = str(number)
    return number == number[::-1]

print(isNumberPalindrome("12321"))
```

- С использованием Python3.10, который допускает использование побитового оператора '|'.

```
def isNumberPalindrome(number: int | str) -> bool:
    if isinstance(number, int):
        number = str(number)
    return number == number[::-1]

print(isNumberPalindrome("12321"))
```

Примечание: разворот списка с помощью среза может быть медленнее, чем другие варианты, например `reversed`, который возвращает итератор.

## Разворот строки

1. Развернуть строку

### Решение

```
my_string[::-1]
```

Более наглядный способ:<br>
<i>Осторожно: это очень медленно</i>

```
def reverse_string(string):
    temp = ""
    for char in string:
        temp =  char + temp
    return temp
```

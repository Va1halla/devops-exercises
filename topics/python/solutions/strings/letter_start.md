## Начинается с буквы

1. Как проверить, начинается ли строка с буквы?

### Решение

```python

# Regex based solution
import re
if re.match("^[a-zA-Z]+.*", string):
    print("yay, it starts with a letter")

# Built-in string method
if string and string[0].isalpha():
    print("yay, it starts with a letter")
```

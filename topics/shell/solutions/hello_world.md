## Скрипты на Shell — Hello World

### Цели

1. Определить переменную со строкой 'Hello World'
2. Вывести значение определённой переменной и перенаправить вывод в файл "amazing_output.txt"

### Решение

```
#!/usr/bin/env bash

HW_STR="Hello World"
echo $HW_STR > amazing_output.txt
```

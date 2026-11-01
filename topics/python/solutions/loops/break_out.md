## Выход из цикла

Написать цикл, который будет разворачивать ввод пользователя, пока он не введёт букву 'q' для выхода

## Решение

```python
while True:
  ans = input("Please insert a string to reverse: ")
  if ans == 'q':
      break
  print(ans[::-1])
```

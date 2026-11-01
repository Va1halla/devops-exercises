## Три наибольших элемента

1. Вывести три наибольших элемента списка

### Решение

```python
sorted(some_list, reverse=True)[:3]
```

Или

```python
some_list.sort(reverse=True)
some_list[:3]
```

## Гласные буквы

1. Улучшить следующий код

```python
char = input("Insert a character: ")
if char == "a" or char == "o" or char == "e" or char =="u" or char == "i":
    print("It's a vowel!")
```

### Решение

```python
char = input("Insert a character: ") # For readablity
if lower(char[0]) in "aieou": # Takes care of multiple characters and separate cases
    print("It's a vowel!")
```
ИЛИ
```python
if lower(input("Insert a character: ")[0]) in "aieou": # Takes care of multiple characters and small/Capital cases
    print("It's a vowel!")
```

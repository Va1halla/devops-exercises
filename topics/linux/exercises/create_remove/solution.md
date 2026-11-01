# Создание и удаление

## Задачи

1. Создать файл с именем `x`
2. Создать каталог с именем `content`
3. Переместить файл `x` в каталог `content`
4. Создать внутри каталога `content` файл с именем `y`
5. Создать в каталоге `content` следующую структуру каталогов: `dir1/dir2/dir3`
6. Удалить каталог content

## Решение

```
touch x
mkdir content
mv x content
touch content/y
mkdir -p content/dir1/dir2/dir3
rm -rf content
```

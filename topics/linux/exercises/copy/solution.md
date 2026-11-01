# Время копировать

## Задачи

1. Создать пустой файл с именем `x` в `/tmp`
2. Скопировать созданный файл `x` в домашний каталог
3. Создать копию файла `x` с именем `y`
4. Создать каталог с именем `files` и переместить туда `x` и `y`
5. Скопировать каталог "files" и назвать копию `copy_of_files`
6. Переименовать каталог `copy_of_files` в `files2`
7. Удалить каталоги `files` и `files2`

## Решение

```
touch /tmp/x
cp x ~/
cp x y
mkdir files
mv x files | mv y files
cp -r files copy_of_files
mv copy_of_files files2
rm -rf files files2
```

## Сравнение каталогов

### Цели

1. В качестве аргументов передаются два каталога; на выходе должны быть все различия между этими двумя каталогами

### Решение 1

Предположим, что скрипт bash называется ```dirdiff.sh```

```
#!/bin/bash

if test $# -ne 2
then
	echo -e "USAGE: ./dirdiff.sh directory1 directory2"
	exit 1
fi

# check for the checksums. 
# If both the checksums same, then both directories are same
if test `ls -1 $1 | sort | md5sum | awk -F "  " '{print $1}'` == `ls -1 $2 | sort | md5sum | awk -F "  " '{print $1}'`
then
	echo -e "No difference between the 2 directories"
	exit 0
fi

diff -q $1 $2
```

### Решение 2

С GNU find можно использовать diff для рекурсивного сравнения каталогов.

```shell
diff --recursive directory1 directory2
```

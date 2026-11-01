# Типы данных

## Задачи

1. Каков результат выполнения следующей программы? Почему?

```Go
package main

import "fmt"

func main() {
    var userName
    userName = "user"
    fmt.Println(userName)
}
```

2. Каков результат выполнения следующей программы? Почему?

```Go
package main

import "fmt"

func main() {
    var userName = 2
    fmt.Println(userName)
}
```

3. Исправьте следующую программу, изменив одну из строк (не добавляя и не удаляя строки)

```Go
package main

import "fmt"

func main() {
    var userName
    userName = "user"
    fmt.Println(userName)
}
```

4. Измените следующую программу так, чтобы она выводила типы переменных

```Go
package main

import "fmt"

func main() {
    var food = "Pizza"
    var slices = 4
    var pineappleOnPizza = True
}
```

## Решение

1. Ошибка. Go — язык со статической типизацией, и при объявлении переменной нужно сообщить компилятору Go тип данных.

2. Будет выведено 2. Ошибки нет (хотя тип не объявлен), потому что Go выполняет вывод типов (type inference): тип определяется по присвоенному значению

3. Объявить тип userName

```Go
package main

import "fmt"

func main() {
    var userName string
    userName = "user"
    fmt.Println(userName)
}
```

4. 

```Go
package main

import "fmt"

func main() {
    var food = "Pizza"
    var slices = 4
    var pineappleOnPizza = true

    fmt.Printf("food is %T\nslices is %T\npineappleOnPizza is %T", food, slices, pineappleOnPizza)
}
```
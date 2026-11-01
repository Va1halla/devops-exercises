# Именованные возвращаемые значения

## Задачи

1. Каков результат выполнения следующего кода?

```Go
package main
        
import "fmt"
        
func add(x, y int) {
    var z int = x + y                     
    return z
}
       
func main() {
    fmt.Print(add(3, 2))
}
```

2. Исправьте код выше

3. Будет ли следующий код работать правильно? Объясните

```Go
package main
        
import "fmt"
        
func add(x, y int) (z int) {
    z = x + y                     
    return
}
       
func main() {
    fmt.Print(add(3, 2))
}
```

## Решение

1. Произойдёт ошибка, так как функция объявлена без возвращаемого значения, а возвращает целое число.

2. 

```Go
package main
        
import "fmt"
        
func add(x, y int) (z int) {
    z = x + y                     
    return z
}
       
func main() {
    fmt.Print(add(3, 2))
}
```

3. Да, это так называемый «голый return» (naked return). Это оператор return без аргументов, который возвращает именованные значения (в данном случае `z`)
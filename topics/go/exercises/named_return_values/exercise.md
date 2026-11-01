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

Нажмите [здесь](solution.md), чтобы посмотреть решение
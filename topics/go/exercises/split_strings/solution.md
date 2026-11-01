# Разделение строк

## Задачи

1. Определите переменную со значением этого имени/строки: `Alexander Supertramp`
2. Используя определённую переменную, выведите только имя
3. Используя определённую переменную, выведите только фамилию

## Решение

```Go
package main
        
import (
    "fmt"
    "strings"
)

func main() {

    var name string = "Alexander Supertramp"
    fmt.Printf("First name: %v\n", strings.Fields(name)[0])                                                        
    fmt.Printf("Surname: %v", strings.Fields(name)[1])
}
```
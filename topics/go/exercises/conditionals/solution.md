# Условные операторы

## Задачи

1. Сгенерируйте случайное число от 1 до 100
   1. Если число больше 50, выведите "It's closer to 100"
   2. Если число меньше 50, выведите "It's closer to 0"
   3. Выведите сгенерированное случайное число
2. Измените предыдущий код так, чтобы он выводил "It's 50!", если случайное число равно 50
3. Измените условие в написанном ранее коде так, чтобы проверялось не только то, что число больше 50, но и то, что оно чётное. Если оно чётное и больше 50, выведите "It's closer to 100 and it's even!"


## Решение

1. 

```Go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    rand.Seed(time.Now().UnixNano())
    var randNum int = rand.Intn(100)

    if randNum > 50 {
        fmt.Println("It's closer to 100")
    } else {
        fmt.Println("It's closer to 0")
    }                                      
    fmt.Printf("Generated number: %v\n", randNum)
}
```

2. 

```Go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    rand.Seed(time.Now().UnixNano())
    var randNum int = rand.Intn(100)

    if randNum > 50 {
        fmt.Println("It's closer to 100")
    } else if randNum < 50 {
        fmt.Println("It's closer to 0")
    } else {
        fmt.Println("It's 50!")
    }
                             
    fmt.Printf("Generated number: %v\n", randNum)
}
```

3. 

```Go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    rand.Seed(time.Now().UnixNano())
    var randNum int = rand.Intn(100)

    if randNum > 50 && randNum%2 == 0 { 
        fmt.Println("It's closer to 100 and even")
    } else if randNum < 50 {
        fmt.Println("It's closer to 0")
    } else if randNum == 50 {                     
        fmt.Println("It's 50!")
    }
    fmt.Printf("Generated number: %v\n", randNum)
}
```
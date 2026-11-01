# Переменные

## Задачи

1. Напишите программу на Go, которая сохраняет имя и возраст в переменных (или константах) и выводит следующее предложение с использованием определённых переменных: `My name is ___ and I'm ___ years old`
   
2. Объясните, почему следующая программа завершится с ошибкой?

```Go
package main

import "fmt"

func main() {
    fmt.Println("Skynet Beta Testing")

    var objective="Defend Humanity"
}
```

3. Что выведет следующая программа?

```Go
package main

import "fmt"

func main() {
    const squares=2
    var circles=0
    
    fmt.Println("Squares:", squares)
    fmt.Println("Circles:", circles)

    squares=1
    circles=7

    fmt.Println("Squares:", squares)
    fmt.Println("Circles:", circles)
}
```

## Решение

Нажмите [здесь](main.go), чтобы посмотреть решение
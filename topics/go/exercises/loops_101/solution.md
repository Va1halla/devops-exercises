# Циклы 101

## Задачи

1. Напишите цикл, который запрашивает у пользователя имя и возраст и выводит "Your name is ___ and your age is ___ years old"
   1. Цикл должен быть бесконечным
2. Определите следующий массив `"pizza"}`
   1. Добавьте в него элемент: "hamburger"
   2. Добавьте в него элемент: "salad"
   3. Переберите список и для каждого элемента выведите `Food: <Food name>`. `<Food name>` нужно заменить элементом массива
3. Определите следующий массив фиксированной длины из 3 элементов: `{square, circle, triangle}`
   1. Переберите его и для каждого элемента выведите следующее: `This is <ITEM> and its index in the array is <INDEX>`


## Решение

1. 

```Go
package main
            
import "fmt"
         
func main() {
    var name string
    var age uint
         
    for {
         
        fmt.Print("\nEnter your name: ")
        fmt.Scan(&name)
        fmt.Print("Enter your age: ")
        fmt.Scan(&age)
         
        fmt.Printf("\nYour name is %v and your age is %v years old\n", name, age)                                                                                            
    }       
}
```

2. 

```Go
package main
 
import "fmt"
 
func main() {
 
    var foods = []string{"pizza"}
                                                                                                                                                                             
    foods = append(foods, "hamburger")
    foods = append(foods, "salad")
 
    for _, food := range foods {
        fmt.Printf("Food: %v\n", food)
    }   
}
```

3. .

```Go
package main

import "fmt"

func main() {

    var shapes = [3]string{"square", "circle", "triangle"}
    
    for index, shape := range shapes {
        fmt.Printf("This is %v and its index in the array is %v\n", shape,index)                                        
    }
}
```
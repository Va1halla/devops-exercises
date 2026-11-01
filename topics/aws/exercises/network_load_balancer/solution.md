## AWS ELB - Network Load Balancer

### Требования                   

Два работающих экземпляра EC2

### Цели

1. Создать Network Load Balancer 
  1. healthy threshold: 3
  2. unhealthy threshold: 3
  3. interval: 10 секунд
  4. Listener должен использовать протокол TCP на порту 80

### Решение

#### Консоль

1. Перейти в сервис EC2
2. В меню слева нажать "Load balancers" в разделе "Load balancing"
3. Нажать "Create load balancer"
4. Выбрать "Network Load Balancer"
5. Ввести имя для LB
6. Выбрать AZ, в которых должен работать LB
7. Выбрать группу безопасности
8. В разделе "Listeners and routing" нажать "Create target group" и выбрать "Instances"
  1. Указать имя целевой группы
  2. Установить healthy threshold в 3
  3. Установить unhealthy threshold в 3
  4. Установить interval в 10 секунд
  5. Установить протокол TCP и порт 80
  6. Нажать "Next" и выбрать два имеющихся экземпляра
  7. Нажать "Create target group"
9. Обновить список целевых групп и выбрать только что созданную
10. Нажать "Create load balancer" и дождаться его создания

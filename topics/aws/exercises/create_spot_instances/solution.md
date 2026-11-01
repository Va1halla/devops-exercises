## AWS EC2 - Spot-экземпляры (Spot Instances)                                                                                                                                                  
### Цели             

A. Создать два Spot-экземпляра с помощью Spot Request со следующими параметрами:

* AMI Amazon Linux 2
* целевая ёмкость — 2 экземпляра (в любой момент времени), у каждого 2 vCPU и 3 GiB RAM

B. Создать один Spot-экземпляр на Amazon Linux 2 и t2.micro

### Решение               

A. Создание Spot Fleet:

1. Перейти в сервис EC2
2. Нажать "Spot Requests"
3. Нажать кнопку "Request Spot Instances"
4. Задать следующие значения параметров:
  * AMI Amazon Linux 2
  * Total target capacity -> 2
  * Отметить "Maintain target capacity"
  * vCPUs: 2
  * Memory: 3 GiB RAM
5. Нажать Launch

B. Создание одного Spot-экземпляра:

1. Перейти в сервис EC2
2. Нажать "Instances"
3. Нажать "Launch Instances"
4. Выбрать "Amazon Linux 2 AMI" и нажать "Next"
5. Выбрать t2.micro и нажать "Next: Configure Instance Details"
6. Выбрать "Request Spot instances" 
7. Установить максимальную цену выше текущей
8. Нажать "Review and Launch"

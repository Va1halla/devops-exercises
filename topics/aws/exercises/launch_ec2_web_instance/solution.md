## AWS - запуск веб-экземпляра EC2

### Цели

Запустить один экземпляр EC2 со следующими требованиями:

1. Образ Amazon Linux 2
2. Тип экземпляра: выбрать тот, у которого 1 vCPU и 1 GiB памяти
3. Хранилище экземпляра должно удаляться при его завершении (termination)
4. При запуске экземпляр должен:
  1. Установить пакет httpd
  2. Запустить сервис httpd
  3. Сделать так, чтобы содержимое /var/www/html/index.html было `I made it! This is is awesome!`
5. У него должен быть тег "Type: web", а имя экземпляра — "web-1"
6. HTTP-трафик (порт 80) должен приниматься откуда угодно

### Решение

1. Выбрать ближайший регион 
2. Перейти в сервис EC2
3. Нажать "Instances" в меню и нажать "Launch instances"
4. Выбрать образ: Amazon Linux 2
5. Выбрать тип экземпляра: t2.micro 
6. Убедиться, что в разделе хранилища отмечено "Delete on Termination"
7. В поле "User data" указать следующее:

```
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>I made it! This is is awesome!</h1>" > /var/www/html/index.html
```
8. Добавить теги со следующими ключами и значениями:
  * ключ "Type" и значение "web"
  * ключ "Name" и значение "web-1"
9. В разделе группы безопасности добавить правило, разрешающее HTTP-трафик (TCP) на порт 80 откуда угодно
10. Нажать "Review", а после проверки — "Launch".
11. Если пары ключей нет, создать её и скачать.

12. ### Решение с помощью Terraform

```
 
provider "aws" {
  region = "us-east-1" // Или нужный вам регион
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678" // Замените на подходящий AMI для Amazon Linux 2
  instance_type = "t2.micro" // Или любой тип экземпляра с 1 vCPU и 1 GiB памяти

  tags = {
    Name = "web-1"
    Type = "web"
  }

  root_block_device {
    volume_size           = 8 // Или любой нужный размер
    delete_on_termination = true
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo bash -c 'echo \"I made it! This is awesome!\" > /var/www/html/index.html'",
      "sudo systemctl enable httpd"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/your_private_key.pem") // Замените на путь к своему приватному ключу
      host        = self.public_ip
    }
  }

  security_group_ids = [aws_security_group.web_sg.id]
}

resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Security group for web server"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```
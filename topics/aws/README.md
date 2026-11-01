# AWS

**Примечание**: некоторые упражнения <b>стоят $$$</b> и не могут быть выполнены в рамках бесплатного уровня (free tier) или ресурсов

**Второе примечание**: приведённые решения используют консоль AWS. Рекомендуется решать упражнения с помощью IaC-технологий (например, Terraform, Pulumi).<br>

- [AWS](#aws)
  - [Упражнения](#упражнения)
    - [IAM](#iam)
    - [EC2](#ec2)
    - [S3](#s3)
    - [ELB](#elb)
    - [Auto Scaling Groups] (#auto-scaling-groups)
    - [VPC](#vpc)
    - [Базы данных](#базы-данных)
    - [DNS](#dns)
    - [Контейнеры](#контейнеры)
    - [Lambda](#lambda)
    - [Elastic Beanstalk](#elastic-beanstalk)
    - [CodePipeline](#codepipeline)
    - [CDK](#cdk)
    - [Разное](#разное)
  - [Вопросы](#вопросы)
    - [Глобальная инфраструктура](#глобальная-инфраструктура)
    - [IAM](#iam-1)
    - [EC2](#ec2-1)
    - [AMI](#ami)
    - [EBS](#ebs)
    - [Instance Store](#instance-store)
    - [EFS](#efs)
    - [Модели ценообразования](#модели-ценообразования)
    - [Launch Template](#launch-template)
    - [ENI](#eni)
    - [Placement Groups](#placement-groups)
    - [VPC](#vpc-1)
      - [VPC по умолчанию](#vpc-по-умолчанию)
    - [Lambda](#lambda-1)
    - [Контейнеры](#контейнеры-1)
      - [ECS](#ecs)
      - [Fargate](#fargate)
    - [S3](#s3-1)
      - [Основы](#основы)
      - [Бакеты 101](#бакеты-101)
      - [Объекты](#объекты)
      - [Безопасность S3](#безопасность-s3)
      - [Разное](#разное-1)
    - [Аварийное восстановление](#аварийное-восстановление)
    - [CloudFront](#cloudfront)
    - [ELB](#elb-1)
      - [NLB](#nlb)
      - [ALB](#alb)
    - [Auto Scaling Group](#auto-scaling-group)
    - [Безопасность](#безопасность)
    - [Базы данных](#базы-данных-1)
      - [RDS](#rds)
      - [Aurora](#aurora)
      - [DynamoDB](#dynamodb)
      - [ElastiCache](#elasticache)
      - [RedShift](#redshift)
    - [Определите сервис](#определите-сервис)
    - [DNS (Route 53)](#dns-route-53)
    - [SQS](#sqs)
    - [SNS](#sns)
    - [Мониторинг и логирование](#мониторинг-и-логирование)
    - [Биллинг и поддержка](#биллинг-и-поддержка)
    - [AWS Organizations](#aws-organizations)
    - [Автоматизация](#автоматизация)
    - [Разное](#разное-2)
    - [Высокая доступность](#высокая-доступность)
    - [Эксплуатация в продакшене и миграции](#эксплуатация-в-продакшене-и-миграции)
    - [Сценарии](#сценарии)
    - [Проектирование архитектуры](#проектирование-архитектуры)
    - [Разное](#разное-3)

## Упражнения

### IAM

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Создание пользователя | IAM | [Упражнение](exercises/create_user/exercise.md) | [Решение](exercises/create_user/solution.md) | |
| Политика паролей | IAM | [Упражнение](exercises/password_policy_and_mfa/exercise.md) | [Решение](exercises/password_policy_and_mfa/solution.md) | |
| Создание роли | IAM | [Упражнение](exercises/create_role/exercise.md) | [Решение](exercises/create_role/solution.md) | |
| Отчёт об учётных данных (Credential Report) | IAM | [Упражнение](exercises/credential_report/exercise.md) | [Решение](exercises/credential_report/solution.md) | |
| Access Advisor | IAM | [Упражнение](exercises/access_advisor/exercise.md) | [Решение](exercises/access_advisor/solution.md) | |

### EC2

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Запуск веб-экземпляра EC2 | EC2 | [Упражнение](exercises/launch_ec2_web_instance/exercise.md) | [Решение](exercises/launch_ec2_web_instance/solution.md) | |
| Группы безопасности (Security Groups) | EC2 | [Упражнение](exercises/security_groups/exercise.md) | [Решение](exercises/security_groups/solution.md) | |
| Роли IAM | EC2, IAM | [Упражнение](exercises/ec2_iam_roles/exercise.md) | [Решение](exercises/ec2_iam_roles/solution.md) | |
| Spot-экземпляры | EC2 | [Упражнение](exercises/create_spot_instances/exercise.md) | [Решение](exercises/create_spot_instances/solution.md) | |
| Elastic IP | EC2, сети | [Упражнение](exercises/elastic_ip/exercise.md) | [Решение](exercises/elastic_ip/solution.md) | |
| Создание групп размещения | EC2, Placement Groups | [Упражнение](exercises/placement_groups/exercise.md) | [Решение](exercises/placement_groups/solution.md) | |
| Эластичные сетевые интерфейсы | EC2, ENI | [Упражнение](exercises/elastic_network_interfaces/exercise.md) | [Решение](exercises/elastic_network_interfaces/solution.md) | |
| Гибернация экземпляра | EC2 | [Упражнение](exercises/hibernate_instance.md) | [Решение](exercises/hibernate_instance/solution.md) | |
| Создание тома | EC2, EBS | [Упражнение](exercises/ebs_volume_creation/exercise.md) | [Решение](exercises/ebs_volume_creation/solution.md) | |
| Снимки (Snapshots) | EC2, EBS | [Упражнение](exercises/snapshots/exercise.md) | [Решение](exercises/snapshots/solution.md) | |
| Создание AMI | EC2, AMI | [Упражнение](exercises/create_ami/exercise.md) | [Решение](exercises/create_ami/solution.md) | |
| Создание EFS | EC2, EFS | [Упражнение](exercises/create_efs/exercise.md) | [Решение](exercises/create_efs/solution.md) | |

### S3

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Создание бакетов | S3 | [Упражнение](exercises/s3/new_bucket/exercise.md) | [Решение](exercises/s3/new_bucket/solution.md)
| Политика жизненного цикла бакета | S3, Lifecycle Policy |  | 
### ELB

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Application Load Balancer | ELB, ALB | [Упражнение](exercises/app_load_balancer/exercise.md) | [Решение](exercises/app_load_balancer/solution.md) | |
| Несколько целевых групп | ELB, ALB | [Упражнение](exercises/alb_multiple_target_groups/exercise.md) | [Решение](exercises/alb_multiple_target_groups/solution.md) | |
| Network Load Balancer | ELB, NLB | [Упражнение](exercises/network_load_balancer/exercise.md) | [Решение](exercises/network_load_balancer/solution.md) | |

### Auto Scaling Groups

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Основы Auto Scaling Groups | ASG | [Упражнение](exercises/auto_scaling_groups_basics/exercise.md) | [Решение](exercises/auto_scaling_groups_basics/solution.md) | |
| Политика динамического масштабирования | ASG, политики | [Упражнение](exercises/asg_dynamic_scaling_policy/exercise.md) | [Решение](exercises/asg_dynamic_scaling_policy/solution.md) | |

### VPC

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Мой первый VPC | VPC | [Упражнение](exercises/new_vpc/exercise.md) | [Решение](exercises/new_vpc/solution.md) | |
| Подсети | VPC | [Упражнение](exercises/subnets/exercise.md) | [Решение](exercises/subnets/solution.md) | |

### Базы данных

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| MySQL DB | RDS | [Упражнение](exercises/mysql_db/exercise.md) | [Решение](exercises/mysql_db/solution.md) | |
| Aurora DB | RDS | [Упражнение](exercises/aurora_db/exercise.md) | [Решение](exercises/aurora_db/solution.md) | |
| ElastiCache | ElastiCache | [Упражнение](exercises/elasticache/exercise.md) | [Решение](exercises/elasticache/solution.md) | |

### DNS

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
Регистрация домена | Route 53 | [Упражнение](exercises/register_domain/exercise.md) | [Решение](exercises/register_domain/solution.md) | |
Создание записей | Route 53 | [Упражнение](exercises/creating_records/exercise.md) | [Решение](exercises/creating_records/solution.md) | |
Проверки состояния (Health Checks) | Route 53 | [Упражнение](exercises/health_checks/exercise.md) | [Решение](exercises/health_checks/solution.md) | |
Failover | Route 53 | [Упражнение](exercises/route_53_failover/exercise.md) | [Решение](exercises/route_53_failover/solution.md) | |

### Контейнеры

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Задача ECS | ECS, Fargate | [Упражнение](exercises/ecs_task/exercise.md) | [Решение](exercises/ecs_task/solution.md) | |

### Lambda

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Функция Hello | Lambda | [Упражнение](exercises/hello_function/exercise.md) | [Решение](exercises/hello_function/solution.md) | |
| Функция по URL | Lambda | [Упражнение](exercises/url_function/exercise.md) | [Решение](exercises/url_function/solution.md) | |
| Веб-приложение с БД | Lambda, DynamoDB | [Упражнение](exercises/web_app_dynamodb/exercise.md) | [Решение](exercises/web_app_dynamodb/solution.md) | |

### Elastic Beanstalk

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Простое приложение Node.js в Elastic Beanstalk | Elastic Beanstalk | [Упражнение](exercises/elastic_beanstalk_simple/exercise.md) | [Решение](exercises/elastic_beanstalk_simple/solution.md) | |

### CodePipeline

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Простой CI с S3 | CodePipeline & S3 | [Упражнение](exercises/basic_s3_ci/exercise.md) | [Решение](exercises/basic_s3_ci/solution.md) | |

### CDK

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Пример CDK | CDK | [Упражнение](exercises/sample_cdk/exercise.md) | [Решение](exercises/sample_cdk/solution.md) | |
### Разное

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Настройка бюджета | Бюджет | [Упражнение](exercises/budget_setup/exercise.md) | [Решение](exercises/budget_setup/solution.md) | |
| Нет приложения :'( | Устранение неполадок | [Упражнение](exercises/no_application/exercise.md) | [Решение](exercises/no_application/solution.md) | |

## Вопросы

### Глобальная инфраструктура

<details>
<summary>Объясните следующие понятия:

  * Зона доступности (Availability zone)
  * Регион (Region)
  * Периферийное расположение (Edge location)</summary><br><b>

Регионы AWS — это центры обработки данных, размещённые в разных географических точках по всему миру.<br>

Внутри каждого региона есть несколько изолированных площадок, называемых зонами доступности (Availability Zones). Каждая зона доступности — это один или несколько дата-центров с резервированием сети, связи и электропитания. Несколько зон доступности обеспечивают высокую доступность на случай, если одна из них выйдет из строя.<br>

Edge locations — по сути, сеть доставки контента (CDN), которая кэширует данные и обеспечивает меньшую задержку и более быструю доставку пользователям в любой точке. Они расположены в крупных городах мира.
</b></details>

<details>
<summary>Верно или неверно? Каждый регион AWS спроектирован так, чтобы быть полностью изолированным от других регионов AWS </summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно или неверно? В каждом регионе минимум 1 зона доступности, а максимум — 4</summary><br><b>

Неверно. Минимум — 2, максимум — 6.
</b></details>

<details>
<summary>Что учитывать при выборе региона AWS для запуска нового приложения?</summary><br><b>

* Доступность сервисов: не все сервисы (и не все их функции) доступны в каждом регионе
* Меньшая задержка: развёртывать приложение в регионе, близком к клиентам
* Соответствие требованиям (compliance): в некоторых странах действуют более строгие правила и требования, например, чтобы данные оставались в пределах страны или региона. В таком случае для запуска приложения можно использовать только определённый регион
* Цены: цены могут различаться между регионами, поэтому один и тот же сервис в разных регионах может стоить по-разному.
</b></details>

### IAM

<details>
<summary>Что такое IAM? Каковы некоторые его возможности?</summary><br><b>

Коротко — он используется для управления пользователями, группами, политиками доступа и ролями
Полное объяснение можно найти [здесь](https://aws.amazon.com/iam)
</b></details>

<details>
<summary>Верно или неверно? Конфигурация IAM определяется глобально, а не для каждого региона</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? При создании аккаунта AWS по умолчанию создаётся root-аккаунт. Именно его рекомендуется использовать и раздавать в организации</summary><br><b>

Неверно. Вместо root-аккаунта нужно создавать пользователей и работать под ними.
</b></details>

<details>
<summary>Верно или неверно? Группы в AWS IAM могут содержать только пользователей, но не другие группы</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? Пользователь в AWS IAM может состоять только в одной группе</summary><br><b>

Неверно. Пользователи могут состоять в нескольких группах.
</b></details>

<details>
<summary>Каковы лучшие практики работы с IAM в AWS?</summary><br><b>

* Удалить ключи доступа root-аккаунта и не использовать root-аккаунт регулярно
* Создавать пользователя IAM для каждого реального человека. Не делить пользователей между людьми.
* Применять «принцип наименьших привилегий» (least privilege principle): давать пользователям только те разрешения, которые им нужны, и не более того.
* Настроить MFA и рассмотреть возможность сделать её обязательной
* Использовать группы для назначения разрешений ( user -> group -> permissions )
</b></details>

<details>
<summary>Какие разрешения есть у нового пользователя?</summary><br><b>

Только доступ для входа.
</b></details>

<details>
<summary>Верно или неверно? Если пользователь в AWS аутентифицируется по паролю, ему не нужно включать MFA</summary><br><b>

Неверно(!). MFA — отличный дополнительный уровень безопасности при аутентификации.
</b></details>

<details>
<summary>Какие есть способы доступа к AWS?</summary><br><b>

  * AWS Management Console
  * AWS CLI
  * AWS SDK
</b></details>

<details>
<summary>Что такое роли (Roles)?</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html): «Роль IAM — это идентичность IAM, которую можно создать в своём аккаунте и которая имеет определённые разрешения... это идентичность AWS с политиками разрешений, определяющими, что эта идентичность может и чего не может делать в AWS.»
Например, можно использовать роль, которая разрешает сервису EC2 обращаться к бакетам s3 (чтение и запись).
</b></details>

<details>
<summary>Что такое политики (Policies)?</summary><br><b>

Политики — это документы, которые задают разрешения: что может делать пользователь, группа или роль. Их формат — JSON.
</b></details>

<details>
<summary>Пользователь не может получить доступ к бакету s3. В чём может быть проблема?</summary><br><b>

Причин может быть несколько. Одна из них — отсутствие политики. Чтобы это исправить, администратор должен привязать к пользователю политику, разрешающую доступ к бакету s3.
</b></details>

<details>
<summary>Что использовать, чтобы:

  - Предоставить доступ между двумя сервисами/ресурсами?
  - Предоставить пользователю доступ к ресурсам/сервисам?</summary><br><b>

  * Роль
  * Политику
</b></details>

<details>
<summary>Из каких операторов (statements) состоят политики AWS IAM?</summary><br><b>

* Sid: идентификатор оператора (необязательно)
* Effect: разрешить или запретить доступ
* Action: список действий (которые запрещаются или разрешаются)
* Resource: список ресурсов, к которым применяются действия
* Principal: роль, аккаунт или пользователь, к которому применяется политика
* Condition: условия, определяющие, когда применяется политика (необязательно)
</b></details>

<details>
<summary>Объясните следующую политику:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect:": "Allow",
            "Action": "*",
            "Resources": "*"
        }
    ]
}
```
</summary><br><b>

Эта политика разрешает выполнять любое действие над любым ресурсом. Это и есть политика "AdministratorAccess".
</b></details>

<details>
<summary>Какие инструменты безопасности предоставляет AWS IAM?</summary><br><b>

* IAM Credentials Report: список всех пользователей аккаунта и состояние их учётных данных
* IAM Access Advisor: показывает разрешения на сервисы, выданные пользователю, и сведения о том, когда он последний раз обращался к этим сервисам
</b></details>

<details>
<summary>Какой инструмент использовать для оптимизации разрешений пользователя путём выявления сервисов, к которым он обращается нерегулярно (или не обращается вовсе)?</summary><br><b>

IAM Access Advisor
</b></details>

<details>
<summary>Какой тип объекта IAM использовать, чтобы разрешить взаимодействие между сервисами?</summary><br><b>

Роль
</b></details>
### EC2

<details>
<summary>Что такое EC2?</summary><br><b>

«веб-сервис, предоставляющий безопасные масштабируемые вычислительные мощности в облаке».
Подробнее [здесь](https://aws.amazon.com/ec2)
</b></details>

<details>
<summary>Верно или неверно? EC2 — региональный сервис</summary><br><b>

Верно. В отличие, например, от IAM, который является глобальным сервисом, EC2 — региональный сервис.
</b></details>

<details>
<summary>Какие свойства/параметры конфигурации экземпляров EC2 можно задать или изменить?</summary><br><b>

* ОС (Linux, Windows)
* RAM и CPU
* Сеть — IP, свойства сетевой карты, например скорость
* Дисковое пространство — (EBS, EFS, EC2 Instance Store)
* EC2 User Data
* Группы безопасности
</b></details>

<details>
<summary>Что использовать для настройки экземпляров EC2 — установки ПО, конфигурации ОС и т.п.?</summary><br><b>

AMI. С помощью AMI (Amazon Machine Image) можно настраивать экземпляры EC2, указывая, какое ПО установить, какие изменения ОС применить и т.д.
</b></details>

#### AMI

<details>
<summary>Что такое AMI?</summary><br><b>

Amazon Machine Images: «Amazon Machine Image (AMI) содержит информацию, необходимую для запуска экземпляра».
Подробнее [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
</b></details>

<details>
<summary>Какие существуют источники AMI?</summary><br><b>

* Собственные AMI — AMI, которые вы создаёте сами
* AWS Marketplace для AMI — AMI, созданные другими, в основном продаются за определённую цену
* Публичные AMI — предоставляются AWS
</b></details>

<details>
<summary>Верно или неверно? AMI создаются для определённого региона</summary><br><b>

Верно (но их можно копировать из одного региона в другой).
</b></details>

<details>
<summary>Опишите в общих чертах процесс создания AMI</summary><br><b>

1. Запустить экземпляр EC2
2. Настроить экземпляр EC2 (установить пакеты, изменить конфигурацию ОС и т.д.)
3. Остановить экземпляр (чтобы избежать проблем с целостностью данных)
4. Создать снимок EBS и собрать AMI
5. Чтобы проверить и протестировать AMI, запустить из него экземпляр
</b></details>

<details>
<summary>Что такое тип экземпляра (instance type)?</summary><br><b>

«указанный тип экземпляра определяет аппаратное обеспечение хост-компьютера, используемого для вашего экземпляра»
Подробнее о типах экземпляров [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
</b></details>

<details>
<summary>Объясните соглашение об именовании типов экземпляров</summary><br><b>

Возьмём для примера тип экземпляра m5.large

`m` — класс экземпляра
`5` — поколение
`large` — размер экземпляра (влияет на характеристики, например vCPU и RAM)
</b></details>

<details>
<summary>Верно или неверно? Пользователю в AWS доступны следующие типы экземпляров:

  * Compute optimized
  * Network optimized
  * Web optimized</summary><br><b>

Неверно. Из этого списка доступен только compute optimized.
</b></details>

<details>
<summary>Объясните каждый из следующих типов экземпляров:

  * "Compute Optimized"
  * "Memory Optimized"
  * "Storage Optimized"</summary><br><b>

Compute Optimized:

* Используется для вычислительно ёмких задач
* Оснащён высокопроизводительными процессорами
* Сценарии разнообразны: игровые серверы, машинное обучение, пакетная обработка и т.д.

Memory Optimized:

* Используется для обработки больших наборов данных в памяти
* Другие сценарии: высокая производительность, базы данных, распределённые кэши

Storage Optimized:

* Используется для задач, интенсивно работающих с хранилищем, — много операций чтения и записи больших наборов данных
* Сценарии: базы данных, OLTP-системы, распределённые файловые системы
</b></details>

<details>
<summary>Что можно подключить к экземпляру EC2 для хранения данных?</summary><br><b>

EBS
</b></details>

#### EBS

<details>
<summary>Объясните, что такое Amazon EBS</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html): «предоставляет тома блочного хранилища для использования с экземплярами EC2. Тома EBS ведут себя как сырые неформатированные блочные устройства.»
</b></details>

<details>
<summary>Что происходит с томами EBS при завершении (termination) экземпляра?</summary><br><b>

По умолчанию корневой том помечается на удаление, а остальные тома сохраняются.<br>
Можно управлять тем, что произойдёт с каждым томом при завершении.
</b></details>

<details>
<summary>Что происходит с диском EC2 (EBS) при остановке экземпляра?</summary><br><b>

Диск остаётся нетронутым и может использоваться после запуска экземпляра.
</b></details>

<details>
<summary>Верно или неверно? Тома EBS привязаны к определённой зоне доступности</summary><br><b>

Верно
</b></details>

<details>
<summary>Объясните, что такое снимки EBS (EBS Snapshots)</summary><br><b>

Снимки EBS используются для создания резервной копии тома EBS на определённый момент времени.
</b></details>

<details>
<summary>Для чего используются снимки EBS?</summary><br><b>

* Резервные копии данных
* Перенос данных между AZ
</b></details>

<details>
<summary>Можно ли подключить один и тот же том EBS к нескольким экземплярам EC2?</summary><br><b>

Да, с помощью multi-attach можно подключить один том EBS к нескольким экземплярам.
</b></details>

<details>
<summary>Верно или неверно? EBS — сетевой диск, поэтому ему нужно сетевое подключение</summary><br><b>

Верно
</b></details>

<details>
<summary>Какие типы томов EBS существуют?</summary><br><b>

* HDD (st 1, sc 1): недорогие тома HDD
* SSD
  * io1, io2: SSD с наивысшей производительностью
  * gp2, gp3: SSD общего назначения
</b></details>

<details>
<summary>Какой тип тома EBS выбрать для нагрузок с низкой задержкой?</summary><br><b>

SSD - io1, io2
</b></details>

<details>
<summary>Какой тип тома EBS выбрать для нагрузок, которым нужна хорошая производительность, но при этом важна и стоимость?</summary><br><b>

SSD - gp2, gp3
</b></details>

<details>
<summary>Какой тип тома EBS выбрать для высокой пропускной способности?</summary><br><b>

SSD - io1, io2
</b></details>

<details>
<summary>Какой тип тома EBS выбрать для редкого доступа к данным?</summary><br><b>

HDD - sc1
</b></details>

<details>
<summary>Какие типы томов EBS можно использовать как загрузочные тома для экземпляров EC2?</summary><br><b>

SSD: gp2, gp3, io1, io2
</b></details>

<details>
<summary>Верно или неверно? У тома EBS типа gp2 IP растёт при увеличении размера диска</summary><br><b>

Верно.
</b></details>

#### Instance Store

<details>
<summary>Что использовать, если к EC2 нужно подключить аппаратный диск вместо сетевого (EBS)?</summary><br><b>

EC2 Instance Store.
</b></details>

<details>
<summary>Объясните, что такое EC2 Instance Store. Почему его могут предпочесть другим вариантам?</summary><br><b>

EC2 instance store обеспечивает более высокую производительность ввода-вывода по сравнению с EBS.<br>
В основном используется для кэша и временных данных.
</b></details>

<details>
<summary>Есть ли недостатки у instance store по сравнению с EBS?</summary><br><b>

Да, данные в instance store теряются при остановке экземпляров.
</b></details>

#### EFS

<details>
<summary>Что такое Amazon EFS?</summary><br><b>

[Документация AWS](https://aws.amazon.com/efs): «Amazon Elastic File System (Amazon EFS) предоставляет простую, масштабируемую, полностью управляемую эластичную файловую систему NFS для использования с облачными сервисами AWS и локальными (on-premises) ресурсами.»

Проще говоря, это сетевая файловая система, которую можно смонтировать на одном или нескольких экземплярах EC2.
</b></details>

<details>
<summary>Верно или неверно? EFS привязана к одной зоне доступности</summary><br><b>

Неверно. EFS можно монтировать в нескольких зонах доступности.
</b></details>

<details>
<summary>Каковы сценарии использования EFS?</summary><br><b>

* Совместное использование данных (например, разработчики, работающие с одной системой контроля версий)
* Веб-хостинг
* Управление контентом
</b></details>

<details>
<summary>Верно или неверно? EFS совместима только с AMI на базе Linux</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? EFS требует от пользователя планирования ёмкости, так как не масштабируется автоматически</summary><br><b>

Неверно. EFS масштабируется автоматически, а оплата идёт по факту использования (pay-per-use).
</b></details>

<details>
<summary>Какие режимы EFS существуют?</summary><br><b>

* Performance mode
  * General purpose: используется в основном для CMS, веб-хостинга, ... так как оптимален для приложений, чувствительных к задержке
  * Max I/O: отлично подходит для масштабирования до высокой пропускной способности и большого числа операций ввода-вывода в секунду
* Throughput mode
  * Bursting: пропускная способность масштабируется в зависимости от размера ФС
  * Provisioned: фиксированная пропускная способность
</b></details>

<details>
<summary>Какой режим EFS выбрать для обработки медиа?</summary><br><b>

Performance Mode (Max I/O): обеспечивает высокую пропускную способность и масштабируется по числу операций в секунду. В основном используется для big data, обработки медиа и т.д.
</b></details>

<details>
<summary>Какой режим EFS используется по умолчанию?</summary><br><b>

Performance Mode (General Purpose): используется для веб-хостинга, CMS, ... всего, что чувствительно к задержке.
</b></details>

<details>
<summary>Какие классы хранения (storage tiers) есть в EFS?</summary><br><b>

* Standard: файлы с частым доступом
* Infrequent access: хранение файлов дешевле, но их извлечение тоже стоит денег
</b></details>

#### Модели ценообразования

<details>
<summary>Какие модели ценообразования EC2 существуют?</summary><br><b>

On Demand — фиксированная почасовая/посекундная оплата без обязательств. Экземпляр можно создать и завершить в любой момент.
Reserved — резервирование ёмкости, по сути покупка экземпляра на фиксированный срок. Чем дольше срок, тем дешевле.
Spot — позволяет предложить любую цену за экземпляры или платить спотовую цену.
Dedicated Hosts — физический сервер EC2, выделенный для вашего использования.
</b></details>

<details>
<summary>Верно или неверно? Reserved-экземпляр нужно использовать минимум 1 год</summary><br><b>

Верно.
</b></details>

<details>
<summary>Объясните следующие типы reserved-экземпляров:

  * Convertible Reserved Instances
  * Scheduled Reserved Instances</summary><br><b>

* Convertible Reserved Instances: используются для длительных нагрузок, когда тип экземпляра может измениться в течение срока резервирования
* Scheduled Reserved Instances: когда экземпляр нужно зарезервировать на долгий срок, но он нужен не постоянно (например, только по утрам)
</b></details>

<details>
<summary>Верно или неверно? В EC2 On Demand оплата почасовая при использовании Linux или Windows и посекундная (после первой минуты) для любой другой операционной системы</summary><br><b>

Неверно. Оплата посекундная (после первой минуты) при использовании Windows или Linux и почасовая для любой другой ОС.
</b></details>

<details>
<summary>Нужен экземпляр на короткий срок, и нагрузка на нём не должна прерываться. Какую модель ценообразования выбрать?</summary><br><b>

On Demand хорошо подходит для краткосрочных непрерываемых нагрузок (но и стоит дороже всего).
</b></details>

<details>
<summary>Нужен экземпляр для непрерывной работы приложения в течение 2 лет без смены типа экземпляра. Какую модель ценообразования выбрать?</summary><br><b>

Reserved-экземпляры: они дешевле on-demand, и экземпляр принадлежит вам в течение выбранного срока.
</b></details>

<details>
<summary>Какая модель ценообразования потенциально даёт наибольшую скидку и в чём её преимущество</summary><br><b>

Spot-экземпляры дают наибольшую скидку, но у них есть недостаток — риск потерять их из-за более высокой ставки.
</b></details>

<details>
<summary>Экземпляр нужен на два года, но только с 10:00 до 15:00 каждый день. Какую модель ценообразования выбрать?</summary><br><b>

Reserved-экземпляры типа "Scheduled Reserved Instances", которые позволяют резервировать определённое временное окно (например, 10:00-15:00 каждый день).
</b></details>

<details>
<summary>Нужен экземпляр для запуска нагрузок. Неважно, если они в какой-то момент упадут, лишь бы в итоге выполнились. Какую модель ценообразования выбрать?</summary><br><b>

Spot-экземпляры. Потенциальная скидка самая высокая по сравнению со всеми остальными моделями. Недостаток в том, что экземпляр можно потерять в любой момент, поэтому запускать стоит только нагрузки, внезапный сбой которых допустим.
</b></details>

<details>
<summary>Нужен физический сервер только для вашего использования. Какую модель ценообразования выбрать?</summary><br><b>

EC2 Dedicated Host
</b></details>

<details>
<summary>Чем отличаются dedicated hosts и dedicated instances?</summary><br><b>

В dedicated hosts оплата идёт за хост, больше прозрачности (сокеты, ядра, ...) и можно управлять размещением экземпляров.<br>
В dedicated instances оплата идёт за экземпляр, но размещением управлять нельзя и нет информации о сокетах, ядрах, ...
</b></details>

<details>
<summary>В каких случаях полезны EC2 dedicated hosts?</summary><br><b>

* Требования соответствия (compliance)
* Когда лицензия ПО сложная (Bring Your Own License) и не поддерживает облако или мультиарендность (multi-tenants)
* Регуляторные требования
</b></details>

<details>
<summary>Что такое группы безопасности (Security Groups)?</summary><br><b>

«Группа безопасности действует как виртуальный файрвол, управляющий трафиком одного или нескольких экземпляров»
Подробнее на эту тему [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
</b></details>

<details>
<summary>Верно или неверно? Группы безопасности содержат только запрещающие правила</summary><br><b>

Неверно. Группы безопасности содержат только разрешающие правила.
</b></details>

<details>
<summary>Верно или неверно? Одну группу безопасности можно подключить к нескольким экземплярам</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? Группы безопасности не привязаны к региону и VPC (т.е. при смене региона не нужно создавать новую)</summary><br><b>

Неверно. Они привязаны к регионам и VPC.
</b></details>

<details>
<summary>Верно или неверно? По умолчанию при использовании групп безопасности весь входящий трафик к экземпляру EC2 блокируется, а весь исходящий разрешён</summary><br><b>

Верно
</b></details>

<details>
<summary>В чём преимущество ссылок на группы безопасности из другой группы безопасности?</summary><br><b>

Представьте экземпляр, который ссылается на две группы безопасности и разрешает входящий трафик от них.<br>
Теперь представьте два экземпляра, каждый из которых использует одну из групп безопасности, на которые ссылается упомянутый экземпляр. Это значит, что трафик от этих двух экземпляров будет приниматься, поскольку они используют группы безопасности, на которые ссылается экземпляр из начала примера. IP-адреса указывать не нужно.
</b></details>

<details>
<summary>Как перенести экземпляр в другую зону доступности?</summary><br><b>
</b></details>

<details>
<summary>Что можно подключить к экземпляру EC2 для хранения данных?</summary><br><b>

EBS
</b></details>

<details>
<summary>Какие типы reserved-экземпляров EC2 существуют?</summary><br><b>

Standard RI — наибольшая скидка + подходит для стабильной нагрузки
Convertible RI — скидка + возможность менять атрибуты RI + подходит для стабильной нагрузки
Scheduled RI — запуск в зарезервированных временных окнах

Подробнее о EC2 RI [здесь](https://aws.amazon.com/ec2/pricing/reserved-instances)
</b></details>

<details>
<summary>На какой срок можно зарезервировать reserved-экземпляры?</summary><br><b>

1 или 3 года.
</b></details>

<details>
<summary>Что позволяет управлять входящим и исходящим трафиком экземпляра?</summary><br><b>

Группы безопасности (Security Groups)
</b></details>

<details>
<summary>Что означает bootstrapping и как его использовать в AWS EC2?</summary><br><b>

Bootstrapping — это выполнение команд при первом запуске машины.
В AWS EC2 это делается с помощью скрипта EC2 user data.
</b></details>

<details>
<summary>При попытке обратиться к приложению, работающему на экземпляре EC2, возникает тайм-аут. Назовите одну возможную причину</summary><br><b>

Неправильно настроена группа безопасности.
</b></details>

<details>
<summary>Что такое AWS Instance Connect?</summary><br><b>

[AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html): «Amazon EC2 Instance Connect предоставляет простой и безопасный способ подключения к экземплярам Linux по Secure Shell (SSH).»
</b></details>

<details>
<summary>Вы пытаетесь выполнить команды EC2 на только что созданном экземпляре EC2, но они завершаются ошибкой из-за отсутствия учётных данных. Что делать?</summary><br><b>

НЕ настраивать учётные данные AWS на экземпляре (иначе любой другой пользователь вашего аккаунта сможет видеть и использовать ваши учётные данные).<br>
Лучшая практика — привязать роль IAM с достаточными разрешениями (например, `IAMReadOnlyAccess`)
</b></details>

<details>
<summary>Верно или неверно? Отмена запроса Spot-экземпляра завершает экземпляр</summary><br><b>

Неверно. Отмена запроса Spot-экземпляра не завершает созданные им экземпляры.<br>
Чтобы завершить такие экземпляры, сначала нужно отменить запрос Spot-экземпляра.
</b></details>

<details>
<summary>Что такое Spot Fleets?</summary><br><b>

Набор Spot-экземпляров и, при желании, также on-demand экземпляров.
</b></details>

<details>
<summary>Какие существуют стратегии выделения Spot-экземпляров?</summary><br><b>

* lowestPrice: запускать экземпляры из пула с самой низкой ценой
* diversified: распределять по всем пулам
* capacityOptimized: оптимизировать по количеству экземпляров
</b></details>

<details>
<summary>Что с точки зрения сети вы получаете по умолчанию при запуске экземпляра EC2?</summary><br><b>

Приватный IP и публичный IP.
</b></details>

<details>
<summary>Объясните, что такое гибернация EC2 (EC2 hibernate)</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html: «Гибернация сохраняет содержимое памяти экземпляра (RAM) на корневой том Amazon Elastic Block Store (Amazon EBS).»
</b></details>

<details>
<summary>Верно или неверно? Использование гибернации EC2 ускоряет загрузку экземпляра</summary><br><b>

Верно. Это связано с тем, что операционная система не перезапускается и не останавливается.
</b></details>

<details>
<summary>Каковы сценарии использования гибернации EC2?</summary><br><b>

* Сохранить состояние RAM
* Сервис с долгой инициализацией
* Сохранить долго работающие процессы
</b></details>

<details>
<summary>Каковы ограничения гибернации EC2?</summary><br><b>

* Размер RAM экземпляра ограничен
* Корневой том должен быть зашифрованным EBS
* Время гибернации ограничено
* Поддерживаются не все типы экземпляров
* Нет поддержки bare metal. Только On-Demand и Reserved-экземпляры
* Поддерживаются не все AMI
</b></details>

<details>
<summary>Объясните, что такое EC2 Nitro</summary><br><b>

* Новое поколение экземпляров EC2 на новой технологии виртуализации
* Улучшенный EBS: 64 000 EBS IOPS
* Улучшенная сеть: HPC, IPv6
* Улучшенная безопасность
</b></details>

<details>
<summary>Какие возможности настройки CPU есть в EC2?</summary><br><b>

* Изменение количества ядер CPU (полезно для приложений с большим объёмом RAM и низкой нагрузкой на CPU)
* Изменение количества потоков на ядро (полезно для нагрузок HPC)
</b></details>

<details>
<summary>Объясните, что такое EC2 Capacity Reservations</summary><br><b>

* Позволяет гарантировать наличие ёмкости EC2, когда она нужна
* Обычно сочетается с Reserved Instances и Saving Plans для экономии затрат
</b></details>

#### Launch Template

<details>
<summary>Что такое шаблон запуска (launch template)?</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html): «Можно создать шаблон запуска, содержащий информацию о конфигурации для запуска экземпляра. Шаблоны запуска позволяют хранить параметры запуска, чтобы не указывать их каждый раз при запуске экземпляра»
</b></details>

<details>
<summary>Чем Launch Configuration отличается от Launch Template?</summary><br><b>

Launch configuration — устаревшая форма Launch Template, которую нужно пересоздавать каждый раз, когда требуется обновить конфигурацию.

Кроме того, у launch template есть явные преимущества:
  * Создание как On-Demand, так и Spot-экземпляров
  * поддержка нескольких версий
  * поддержка создания подмножеств параметров (для повторного использования и наследования)
</b></details>

#### ENI

<details>
<summary>Объясните, что такое Elastic Network Interfaces (ENI)</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html): «Эластичный сетевой интерфейс — это логический сетевой компонент в VPC, представляющий виртуальную сетевую карту.»
</b></details>

<details>
<summary>Назовите как минимум три атрибута, которые могут быть у Elastic Network Interfaces (ENI)</summary><br><b>

1. Один публичный IPv4-адрес
2. MAC-адрес
3. Основной приватный IPv4-адрес (из диапазона адресов вашего VPC)
</b></details>

<details>
<summary>Верно или неверно? ENI не привязаны к определённой зоне доступности</summary><br><b>

Неверно. ENI привязаны к определённой зоне доступности.
</b></details>

<details>
<summary>Верно или неверно? ENI можно создавать независимо от экземпляров EC2</summary><br><b>

Верно. Их можно подключить позже и на лету (для целей отказоустойчивости).
</b></details>

#### Placement Groups

<details>
<summary>Что такое группы размещения (Placement Groups)?</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html): «При запуске нового экземпляра EC2 сервис EC2 пытается разместить его так, чтобы все ваши экземпляры были распределены по базовому оборудованию для минимизации коррелированных сбоев. С помощью групп размещения можно влиять на размещение группы взаимозависимых экземпляров в соответствии с потребностями вашей нагрузки.»
</b></details>

<details>
<summary>Какие стратегии групп размещения существуют?</summary><br><b>

* Cluster: размещает экземпляры близко друг к другу в одной AZ.
* Spread: распределяет экземпляры по оборудованию
* Partition: распределяет экземпляры по разным разделам (= разным наборам оборудования/стоек) внутри AZ
</b></details>

<details>
<summary>Для каждого из следующих сценариев выберите стратегию группы размещения:

  * Высокая доступность — главный приоритет
  * Низкая задержка между экземплярами
  * Экземпляры должны быть изолированы друг от друга
  * Big Data-приложения, учитывающие разделы (partition aware)
  * Big Data-процесс, который должен быстро завершиться</summary><br><b>

  * Высокая доступность — главный приоритет - Spread
  * Низкая задержка между экземплярами - Cluster
  * Экземпляры должны быть изолированы друг от друга - Spread
  * Big Data-приложения, учитывающие разделы - Partition
  * Big Data-процесс, который должен быстро завершиться - Cluster
</b></details>

<details>
<summary>Каковы минусы и плюсы стратегии группы размещения "Cluster"?</summary><br><b> 

Минусы: при отказе оборудования отказывают все экземпляры
Плюсы: сеть с низкой задержкой и высокой пропускной способностью
</b></details>

<details>
<summary>Каковы минусы и плюсы стратегии группы размещения "Spread"?</summary><br><b> 

Минусы:
  * Текущее ограничение — 7 экземпляров на AZ (на группу размещения)
Плюсы:
  * Максимальная высокая доступность (экземпляры на разном оборудовании, охватывают несколько AZ)
</b></details>

### VPC

<details>
<summary>Что такое VPC?</summary><br><b>

«Логически изолированная часть облака AWS, в которой можно запускать ресурсы AWS в определяемой вами виртуальной сети»
Подробнее [здесь](https://aws.amazon.com/vpc).
</b></details>

<details>
<summary>Верно или неверно? VPC охватывает несколько регионов</summary><br><b>

Неверно
</b></details>

<details>
<summary>Верно или неверно? В одном регионе может быть несколько VPC</summary><br><b>

Верно. На сегодняшний день мягкий лимит (soft limit) — 5.
</b></details>

<details>
<summary>Верно или неверно? Подсети, принадлежащие одному VPC, могут находиться в разных зонах доступности</summary><br><b>

Верно. Уточним: одна подсеть целиком находится в одной AZ.
</b></details>

<details>
<summary>Вы заметили, что в подсетях вашего VPC (с CIDR x.x.x.x/20) доступно 4096 IP-адресов, хотя в этом CIDR должно быть 4096 адресов. В чём причина?</summary><br><b>

AWS резервирует в каждой подсети 5 IP-адресов — первые 4 и последний, поэтому они недоступны для использования.
</b></details>

<details>
<summary>Для чего AWS использует 5 зарезервированных IP-адресов?</summary><br><b>

x.x.x.0 - адрес сети
x.x.x.1 - маршрутизатор VPC
x.x.x.2 - DNS
x.x.x.3 - резерв на будущее
x.x.x.255 - широковещательный адрес
</b></details>

<details>
<summary>Что такое Internet Gateway?</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html): «компонент, обеспечивающий связь между экземплярами в вашем VPC и интернетом»

Кроме того, полезно знать, что IGW:
  * Высокодоступен и резервирован
  * Сам по себе не даёт доступа в интернет (нужно отредактировать таблицы маршрутизации)
  * Создаётся отдельно от VPC
</b></details>

<details>
<summary>Верно или неверно? К одному Internet Gateway можно подключить один или несколько VPC</summary><br><b>

Неверно. К одному IGW можно подключить только один VPC, и наоборот
</b></details>

<details>
<summary>Верно или неверно? NACL разрешает или запрещает трафик на уровне подсети</summary><br><b>

Верно
</b></details>

<details>
<summary>Что такое VPC peering?</summary><br><b>

[docs.aws](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html): «Пиринговое соединение VPC — это сетевое соединение между двумя VPC, позволяющее маршрутизировать трафик между ними с помощью приватных IPv4- или IPv6-адресов.»
</b></details>

<details>
<summary>Верно или неверно? К одному VPC можно подключить несколько Internet Gateway</summary><br><b>

Неверно. К одному VPC можно подключить только один internet gateway.
</b></details>

<details>
<summary>Вы перезапустили экземпляр EC2, и публичный IP изменился. Что сделать, чтобы этого не происходило?</summary><br><b>

Использовать Elastic IP, который даёт фиксированный IP-адрес.
</b></details>

<details>
<summary>При создании нового VPC есть параметр "Tenancy". Для чего он нужен?</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html): параметр `Tenancy` определяет, будут ли экземпляры EC2, запускаемые в VPC, работать на оборудовании, общем с другими аккаунтами AWS, или на оборудовании, выделенном только для вас. 
</b></details>

<details>
<summary>Что такое Elastic IP-адрес?</summary><br><b>

[Документация AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html): «Elastic IP-адрес — это статический IPv4-адрес, предназначенный для динамических облачных вычислений. Elastic IP-адрес выделяется вашему аккаунту AWS и принадлежит вам, пока вы его не освободите. С помощью Elastic IP-адреса можно скрыть сбой экземпляра или ПО, быстро переназначив адрес на другой экземпляр в вашем аккаунте.»
</b></details>

<details>
<summary>Зачем использовать Elastic IP-адрес?</summary><br><b>

Допустим, есть экземпляр, который нужно выключить или провести на нём обслуживание. В этом случае Elastic IP-адрес стоит перенести на другой работающий экземпляр, пока обслуживание не завершится, а затем вернуть его на исходный экземпляр (или оставить на втором).
</b></details>

<details>
<summary>Верно или неверно? При остановке и запуске экземпляра EC2 его публичный IP меняется</summary><br><b>

Верно
</b></details>

<details>
<summary>Каковы лучшие практики использования Elastic IP?</summary><br><b>

Лучшая практика — по возможности вообще их не использовать. Чаще используют балансировщик нагрузки без публичного IP или случайный публичный IP с зарегистрированной для него DNS-записью
</b></details>

<details>
<summary>Верно или неверно? Elastic IP бесплатен, пока он не связан с экземпляром EC2</summary><br><b>

Неверно. Elastic IP бесплатен, пока он **связан ** с экземпляром EC2. Этот экземпляр должен работать и иметь только один Elastic IP.
</b></details>

<details>
<summary>Верно или неверно? Таблицы маршрутизации (Route Tables) используются, чтобы разрешать или запрещать трафик из интернета к экземплярам AWS</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Объясните, что такое Security Groups и Network ACLs</summary><br><b>

* NACL — уровень безопасности на уровне подсети.
* Security Group — уровень безопасности на уровне экземпляра.

Подробнее [здесь](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) и [здесь](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
</b></details>

<details>
<summary>Что такое AWS Direct Connect?</summary><br><b>

Позволяет подключить корпоративную сеть к сети AWS.
</b></details>

<details>
<summary>Что использовать, если экземпляру EC2 нужен фиксированный публичный IP?</summary><br><b>

Elastic IP
</b></details>

<details>
<summary>Ваш коллега Кратос решил использовать подсеть /27, потому что ему нужно 29 IP-адресов для экземпляров EC2. Прав ли Кратос?</summary><br><b>

Нет. Поскольку AWS резервирует 5 IP-адресов в каждой подсети, у Кратоса будет 32-5=27 адресов, а это меньше, чем ему нужно (29).

Лучше бы Кратосу использовать подсеть размера /26, но удачи вам в попытке ему это объяснить.
</b></details>

#### VPC по умолчанию

<details>
<summary>Верно или неверно? По умолчанию у любого нового аккаунта есть VPC по умолчанию (default VPC)</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно или неверно? VPC по умолчанию не имеет подключения к интернету, и любому запущенному экземпляру EC2 назначается только приватный IP</summary><br><b>

Неверно. VPC по умолчанию имеет подключение к интернету, и любой запущенный экземпляр EC2 получает публичный IPv4-адрес.

Кроме того, любой запущенный экземпляр EC2 получает публичное и приватное DNS-имена.
</b></details>

<details>
<summary>Что из перечисленного входит в VPC по умолчанию?

* Internet gateway, подключённый к VPC по умолчанию
* Маршрут в основной таблице маршрутизации, направляющий весь трафик в internet gateway
* Публичная подсеть по умолчанию
* CIDR-блок IPv4 /16 по умолчанию</summary><br><b>

Всё перечисленное :)
</b></details>
### Lambda

<details>
<summary>Объясните, что такое AWS Lambda</summary><br><b>

Определение AWS: «AWS Lambda позволяет запускать код без создания серверов и управления ими. Вы платите только за потреблённое вычислительное время.»

Подробнее [здесь](https://aws.amazon.com/lambda)
</b></details>

<details>
<summary>Верно или неверно? В AWS Lambda плата взимается всё время, пока функция существует, независимо от того, выполняется она или нет</summary><br><b>

Неверно. Плата взимается при выполнении функции — за время выполнения и использованные вычислительные ресурсы.
</b></details>

<details>
<summary>Какой из следующих наборов языков поддерживает Lambda?

- R, Swift, Rust, Kotlin
- Python, Ruby, Go, Kotlin, Bash
- Python, Ruby, PHP, PowerShell, C#, Perl
- Python, Ruby, Go, Node.js, Groovy, C++
- Python, Ruby, Go, Node.js, PowerShell, C#
</summary><br><b>

- Python, Ruby, Go, Node.js, PowerShell, C#
</b></details>

<details>
<summary>Верно или неверно? Базовые разрешения lambda позволяют только загружать логи в Amazon CloudWatch Logs</summary><br><b>

Верно
</b></details>

<details>
<summary>В чём одна из проблем текущей архитектуры?

<img src="images/lambda/aws_lambda_direct_access.png"/>
</summary><br><b>

Пользователи не должны обращаться к AWS Lambda напрямую. Если нужно открыть функцию Lambda для пользователей, лучше настроить эндпоинт API Gateway между пользователями и функцией Lambda.

Это не только повышает безопасность, но и упрощает доступ для пользователя: он может обращаться к функции по HTTP или HTTPS.
</b></details>

<details>
<summary>Назовите один или несколько сценариев использования AWS Lambda</summary><br><b>

- Загрузка изображений в S3 и их тегирование или запись информации об изображениях в базу данных
- Загрузка видео в S3, их редактирование или добавление субтитров/подписей с сохранением результата в S3
- Использование SNS и/или SQS для запуска функций по уведомлениям или сообщениям от этих сервисов.
- Cron-задачи: использование Lambda вместе с событиями CloudWatch для периодического запуска задач/функций по расписанию.
</b></details>

<details>
<summary>В вашей архитектуре есть функция Lambda, которая загружает изображения в бакет S3 и сохраняет информацию о них в DynamoDB. Нужно открыть функцию для пользователей, чтобы они могли её вызывать. Ваш друг Карлос предлагает раскрыть пользователям учётные данные функции Lambda. Что вы об этом думаете?</summary><br><b>

Категорически нет. Нельзя давать пользователям прямой доступ к функции Lambda.

Правильный способ открыть функцию Lambda для пользователей — через эндпоинт API Gateway.
</b></details>

### Контейнеры

#### ECS

<details>
<summary>Что такое Amazon ECS?</summary><br><b>

[Документация AWS](https://aws.amazon.com/ecs): «Amazon Elastic Container Service (Amazon ECS) — полностью управляемый сервис оркестрации контейнеров. Такие клиенты, как Duolingo, Samsung, GE и Cook Pad, используют ECS для запуска своих самых чувствительных и критически важных приложений благодаря его безопасности, надёжности и масштабируемости.»

Проще говоря, он позволяет запускать контейнеры в AWS.<br>
AWS берёт на себя запуск/остановку контейнеров, а вам нужно создавать и обслуживать инфраструктуру, на которой они работают (экземпляры EC2).
</b></details>

<details>
<summary>Что нужно сделать, чтобы экземпляр EC2 стал частью кластера ECS?</summary><br><b>

Установить на него агент ECS. В некоторых AMI для этого есть встроенная конфигурация.
</b></details>

<details>
<summary>Какие типы запуска (launch types) есть в ECS?</summary><br><b>

* EC2 Instance
* AWS Fargate
</b></details>

<details>
<summary>Что такое Amazon ECR?</summary><br><b>

[Документация AWS](https://aws.amazon.com/ecr): «Amazon Elastic Container Registry (ECR) — полностью управляемый реестр контейнеров Docker, упрощающий разработчикам хранение, управление и развёртывание образов контейнеров Docker.»
</b></details>

<details>
<summary>Для чего используется роль "EC2 Instance Profile" применительно к ECS?</summary><br><b>

EC2 Instance Profile используется агентом ECS на экземпляре EC2, чтобы:

  * Выполнять вызовы API к сервису ECS
  * Отправлять логи из контейнера в CloudWatch
  * Использовать секреты, определённые в SSM Parameter Store или Secrets Manager
  * Загружать образы контейнеров из ECR (реестра)
</b></details>

<details>
<summary>Как обмениваться данными между контейнерами (часть из ECS, часть из Fargate)?</summary><br><b>

Использование EFS — хороший способ обмена данными между контейнерами, и он работает также между разными AZ.
</b></details>

#### Fargate

<details>
<summary>Что такое AWS Fargate?</summary><br><b>

[Документация Amazon](https://aws.amazon.com/fargate): «AWS Fargate — бессерверный (serverless) вычислительный движок с оплатой по мере использования, который позволяет сосредоточиться на создании приложений, не управляя серверами. AWS Fargate совместим как с Amazon Elastic Container Service (ECS), так и с Amazon Elastic Kubernetes Service (EKS)»

Проще говоря, AWS Fargate позволяет запускать контейнеры в AWS, не заботясь об управлении инфраструктурой. Он запускает контейнеры исходя из нужных CPU и RAM.
</b></details>

<details>
<summary>Чем AWS Fargate отличается от AWS ECS?</summary><br><b>

В AWS ECS инфраструктурой управляете вы — нужно создавать и настраивать экземпляры EC2.<br>
В AWS Fargate вы не создаёте и не обслуживаете инфраструктуру, а просто запускаете контейнеры Docker. Можно считать его бессерверной версией AWS ECS.
</b></details>

<details>
<summary>Верно или неверно? Fargate создаёт ENI для каждой запускаемой задачи</summary><br><b>

Верно.
</b></details>

### S3

#### Основы

<details>
<summary>Объясните, что такое AWS S3</summary><br><b>

- S3 — быстрый, масштабируемый и надёжный сервис объектного хранилища. S3 позволяет клиентам загружать, скачивать и хранить любые файлы или объекты размером до 5 TB.<br>
- S3 расшифровывается как Simple Storage Service
- Пользователю не нужно беспокоиться о файловых системах или дисковом пространстве
</b></details>

#### Бакеты 101

<details>
<summary>Что такое бакет (bucket)?</summary><br><b>

Бакет S3 — ресурс, похожий на папку в файловой системе, который позволяет хранить объекты, состоящие из данных.
</b></details>

<details>
<summary>Верно или неверно? Бакеты определяются глобально</summary><br><b>

Неверно. Они определяются на уровне региона.
</b></details>

<details>
<summary>Верно или неверно? Имя бакета должно быть глобально уникальным</summary><br><b>

Верно
</b></details>

<details>
<summary>Как переименовать бакет в S3?</summary><br><b>

Имя бакета S3 неизменяемо. Это значит, что изменить его нельзя без удаления бакета и создания нового.

Поэтому процесс переименования бакета выглядит так:

* Создать новый бакет с нужным именем
* Перенести в него данные из старого бакета
* Удалить старый бакет

С помощью AWS CLI это выглядит так:

```sh
# Создать новый бакет
aws s3 mb s3://[NEW_BUCKET_NAME]
# Синхронизировать содержимое старого бакета с новым
$ aws s3 sync s3://[OLD_BUCKET_NAME] s3://[NEW_BUCKET_NAME]
# Удалить старый бакет
$ aws s3 rb --force s3://[OLD_BUCKET_NAME]
```
</b></details>

<details>
<summary>Верно или неверно? Максимальный размер объекта, который пользователь может загрузить за один раз, — 5TB</summary><br><b>

Верно
</b></details>

<details>
<summary>Объясните, что такое "Multi-part upload"</summary><br><b>

[Документация Amazon](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html): «Составная загрузка (multipart upload) позволяет загрузить один объект как набор частей. Каждая часть — непрерывный фрагмент данных объекта... Как правило, когда размер объекта достигает 100 MB, стоит рассмотреть составную загрузку вместо загрузки объекта одной операцией.»
</b></details>

#### Объекты

<details>
<summary>Объясните, что такое "Object Versioning"</summary><br><b>

Если версионирование включено на уровне бакета, оно позволяет загружать новые версии файлов поверх предыдущих, что даёт возможность легко откатиться и защищает данные от безвозвратного удаления.
</b></details>

<details>
<summary>Объясните следующее:

  - Object Lifecycles
  - Object Sharing</summary><br><b>

  * Object Lifecycles — перенос объектов между классами хранения по заданным правилам на основе временных периодов
  * Object Sharing — предоставление доступа к объектам по URL-ссылке
</b></details>

<details>
<summary>Объясните, что такое Object Durability и Object Availability</summary><br><b>

Object Durability: вероятность (в процентах) того, что файл не будет потерян в течение года
Object Availability: доля времени (в процентах) в течение года, когда файл будет доступен
</b></details>

#### Безопасность S3

<details>
<summary>Верно или неверно? Каждый новый бакет S3 по умолчанию публичный</summary><br><b>

Неверно. Новый бакет приватный, если его не настроили как публичный.
</b></details>

<details>
<summary>Что такое presigned URL?</summary><br><b>

Поскольку каждый новый бакет по умолчанию приватный, через него нельзя делиться файлами с пользователями. Даже если загрузивший их человек попытается их просмотреть, ему будет отказано.

Presigned URL — способ обойти это и поделиться файлами с пользователями, включив учётные данные (токен) в состав URL. Это можно сделать на ограниченное время.
</b></details>

<details>
<summary>Какие меры безопасности вы применяли в контексте S3?</summary><br><b>
	* Не делать бакет публичным.
	* Включить шифрование, если оно выключено.
    * Определить политику доступа
</b></details>


<details>
<summary>Какие типы шифрования поддерживает S3?</summary><br><b>

* SSE-S3
* SSE-KMS
* SSE-C
</b></details>

<details>
<summary>Кратко опишите, как работает шифрование SSE-S3 (AES)</summary><br><b>

1. Вы загружаете файл в S3 по HTTP (или HTTPS) с заголовком
2. S3 шифрует его с помощью управляемого ключа данных
3. S3 сохраняет зашифрованный объект в бакете
</b></details>

<details>
<summary>Верно или неверно? При шифровании SSE-S3 (AES-256) ключом управляете вы</summary><br><b>

Неверно. Ключом управляет S3, а для шифрования используется алгоритм AES-256.
</b></details>

<details>
<summary>Кто или что управляет ключами при шифровании SSE-KMS?</summary><br><b>

Сервис KMS.
</b></details>

<details>
<summary>Почему можно предпочесть SSE-KMS вместо SSE-S3?</summary><br><b>

SS3-KMS даёт контроль над тем, у кого есть доступ к ключам, а также позволяет включить журнал аудита (audit trail).
</b></details>

<details>
<summary>Верно или неверно? При шифровании SSE-C ключами управляете и вы, и S3</summary><br><b>

Неверно. Ключами управляете вы. Это ключи, предоставляемые клиентом.
</b></details>

<details>
<summary>Верно или неверно? При SSE-C обязательно использовать HTTPS и передавать ключ шифрования в заголовках каждого HTTP-запроса</summary><br><b>

Верно.
</b></details>

<details>
<summary>Кратко опишите, как работает шифрование SSE-C</summary><br><b>

1. Пользователь загружает файл в S3 по HTTPS, передавая ключ данных в заголовке
2. AWS S3 выполняет шифрование с помощью переданного ключа данных, и зашифрованный объект сохраняется в бакете

Чтобы получить объект, пользователю нужно будет передать тот же ключ данных.
</b></details>

<details>
<summary>С какой строки начинается заголовок?

* x-zmz
* x-amz
* x-ama
</summary><br><b>

x-amz
</b></details>

#### Разное

<details>
<summary>Что такое класс хранения (storage class)? Какие классы хранения существуют?</summary><br><b>

Каждому объекту назначается класс хранения, влияющий на его доступность и надёжность (durability). Он также влияет на стоимость.
Классы хранения, доступные сегодня:
  * Standard:
    * Используется для хранения общего назначения (в основном данных, к которым нужен частый доступ)
    * Самый дорогой класс хранения
    * Надёжность 11x9%
    * Доступность 2x9%
    * Класс хранения по умолчанию

  * Standard-IA (Infrequent Access)
    * Долгоживущие данные с редким доступом, которые при обращении должны быть доступны немедленно
    * Надёжность 11x9%
    * Доступность 99.90%

  * One Zone-IA (Infrequent Access):
    * Долгоживущие некритичные данные с редким доступом
    * Дешевле классов Standard и Standard-IA
    * Надёжность 2x9%
    * Доступность 99.50%

  * Intelligent-Tiering:
    * Долгоживущие данные с меняющимся или неизвестным характером доступа. По сути, в этом классе данные автоматически перемещаются в наиболее подходящий класс в зависимости от характера использования
    * Цена зависит от используемого класса
    * Надёжность 11x9%
    * Доступность 99.90%

  * Glacier: архивные данные со временем извлечения от минут до часов
  * Glacier Deep Archive: архивные данные, к которым обращаются редко или никогда, со временем извлечения в часах
  * И Glacier, и Glacier Deep Archive:
    * Самые дешёвые классы хранения
    * имеют надёжность 9x9%

Подробнее о классах хранения [здесь](https://aws.amazon.com/s3/storage-classes)
</b></details>

<details>
<summary>Клиент хочет перенести редко используемые данные из класса хранения standard в самый дешёвый класс. Какой класс хранения выбрать?

  * One Zone-IA
  * Glacier Deep Archive
  * Intelligent-Tiering</summary><br><b>

Glacier Deep Archive
</b></details>

<details>
<summary>Какие варианты извлечения данных из Glacier доступны пользователю?</summary><br><b>

Expedited, Standard и Bulk
</b></details>

<details>
<summary>Верно или неверно? Каждый аккаунт AWS может хранить до 500 петабайт данных. Любой дополнительный объём стоит вдвое дороже</summary><br><b>

Неверно. Ёмкость не ограничена.
</b></details>

<details>
<summary>Объясните, что такое Storage Gateway</summary><br><b>

«AWS Storage Gateway — гибридный облачный сервис хранения, дающий локальный (on-premises) доступ к практически неограниченному облачному хранилищу».
Подробнее о Storage Gateway [здесь](https://aws.amazon.com/storagegateway)
</b></details>

<details>
<summary>Объясните следующие типы развёртывания Storage Gateway

  * File Gateway
  * Volume Gateway
  * Tape Gateway</summary><br><b>

Подробно объясняется [здесь](https://aws.amazon.com/storagegateway/faqs)
</b></details>

<details>
<summary>Чем stored volumes отличаются от cached volumes?</summary><br><b>

Stored Volumes — данные находятся в дата-центре клиента и периодически резервируются в AWS
Cached Volumes — данные хранятся в облаке AWS и кэшируются в дата-центре клиента для быстрого доступа
</b></details>

<details>
<summary>Что такое "Amazon S3 Transfer Acceleration"?</summary><br><b>

Определение AWS: «Amazon S3 Transfer Acceleration обеспечивает быструю, простую и безопасную передачу файлов на большие расстояния между клиентом и бакетом S3»

Подробнее [здесь](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)
</b></details>

<details>
<summary>Объясните, что такое согласованность данных (data consistency)</summary><br><b>
	S3 Data Consistency обеспечивает строгую согласованность чтения после записи (read-after-write) для запросов PUT и DELETE к объектам в бакете S3 во всех регионах AWS. S3 всегда возвращает последнюю версию файла.
</b></details>

<details>
<summary>Можно ли размещать в S3 динамические сайты? А статические?</summary><br><b>
	Нет. S3 поддерживает только статические сайты. На статическом сайте отдельные веб-страницы содержат статический контент. Они также могут содержать клиентские скрипты. Динамический же сайт опирается на обработку на стороне сервера, включая серверные скрипты на PHP, JSP или ASP.NET. Amazon S3 не поддерживает серверные скрипты.
</b></details>

### Аварийное восстановление

<details>
<summary>Что такое RTO и RPO применительно к аварийному восстановлению (disaster recovery)?</summary><br><b>

RTO — максимально допустимое время, в течение которого приложение может быть недоступно.

RPO — максимально допустимый период, за который данные приложения могут быть потеряны в результате инцидента.
</b></details>

<details>
<summary>Какие методы аварийного восстановления поддерживает AWS?</summary><br><b>

* The Cold Method — периодическое резервное копирование и отправка копий на внешнюю площадку<br>
* Pilot Light — данные зеркалируются в постоянно работающее окружение
* Warm Standby — работающая уменьшенная версия продакшен-окружения
* Multi-site — дублированное окружение, работающее постоянно
</b></details>

<details>
<summary>У какого варианта аварийного восстановления самый большой простой, а у какого — самый маленький?</summary><br><b>

Самый маленький — Multi-site
Самый большой — The cold method
</b></details>

### CloudFront

<details>
<summary>Объясните, что такое CloudFront</summary><br><b>

Определение AWS: «Amazon CloudFront — быстрый сервис сети доставки контента (CDN), который безопасно доставляет данные, видео, приложения и API клиентам по всему миру с низкой задержкой и высокой скоростью передачи в удобной для разработчиков среде.»

Подробнее о CloudFront [здесь](https://aws.amazon.com/cloudfront)
</b></details>

<details>
<summary>Объясните следующие понятия:

  * Origin
  * Edge location
  * Distribution</summary><br><b>
</b></details>

<details>
<summary>Какие способы доставки доступны пользователю с CDN?</summary><br><b>
</b></details>

<details>
<summary>Верно или неверно? Объекты кэшируются на время жизни TTL</summary><br><b>

Верно
</b></details>

<details>
<summary>Что такое AWS Snowball?</summary><br><b>

Транспортное решение, предназначенное для переноса больших объёмов данных (петабайтного масштаба) в облако AWS и из него.
</b></details>

<details>
<summary> Как компании обеспечить продолжение работы веб-приложения, если оно станет недоступным в текущем единственном регионе?</summary><br><b>
Развернуть приложение в нескольких регионах. Использовать проверки состояния DNS в Amazon Route 53 для направления трафика в работоспособный регион
</b></details>

### ELB

<details>
<summary>Что такое ELB (Elastic Load Balancing)?</summary><br><b>

[Документация AWS](https://aws.amazon.com/elasticloadbalancing): «Elastic Load Balancing автоматически распределяет входящий трафик приложений между несколькими целями, такими как экземпляры Amazon EC2, контейнеры, IP-адреса и функции Lambda.»
</b></details>

<details>
<summary>Верно или неверно? Elastic Load Balancer — управляемый ресурс (= о нём заботится AWS)</summary><br><b>

Верно. AWS отвечает за работоспособность ELB и берёт на себя операции жизненного цикла, такие как обновления, обслуживание и высокая доступность.
</b></details>

<details>
<summary>Какие типы балансировщиков нагрузки есть в AWS?</summary><br><b>

* Classic Load Balancer (CLB): в основном для TCP (уровень 4) и HTTP, HTTPS (уровень 7)
* Application Load Balancer (ALB): в основном для HTTP, HTTPS и WebSocket
* Network Load Balancer (NLB): в основном для TCP, TLS и UDP
* Gateway Load Balancer (GWLB): в основном для операций уровня 3 (протокол IP)
</b></details>

<details>
<summary>Что такое "listener" применительно к ELB?</summary><br><b>
</b></details>

<details>
<summary>Что такое "target group" применительно к ELB?</summary><br><b>
</b></details>

<details>
<summary>Какой балансировщик нагрузки использовать для сервисов с трафиком HTTP или HTTPS?</summary><br><b>

Application Load Balancer (ALB).
</b></details>

<details>
<summary>Каковы сценарии использования Gateway Load Balancer?</summary><br><b>

* Обнаружение вторжений (Intrusion Detection)
* Файрвол
* Изменение полезной нагрузки (payload)
</b></details>

<details>
<summary>Объясните, что такое "health checks" в контексте AWS ELB</summary><br><b>

Проверки состояния используются ELB, чтобы проверить, корректно ли работают экземпляры EC2.<br>
Если проверки не проходят, ELB перестаёт направлять трафик на тот экземпляр EC2, на котором они не прошли.
</b></details>

<details>
<summary>Верно или неверно? Проверки состояния AWS ELB выполняются по порту и маршруту</summary><br><b>

Верно.

Например, порт `2017` и эндпоинт `/health`.
</b></details>

<details>
<summary>Какие типы балансировщиков нагрузки поддерживаются в EC2 и для чего они используются?</summary><br><b>

* Application LB — трафик уровня 7<br>
* Network LB — сверхвысокая производительность или статический IP-адрес (уровень 4)<br>
* Classic LB — низкая стоимость, подходит для тестовых окружений или окружений разработки (выведен из эксплуатации к 15 августа 2022 г.)<br>
* Gateway LB — прозрачный сетевой шлюз, распределяющий трафик на такие системы, как файрволы, системы обнаружения и предотвращения вторжений и системы глубокой инспекции пакетов. (уровень 3)<br>
</b></details>

<details>
<summary>Какой тип балансировщика нагрузки AWS используется на следующей схеме?<br>
<img src="../../images/aws/identify_load_balancer.png"/>
</summary><br><b>

Application Load Balancer (маршрутизация по разным эндпоинтам + используется HTTP).
</b></details>

<details>
<summary>Какие целевые группы возможны для ALB (Application Load Balancer)?</summary><br><b>

* Задачи EC2
* Экземпляры ECS
* Функции Lambda
* Приватные IP-адреса
</b></details>

<details>
<summary>Верно или неверно? ALB может маршрутизировать только в одну группу маршрутов</summary><br><b>

Неверно. ALB может маршрутизировать в несколько целевых групп.
</b></details>

<details>
<summary>Для анализа сетевого трафика используется `____ load balancer`</summary><br><b>

Gateway Load Balancer
</b></details>

<details>
<summary>У кого меньше задержка: у Application Load Balancer или Network Load Balancer?</summary><br><b>

У Network Load Balancer (~100 мс), тогда как у ALB задержка ~400 мс
</b></details>

<details>
<summary>Верно или неверно? У Network load balancer один статический IP на каждую зону доступности</summary><br><b>

Верно.
</b></details>

<details>
<summary>Какие целевые группы поддерживает network load balancer?</summary><br><b>

* Экземпляр EC2
* IP-адреса
* Application Load Balancer
</b></details>

<details>
<summary>Какие целевые группы поддерживает gateway load balancer?</summary><br><b>

* Экземпляр EC2
* IP-адреса (только приватные)
</b></details>

<details>
<summary>Назовите один сценарий использования application load balancer в качестве целевой группы для network load balancer</summary><br><b>

Может понадобиться фиксированный IP-адрес (NLB) и при этом перенаправление HTTP-трафика по пути, параметрам запроса, ..., что затем делает ALB
</b></details>

<details>
<summary>Каковы сценарии использования Network Load Balancer?</summary><br><b>

* Трафик TCP, UDP
* Экстремальная производительность
</b></details>

<details>
<summary>Верно или неверно? Network load balancer работает на уровне 4</summary><br><b>

Верно. Он перенаправляет трафик TCP, UDP.
</b></details>

<details>
<summary>Верно или неверно? Для network load balancer можно включить sticky session, чтобы один и тот же клиент всегда направлялся на один и тот же экземпляр</summary><br><b>

Неверно. Это поддерживается только в Classic Load Balancer и Application Load Balancer.
</b></details>

<details>
<summary>Объясните, что такое Cross Zone Load Balancing</summary><br><b>

При межзональной балансировке нагрузки (cross zone load balancing) трафик равномерно распределяется между всеми (зарегистрированными) экземплярами во всех зонах доступности.
</b></details>

<details>
<summary>Верно или неверно? Для network load balancer межзональная балансировка всегда включена и не может быть отключена </summary><br><b>

Неверно. По умолчанию она отключена
</b></details>

<details>
<summary>Верно или неверно? При межзональной балансировке AWS берёт плату за передачу данных между AZ в network load balancer, но не в application load balancer</summary><br><b>

Верно. Плата за передачу данных между AZ взимается в network load balancer, но не в application load balancer
</b></details>

<details>
<summary>Верно или неверно? И ALB, и NLB поддерживают несколько listener с несколькими SSL-сертификатами </summary><br><b>

Верно
</b></details>

<details>
<summary>Объясните, что такое Deregistration Delay (или Connection Draining) применительно к ELB</summary><br><b>

Период времени или процесс «осушения» (draining) экземпляров от запросов/трафика (по сути, дать завершиться всем активным соединениям, но не открывать новые), чтобы в итоге экземпляр можно было снять с регистрации и ELB больше не отправлял на него запросы/трафик.
</b></details>

#### NLB

<details>
<summary>На каком сетевом уровне работает Network Load Balancer?</summary><br><b>

Уровень 4
</b></details>

#### ALB

<details>
<summary>Верно или неверно? С ALB (Application Load Balancer) можно выполнять маршрутизацию по строке запроса и/или заголовкам</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно или неверно? Для application load balancer межзональная балансировка всегда включена и не может быть отключена</summary><br><b>

Верно
</b></details>

### Auto Scaling Group

<details>
<summary>Объясните, что такое Auto Scaling Group</summary><br><b>

[Документация Amazon](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html): «Auto Scaling group содержит набор экземпляров Amazon EC2, которые рассматриваются как логическая группа для целей автоматического масштабирования и управления. Auto Scaling group также позволяет использовать функции Amazon EC2 Auto Scaling, такие как замена по результатам проверки состояния и политики масштабирования»
</b></details>

<details>
<summary>В составе ASG работают два экземпляра. Вы меняете желаемую ёмкость (desired capacity) на 1. К чему это приведёт?</summary><br><b>

Один из экземпляров будет завершён.
</b></details>

<details>
<summary>Как настроить триггер для масштабирования auto scaling group вниз/вверх (scale in/out)?</summary><br><b>

Один из способов — использовать алармы CloudWatch: аларм отслеживает метрику, и при определённом значении (или диапазоне) можно выбрать масштабирование ASG вниз или вверх.
</b></details>

<details>
<summary>Какие метрики/правила используются для автомасштабирования</summary><br><b>

* Входящий/исходящий сетевой трафик (Network In/Out)
* Количество запросов к ELB на экземпляр
* Средняя загрузка CPU, использование RAM
</b></details>

<details>
<summary>Что такое политика динамического масштабирования (dynamic Scaling policy) применительно к Auto Scaling Groups?</summary><br><b>

Политика, при которой масштабирование происходит автоматически на основе различных метрик.

Есть 3 типа:

1. Target Tracking Scaling: масштабирование при изменении базового значения (например, CPU выше 60%)
2. Step Scaling: более детальное масштабирование, при котором для разных значений метрик можно выбрать разные действия (например, когда CPU меньше 20% — удалить один экземпляр, когда CPU выше 40% — добавить 3 экземпляра)
3. Scheduled Actions: заранее заданное масштабирование на определённый период (например, добавлять экземпляры по понедельникам с 10:00 до 11:00)
</b></details>

<details>
<summary>Что такое политика предиктивного масштабирования (predictive scaling policy) применительно к Auto Scaling Groups?</summary><br><b>

Масштабирование на основе анализа исторической нагрузки и планирование масштабирования по прогнозу нагрузки.
</b></details>

<details>
<summary>Объясните, что такое периоды ожидания масштабирования (scaling cooldowns) применительно к Auto Scaling Groups</summary><br><b>

Во время периода ожидания ASG не завершает и не запускает дополнительные экземпляры. Период ожидания наступает после операции масштабирования, и причина такого поведения в том, что перед следующей операцией масштабирования нужно собрать метрики и дать им стабилизироваться.
</b></details>

<details>
<summary>Объясните политику завершения экземпляров ASG по умолчанию</summary><br><b>

1. Находится AZ с наибольшим количеством экземпляров EC2
2. Если количество экземпляров > 1, выбирается экземпляр с самой старой launch configuration или шаблоном, и он завершается
</b></details>

<details>
<summary>Верно или неверно? По умолчанию ASG старается сбалансировать количество экземпляров между AZ</summary><br><b>

Верно, поэтому при завершении экземпляров выбирается AZ с наибольшим их количеством.
</b></details>

<details>
<summary>Объясните, что такое Lifecycle hooks применительно к Auto Scaling Groups</summary><br><b>

Lifecycle hooks позволяют выполнить дополнительные шаги до того, как экземпляр начнёт обслуживать запросы (в состоянии pending), или до его завершения (в состоянии terminating).
</b></details>

<details>
<summary>Вы используете ASG и хотите выполнить дополнительные шаги до того, как экземпляр начнёт обслуживать запросы. Что использовать? </summary><br><b>

Lifecycle hooks в состоянии pending.
</b></details>

<details>
<summary>Опишите один способ проверить, что ASG действительно работает</summary><br><b>

На экземплярах Linux можно установить пакет 'stress' и запустить stress, чтобы нагрузить систему на определённое время, и посмотреть, сработает ли ASG, добавив ёмкость (= больше экземпляров).

Например: `sudo stress --cpu 100 --timeout 20`
</b></details>

### Безопасность

<details>
<summary>Что такое модель общей ответственности (shared responsibility model)? За что отвечает AWS, а за что пользователь согласно этой модели?</summary><br><b>

Модель общей ответственности определяет, за что отвечает клиент, а за что — AWS.

Подробнее о модели общей ответственности [здесь](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Верно или неверно? Согласно модели общей ответственности, Amazon отвечает за физические CPU и группы безопасности на экземплярах</summary><br><b>

Неверно. Amazon отвечает за оборудование на своих площадках, но не за группы безопасности, которые создаются и управляются пользователями.
</b></details>

<details>
<summary>Объясните, что такое "Shared Controls" применительно к модели общей ответственности</summary><br><b>

Определение AWS: «применяются как к уровню инфраструктуры, так и к уровню клиента, но в совершенно разных контекстах или ракурсах. В общем контроле AWS предоставляет требования к инфраструктуре, а клиент должен обеспечить собственную реализацию контроля при использовании сервисов AWS»

Подробнее [здесь](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Что такое программа соответствия AWS (AWS compliance program)?</summary><br><b>
</b></details>

<details>
<summary>Как защитить экземпляры в AWS?</summary><br><b>

  * У ролей IAM экземпляров должны быть минимально необходимые разрешения. Нельзя допустить, чтобы инцидент на уровне экземпляра превратился в инцидент на уровне аккаунта
  * Использовать "AWS System Manager Session Manager" для SSH
  * Использовать для экземпляров последние образы ОС
</b></details>

<details>
<summary>Что такое AWS Artifact?</summary><br><b>

Определение AWS: «AWS Artifact — ваш основной центральный ресурс для важной для вас информации о соответствии требованиям. Он предоставляет доступ по запросу к отчётам AWS о безопасности и соответствии, а также к отдельным онлайн-соглашениям.»

Подробнее [здесь](https://aws.amazon.com/artifact)
</b></details>

<details>
<summary>Что такое AWS Inspector?</summary><br><b>

Определение AWS: «Amazon Inspector — автоматизированный сервис оценки безопасности, помогающий повысить безопасность и соответствие требованиям приложений, развёрнутых в AWS. Amazon Inspector автоматически оценивает приложения на предмет уязвимостей, незащищённости и отклонений от лучших практик.»"

Подробнее [здесь](https://aws.amazon.com/inspector)
</b></details>

<details>
<summary>Что такое AWS Guarduty?</summary><br><b>
Определение AWS: «Amazon GuardDuty — сервис обнаружения угроз, который непрерывно отслеживает вредоносную активность и несанкционированное поведение, чтобы защитить ваши аккаунты Amazon Web Services, нагрузки и данные, хранящиеся в Amazon S3» <br>
Отслеживает VPC Flow lows, логи DNS, события CloudTrail S3 и события CloudTrail Mgmt.
</b></details>

<details>
<summary>Что такое AWS Shield?</summary><br><b>

Определение AWS: «AWS Shield — управляемый сервис защиты от распределённых атак типа «отказ в обслуживании» (DDoS), защищающий приложения, работающие в AWS.»
</b></details>

<details>
<summary>Что такое AWS WAF? Приведите пример его использования и опишите, с какими ресурсами или сервисами его можно использовать</summary><br><b>
</b></details>

<details>
<summary>Для чего используется AWS VPN?</summary><br><b>
</b></details>

<details>
<summary>Чем Site-to-Site VPN отличается от Client VPN?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS CloudHSM?</summary><br><b>

Определение Amazon: «AWS CloudHSM — облачный аппаратный модуль безопасности (HSM), позволяющий легко генерировать и использовать собственные ключи шифрования в облаке AWS.»

Подробнее [здесь](https://aws.amazon.com/cloudhsm)
</b></details>

<details>
<summary>Верно или неверно? AWS Inspector может выполнять как сетевые проверки, так и проверки хостов</summary><br><b>

Верно
</b></details>

<details>
<summary>Что такое AWS Key Management Service (KMS)?</summary><br><b>

Определение AWS: «KMS упрощает создание криптографических ключей и управление ими, а также контроль их использования в широком спектре сервисов AWS и в ваших приложениях.»
Подробнее о KMS [здесь](https://aws.amazon.com/kms)
</b></details>

<details>
<summary>Что такое AWS Acceptable Use Policy?</summary><br><b>

Она описывает запрещённые способы использования веб-сервисов, предлагаемых AWS.
Подробнее об AWS Acceptable Use Policy [здесь](https://aws.amazon.com/aup)
</b></details>

<details>
<summary>Верно или неверно? Пользователю запрещено проводить тестирование на проникновение (penetration testing) любых сервисов AWS</summary><br><b>

Неверно. Для некоторых сервисов, например EC2, CloudFront и RDS, тестирование на проникновение разрешено.
</b></details>

<details>
<summary>Верно или неверно? DDoS-атака — пример разрешённого тестирования на проникновение</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Верно или неверно? AWS Access Key — разновидность MFA-устройства для защиты ресурсов AWS</summary><br><b>

Неверно. Пример MFA-устройства — ключ безопасности (security key).
</b></details>

<details>
<summary>Что такое Amazon Cognito?</summary><br><b>

Определение Amazon: «Amazon Cognito обеспечивает аутентификацию и авторизацию пользователей для ваших веб- и мобильных приложений.»

Подробнее [здесь](https://docs.aws.amazon.com/cognito/index.html)
</b></details>

<details>
<summary>Что такое AWS ACM?</summary><br><b>

Определение Amazon: «AWS Certificate Manager — сервис, позволяющий легко создавать, управлять и развёртывать публичные и приватные сертификаты Secure Sockets Layer/Transport Layer Security (SSL/TLS) для использования с сервисами AWS и вашими внутренними подключёнными ресурсами.»

Подробнее [здесь](https://aws.amazon.com/certificate-manager)
</b></details>

### Базы данных

#### RDS

<details>
<summary>Что такое AWS RDS?</summary><br><b>

* Relational Database Service
* Управляемый сервис БД (подключиться к машине по ssh нельзя)
* Поддерживает несколько СУБД: MySQL, Oracle, Aurora (собственная разработка AWS), ...
</b></details>

<details>
<summary>Зачем использовать AWS RDS вместо запуска экземпляра EC2 с установленной на нём базой данных?</summary><br><b>

AWS RDS — управляемый сервис, т.е. создание и установка патчей выполняются автоматически.

Кроме того, он предоставляет непрерывное резервное копирование (и возможность восстановления на любой момент времени), масштабирование (как горизонтальное, так и вертикальное), панель мониторинга и реплики для чтения.
</b></details>

<details>
<summary>Что вы знаете о резервном копировании в RDS?</summary><br><b>

* Автоматические резервные копии
* Полная ежедневная резервная копия (во время окна обслуживания)
* Резервное копирование журналов транзакций каждые 5 минут
* Срок хранения можно увеличить, по умолчанию — 7 дней
</b></details>

<details>
<summary>Объясните, что такое AWS RDS Storage Auto Scaling</summary><br><b>

* Хранилище RDS может автоматически увеличиваться при нехватке места
* Пользователю нужно задать "Maximum Storage Threshold", чтобы ограничить масштабирование хранилища
* Сценарии: приложения с непредсказуемой нагрузкой
* Поддерживает несколько движков баз данных RDS
</b></details>

<details>
<summary>Объясните, что такое Amazon RDS Read Replicas</summary><br><b>

[Документация AWS](https://aws.amazon.com/rds/features/read-replicas): «Amazon RDS Read Replicas повышают производительность и надёжность экземпляров баз данных (DB) RDS. Они упрощают эластичное горизонтальное масштабирование за пределы ограничений ёмкости одного экземпляра БД для нагрузок с преобладанием чтения.»

Проще говоря, они позволяют масштабировать чтение.
</b></details>

<details>
<summary>Верно или неверно? Реплики для чтения RDS поддерживаются внутри AZ, между AZ и между регионами</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? Реплики для чтения RDS асинхронные</summary><br><b>

Верно. Так сделано, чтобы чтение было согласованным.
</b></details>

<details>
<summary>Верно или неверно? Amazon RDS поддерживает MongoDB</summary><br><b>

Неверно. RDS — реляционная база данных, а MongoDB — NoSQL БД.
</b></details>

<details>
<summary>Каковы сценарии использования реплик для чтения RDS?</summary><br><b>

Есть основное приложение, работающее с базой данных, и нужно добавить ещё одно — для логирования, аналитики, ..., — которое не должно использовать ту же базу. В этом случае создаётся экземпляр реплики для чтения, и второе приложение работает с ним.
</b></details>

<details>
<summary>Объясните, что такое RDS Multi Availability Zone</summary><br><b>

* RDS multi AZ используется в основном для аварийного восстановления
* Есть основной (master) экземпляр RDS и в другой AZ — резервный (standby) экземпляр RDS
* Данные синхронизируются между ними синхронно
* Пользователь или приложение обращается к одному DNS-имени, и при сбое основного экземпляра DNS-имя переключается на резервный, так что переключение (failover) происходит автоматически
</b></details>

<details>
<summary>Верно или неверно? Перевод AWS RDS из single AZ в multi AZ — операция с простоем (т.е. нужно остановить БД)</summary><br><b>

Неверно. Это операция без простоя = останавливать базу данных не нужно.
</b></details>

<details>
<summary>Как AWS RDS переключается из single AZ в multi AZ?</summary><br><b>

1. RDS делает снимок
2. Снимок восстанавливается на другой, резервный экземпляр RDS
3. Включается синхронизация между двумя экземплярами
</b></details>

<details>
<summary>Верно или неверно? Шифрование RDS нужно задавать при запуске</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? В RDS реплики могут быть зашифрованы, даже если основной экземпляр не зашифрован</summary><br><b>

Неверно
</b></details>

<details>
<summary>Как сделать снимки RDS зашифрованными?</summary><br><b>

* Если база данных RDS зашифрована, то и снимок зашифрован
* Если база данных RDS не зашифрована, то и снимок не зашифрован; тогда можно скопировать незашифрованный снимок, создав зашифрованную копию
</b></details>

<details>
<summary>Как зашифровать незашифрованный экземпляр RDS?</summary><br><b>

Создать копию незашифрованного экземпляра -> скопировать снимок, создав зашифрованную копию -> восстановить базу данных из зашифрованного снимка -> перевести приложение на работу со скопированным экземпляром -> удалить исходный экземпляр БД
</b></details>

<details>
<summary>Как работает IAM-аутентификация в RDS?</summary><br><b>

Например:

1. Экземпляр EC2 с помощью роли IAM выполняет вызов API для получения токена аутентификации
2. Токен с шифрованием SSL используется для доступа к экземпляру RDS

Примечание: время жизни токена — 15 минут
</b></details>

<details>
<summary>Верно или неверно? В случае RDS (не Aurora) реплики для чтения требуют изменить строку подключения SQL</summary><br><b>

Верно. Поскольку реплики для чтения добавляют эндпоинты, каждый со своим DNS-именем, нужно изменить приложение, чтобы оно обращалось к этим новым эндпоинтам и балансировало нагрузку чтения.
</b></details>

#### Aurora

<details>
<summary>Что вы знаете об Amazon Aurora?</summary><br><b>

* Реляционная база данных на основе MySQL и Postgresql.
* Собственная технология AWS
* База данных, предлагаемая пользователю по умолчанию при создании базы через RDS.
* Хранилище автоматически растёт с шагом 10 GiB
* Встроенная высокая доступность (HA) — мгновенное переключение
* Производительнее MySQL и Postgres
* Поддерживает 15 реплик (тогда как MySQL — 5)
</b></details>

<details>
<summary>Верно или неверно? Aurora хранит 4 копии данных в 2 зонах доступности</summary><br><b>

Неверно. Она хранит 6 копий в 3 зонах доступности
</b></details>

<details>
<summary>Верно или неверно? Aurora поддерживает самовосстановление (self healing), при котором повреждённые данные заменяются с помощью peer-to-peer репликации</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? Хранилище Aurora распределено (striped) по 20 томам</summary><br><b>

Неверно. По 100 томам.
</b></details>

<details>
<summary>Верно или неверно? Реплики Aurora можно масштабировать</summary><br><b>

Верно. Если экземпляры реплик для чтения исчерпали CPU, можно масштабироваться, добавив экземпляры
</b></details>

<details>
<summary>Объясните, что такое Aurora Serverless. Для каких сценариев он подходит?</summary><br><b>

* Aurora serverless — автоматическое создание экземпляров базы данных с автомасштабированием в зависимости от фактического использования
* Подходит в основном для нерегулярных или непредсказуемых нагрузок
* Оплата посекундная, поэтому в итоге может быть экономичнее
</b></details>

<details>
<summary>Для какого сценария используется Aurora multi-master?</summary><br><b>

Aurora multi-master идеально подходит, когда нужно мгновенное переключение (failover) узла записи.
</b></details>

#### DynamoDB

<details>
<summary>Что такое AWS DynamoDB?</summary><br><b>
</b></details>

<details>
<summary>Объясните функцию "Point-in-Time Recovery" в DynamoDB</summary><br><b>

Определение Amazon: «Можно создавать резервные копии таблиц Amazon DynamoDB по запросу или включить непрерывное резервное копирование с помощью восстановления на момент времени (point-in-time recovery). Подробнее о резервных копиях по запросу см. On-Demand Backup and Restore for DynamoDB.»

Подробнее [здесь](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
</b></details>

<details>
<summary>Объясните, что такое "Global Tables" в DynamoDB</summary><br><b>

Определение Amazon: «Глобальная таблица — набор из одной или нескольких таблиц-реплик, принадлежащих одному аккаунту AWS.»

Подробнее [здесь](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)
</b></details>

<details>
<summary>Что такое DynamoDB Accelerator?</summary><br><b>

Определение Amazon: «Amazon DynamoDB Accelerator (DAX) — полностью управляемый высокодоступный кэш в памяти для DynamoDB, обеспечивающий до 10-кратного прироста производительности — с миллисекунд до микросекунд...»

Подробнее [здесь](https://aws.amazon.com/dynamodb/dax)
</b></details>

#### ElastiCache

<details>
<summary>Что такое AWS ElastiCache? В каких сценариях его стоит использовать?</summary><br><b>

Amazon Elasticache — полностью управляемое хранилище данных в памяти Redis или Memcached.<br>
Отлично подходит для нагрузок с преобладанием чтения, когда частые данные/запросы кэшируются и приложения/пользователи обращаются к кэшу вместо основной базы данных.
</b></details>

<details>
<summary>Опишите порядок работы приложения, использующего кэш в AWS</summary><br><b>

1. Приложение выполняет запрос к БД. Проверяется, есть ли данные в кэше
  1. Если есть — это "cache hit", и данные берутся оттуда
  2. Если нет — это "cache miss", и данные извлекаются из базы данных
   1. Затем данные также записываются в кэш (если к ним часто обращаются), и при следующем запросе пользователя к тем же данным они могут быть получены из кэша (зависит от того, сколько прошло времени и были ли эти данные инвалидированы)
</b></details>

<details>
<summary>Как с помощью ElastiCache сделать приложение stateless (без состояния)?</summary><br><b>

Допустим, есть несколько экземпляров, на которых работает одно и то же приложение, и при каждом использовании приложение создаёт пользовательскую сессию.<br>
Эту сессию можно хранить в ElastiCache, и даже если пользователь обратится к другому экземпляру приложения, оно сможет получить сессию из ElsatiCache.
</b></details>

<details>
<summary>Нужен высокодоступный кэш с функциями резервного копирования и восстановления. Что выбрать?</summary><br><b>

ElastiCache Redis.
</b></details>

<details>
<summary>Нужен кэш с масштабируемыми репликами для чтения и поддержкой multi AZ. Что выбрать?</summary><br><b>

ElastiCache Redis.
</b></details>

<details>
<summary>Нужен кэш с поддержкой шардинга, изначально построенный на многопоточной архитектуре. Что выбрать?</summary><br><b>

ElastiCache Memcached
</b></details>

<details>
<summary>Верно или неверно? ElastiCache не поддерживает IAM-аутентификацию</summary><br><b>

Верно.
</b></details>

<details>
<summary>Какие существуют паттерны загрузки данных в кэш?</summary><br><b>

* Write Through: добавлять или обновлять данные в кэше при записи данных в БД
* Lazy Loading: кэшируются все прочитанные данные
* Session Store: хранить временные данные сессий в кэше
</b></details>

#### RedShift

<details>
<summary>Что такое AWS Redshift и чем он отличается от RDS?</summary><br><b>

облачное хранилище данных (data warehouse)
</b></details>

<details>
<summary>Что делать, если есть подозрение, что AWS Redshift работает медленно?</summary><br><b>

* Подтвердить подозрение можно в консоли AWS Redshift на графике выполняющихся запросов. Он покажет, есть ли долго выполняющиеся запросы.
* Если подтвердилось, можно запросить список выполняющихся запросов и отменить ненужные
* Проверить утечки соединений (запросить активные соединения вместе с их IP)
* Проверить блокировки таблиц и завершить ненужные блокирующие сессии
</b></details>

<details>
<summary>Что такое Amazon DocumentDB?</summary><br><b>

Определение Amazon: «Amazon DocumentDB (с совместимостью с MongoDB) — быстрый, масштабируемый, высокодоступный и полностью управляемый сервис документной базы данных, поддерживающий нагрузки MongoDB. Как документная база данных, Amazon DocumentDB упрощает хранение, запросы и индексирование данных JSON.»

Подробнее [здесь](https://aws.amazon.com/documentdb)
</b></details>

<details>
<summary>Для чего используется "AWS Database Migration Service"?</summary><br><b>
</b></details>

<details>
<summary>Какой тип хранилища использует Amazon RDS?</summary><br><b>

EBS
</b></details>


### Определите сервис

<details>
<summary>Что использовать для автоматизации развёртывания кода/ПО?</summary><br><b>

AWS CodeDeploy
</b></details>

<details>
<summary>Нужно вызывать функцию каждый раз при вводе URL в браузере. Какой сервис для этого использовать?</summary><br><b>

AWS Lambda
</b></details>

<details>
<summary>Что использовать, чтобы легко создавать похожие окружения/ресурсы AWS для разных клиентов?</summary><br><b>

CloudFormation
</b></details>

<details>
<summary>С помощью какого сервиса можно добавить регистрацию, вход и управление доступом в мобильные и веб-приложения?</summary><br><b>

Cognito
</b></details>

<details>
<summary>Какой сервис использовать для создания сайта или веб-приложения?</summary><br><b>

Lightsail
</b></details>

<details>
<summary>Какой инструмент использовать для выбора между Reserved и On-Demand экземплярами?</summary><br><b>

Cost Explorer
</b></details>

<details>
<summary>Что использовать, чтобы проверить, сколько у вас несвязанных Elastic IP-адресов?</summary><br><b>

Trusted Advisor
</b></details>

<details>
<summary>Какой сервис позволяет переносить большие объёмы (петабайты) данных в облако AWS и из него?</summary><br><b>

AWS Snowball
</b></details>

<details>
<summary>Какой сервис использовать, если нужно хранилище данных (data warehouse)?</summary><br><b>

AWS RedShift
</b></details>

<details>
<summary>Какой сервис предоставляет виртуальную сеть, выделенную для вашего аккаунта AWS?</summary><br><b>

VPC
</b></details>

<details>
<summary>Что использовать для автоматического резервного копирования приложения со слоем базы данных MySQL?</summary><br><b>

Amazon Aurora
</b></details>

<details>
<summary>Что использовать для миграции локальной (on-premise) базы данных в AWS?</summary><br><b>

AWS Database Migration Service (DMS)
</b></details>

<details>
<summary>Что использовать, чтобы выяснить, почему определённые экземпляры EC2 были завершены?</summary><br><b>

AWS CloudTrail
</b></details>

<details>
<summary>Что использовать для SQL-базы данных?</summary><br><b>

AWS RDS
</b></details>

<details>
<summary>Что использовать для NoSQL-базы данных?</summary><br><b>

AWS DynamoDB
</b></details>

<details>
<summary>Что использовать, чтобы добавить в приложение анализ изображений и видео?</summary><br><b>

AWS Rekognition
</b></details>

<details>
<summary>Какой сервис использовать для отладки и устранения проблем с производительностью приложений?</summary><br><b>

AWS X-Ray
</b></details>

<details>
<summary>Какой сервис используется для отправки уведомлений?</summary><br><b>

SNS
</b></details>

<details>
<summary>Что использовать для интерактивного выполнения SQL-запросов к S3?</summary><br><b>

AWS Athena
</b></details>

<details>
<summary>Что использовать для подготовки и объединения данных для аналитики или ML?</summary><br><b>

AWS Glue
</b></details>

<details>
<summary>Какой сервис использовать для отслеживания вредоносной активности и несанкционированного поведения в аккаунтах и нагрузках AWS?</summary><br><b>

Amazon GuardDuty
</b></details>

<details>
<summary>Какой сервис использовать для централизованного управления биллингом, доступом, соответствием требованиям и безопасностью в нескольких аккаунтах AWS?</summary><br><b>

AWS Organizations
</b></details>

<details>
<summary>Какой сервис использовать для защиты веб-приложений?</summary><br><b>

AWS WAF
</b></details>

<details>
<summary>Нужно отслеживать часть ресурсов в разных сервисах. Какой сервис для этого использовать?</summary><br><b>

CloudWatch
</b></details>

<details>
<summary>Какой сервис использовать для оценки безопасности?</summary><br><b>

AWS Inspector
</b></details>

<details>
<summary>Какой сервис использовать для создания DNS-записи?</summary><br><b>

Route 53
</b></details>

<details>
<summary>Что использовать, если нужна полностью управляемая документная база данных?</summary><br><b>

Amazon DocumentDB
</b></details>

<details>
<summary>Какой сервис использовать, чтобы добавить управление доступом (или формы регистрации и входа) в веб/мобильные приложения?</summary><br><b>

AWS Cognito
</b></details>

<details>
<summary>О каком сервисе часто говорят, что он «используется для развязки (decoupling) приложений»?</summary><br><b>

AWS SQS. Поскольку это очередь сообщений, она позволяет приложениям перейти от синхронного взаимодействия к асинхронному.
</b></details>

<details>
<summary>Какой сервис использовать, если нужна очередь сообщений?</summary><br><b>

Simple Queue Service (SQS)
</b></details>

<details>
<summary>Какой сервис использовать, если нужна управляемая защита от DDOS?</summary><br><b>

AWS Shield
</b></details>

<details>
<summary>Какой сервис использовать для хранения часто используемых данных с доступом с низкой задержкой?</summary><br><b>

ElastiCache
</b></details>

<details>
<summary>Что использовать для передачи файлов на большие расстояния между клиентом и бакетом S3?</summary><br><b>

Amazon S3 Transfer Acceleration
</b></details>

<details>
<summary>Какие сервисы участвуют в получении произвольной строки (на основе входных данных) при вводе URL в браузере?</summary><br><b>

Lambda — чтобы определить функцию, которая получает входные данные и возвращает определённую строку<br>
API Gateway — чтобы определить URL-триггер (= при вводе URL вызывается функция).
</b></details>

<details>
<summary>Какой сервис использовать для потоковой передачи данных или событий?</summary><br><b>

Kinesis
</b></details>

<details>
<summary>Какой (бесплатный) инструмент использовать для получения информации об экономии затрат?</summary><br><b>

Trusted Advisor
</b></details>

<details>
<summary>Нужен доступ из локальной (on-perm) инфраструктуры к хранилищу AWS. Что для этого использовать?</summary><br><b>

Storage Gateway
</b></details>

### DNS (Route 53)

<details>
<summary>Что такое Route 53?</summary><br><b>

[AWS Route 53](https://aws.amazon.com/route53): «Amazon Route 53 — высокодоступный и масштабируемый облачный веб-сервис системы доменных имён (DNS)...»

Некоторые возможности Route 53:
  * Регистрация доменов
  * Сервис DNS — преобразование доменных имён
  * Проверки состояния — проверка доступности приложения
  * Не функция, но его SLA — 100% доступности
</b></details>

<details>
<summary>Что означает «Route 53 — авторитетный (Authoritative) DNS»?</summary><br><b>

Клиент может обновлять DNS-записи
</b></details>

<details>
<summary>Что содержит каждая запись Route 53?</summary><br><b>

* Имя домена/поддомена (например, blipblop.com)
* Значение (например, 201.7.202.2)
* Тип записи (например, A, AAAA, MX)
* TTL: время, в течение которого запись будет кэшироваться
* Routing Policy: как отвечать на запросы
</b></details>

<details>
<summary>Какие типы DNS-записей поддерживает Route 53?</summary><br><b>

* A
* AAAA
* CNAME
* NS
* DS
* CAA
* SOA
* MX
* TXT
* SPF
* SRV
* NAPTR
* PTR
</b></details>

<details>
<summary>Что такое hosted zones?</summary><br><b>

Контейнер с записями, определяющими, как маршрутизировать трафик для домена и его поддоменов
</b></details>

<details>
<summary>Какие типы hosted zones существуют?</summary><br><b>

* Public Hosted Zones — содержат записи, определяющие маршрутизацию трафика в интернете
* Private Hosted Zones — содержат записи, определяющие маршрутизацию трафика внутри VPC
</b></details>

<details>
<summary>Чем запись CNAME отличается от записи Alias?</summary><br><b>

CNAME используется для сопоставления одного имени хоста с любым другим именем хоста, а Alias — для сопоставления имени хоста с ресурсом AWS.

Кроме того, Alias работает как для корневого домена (somedomain.com), так и для некорневого, а CNAME — только для некорневого (foo.somedomain.com)
</b></details>

<details>
<summary>Верно или неверно? Запись Alias можно настроить для DNS-имени EC2</summary><br><b>

Неверно
</b></details>

<details>
<summary>Верно или неверно? Запись Alias можно настроить для VPC interface endpoint</summary><br><b>

Верно
</b></details>

<details>
<summary>Верно или неверно? Запись Alias бывает только типа A или AAAA</summary><br><b>

Верно
</b></details>

<details>
<summary>Что такое политика маршрутизации (routing policy) в AWS Route 53?</summary><br><b>

Политика маршрутизации определяет, как Route 53 отвечает на DNS-запросы.
</b></details>

<details>
<summary>Какие политики маршрутизации есть в Route 53?</summary><br><b>

* Simple 
* Geolocation
* Failover
* Latency based
* Geoproximity
* Multi-Value Answer
* Weighted
</b></details>

<details>
<summary>Допустим, нужно направить определённый % трафика на один экземпляр, а остальной трафик — на другой. Какую политику маршрутизации выбрать?</summary><br><b>

Weighted routing policy.
</b></details>

<details>
<summary>Допустим, нужно с помощью Route 53 направить трафик на единственный источник без каких-либо других требований. Какую политику маршрутизации выбрать?</summary><br><b>

Политику маршрутизации `simple`
</b></details>

<details>
<summary>Объясните политику маршрутизации geolocation</summary><br><b>

* Маршрутизация по местоположению пользователя
* Местоположение можно указать по континенту, стране или штату США
* Рекомендуется иметь запись по умолчанию на случай, если совпадения по местоположению нет
</b></details>

<details>
<summary>Каковы сценарии использования политики маршрутизации geolocation?</summary><br><b>

* Ограничение распространения контента
* Локализация приложения
* Балансировка нагрузки
</b></details>

<details>
<summary>Объясните политику маршрутизации geoproximity</summary><br><b>

* Маршрутизация по географическому расположению ресурсов
* Смещение маршрутизации выполняется на основе значения `bias`
* Ресурсы могут быть как AWS, так и не-AWS
    * Для не-AWS ресурсов, помимо региона AWS (как для ресурсов AWS), нужно указать широту и долготу
* Для её использования нужен Route 53 traffic flow
</b></details>

<details>
<summary>Каковы сценарии использования политики маршрутизации <code>weighted</code>?</summary><br><b>

* Балансировка нагрузки между регионами
* Тестирование новых версий приложений
</b></details>

<details>
<summary>Верно или неверно? Политика маршрутизации Route 53 <code>simple</code> поддерживает как одно, так и несколько значений</summary><br><b>

Верно.

Если Route 53 возвращает несколько значений, клиент сам выбирает одно из них.
</b></details>

<details>
<summary>Верно или неверно? При маршрутизации <code>weighted</code> DNS-записи должны иметь одинаковое имя, но не одинаковый тип</summary><br><b>

Неверно. У них должны совпадать и имя, И тип.
</b></details>

<details>
<summary>Нужна политика маршрутизации, которая учитывает задержку и направляет на ресурс с наименьшей задержкой. Какую политику выбрать?</summary><br><b>

Latency-based routing policy.
</b></details>

<details>
<summary>Что произойдёт, если при политике маршрутизации <code>Weighted</code> задать всем записям вес 0?</summary><br><b>

Все записи будут использоваться одинаково.
</b></details>

<details>
<summary>Для чего используются проверки состояния (health checks) Route 53?</summary><br><b>

Автоматическое переключение DNS (failover) на основе мониторинга:

  * Другой проверки состояния
  * эндпоинта (приложение, ресурс AWS, сервер)
  * Алармов CloudWatch
</b></details>

<details>
<summary>Нужна политика маршрутизации на основе расположения ресурсов с возможностью смещать больше трафика на некоторые ресурсы. Какую выбрать?</summary><br><b>

Geoproximity routing policy
</b></details>

<details>
<summary>Объясните функцию Route 53 Traffic Flow</summary><br><b>

Это визуальный редактор для управления сложными деревьями решений маршрутизации. Он упрощает управление записями.

Конфигурацию можно сохранить (как Traffic Flow Policy) и применить к разным доменам/hosted zones. Кроме того, поддерживается версионирование
</b></details>

<details>
<summary>Что такое вычисляемые (calculated) проверки состояния?</summary><br><b>

Это объединение результатов нескольких проверок состояния в одну.
</b></details>

<details>
<summary>Каков один из возможных сценариев использования вычисляемых проверок состояния?</summary><br><b>

Проведение обслуживания сайта так, чтобы не провалились все проверки состояния.
</b></details>

<details>
<summary>Нужна политика маршрутизации на основе местоположения пользователя. Какую выбрать?</summary><br><b>

Geolocation routing policy. Она основана на местоположении пользователя.

Не путайте её с latency-based routing policy. Хотя меньшее расстояние может давать меньшую задержку, в вопросе требуется не это.
</b></details>

<details>
<summary>Верно или неверно? Route 53 Multi Value — замена ELB для тех, кому нужно более дешёвое решение</summary><br><b>

Неверно. Route 53 Multi Value не заменяет ELB. В отличие от ELB, он ориентирован на балансировку нагрузки на стороне клиента.
</b></details>

<details>
<summary>Верно или неверно? Регистратор доменов и сервис DNS — по сути одно и то же</summary><br><b>

Неверно. Сервисом DNS может быть Route 53 (где вы управляете DNS-записями), а сам домен можно купить у других поставщиков, не связанных с Amazon (например, GoDadday).
</b></details>

### SQS

<details>
<summary>Что такое Simple Queue Service (SQS)?</summary><br><b>

Определение AWS: «Amazon Simple Queue Service (SQS) — полностью управляемый сервис очередей сообщений, позволяющий развязывать и масштабировать микросервисы, распределённые системы и бессерверные приложения».

Подробнее [здесь](https://aws.amazon.com/sqs)
</b></details>

<details>
<summary>Объясните, что такое "producer" и "consumer" применительно к очереди сообщений</summary><br><b>

Producer — приложение или, в общем случае, источник, который отправляет сообщения в очередь.

Consumer — процесс или приложение, которое забирает сообщения из очереди.
</b></details>

<details>
<summary>Что означает "default retention of messages"?</summary><br><b>

Это срок хранения, в течение которого сообщение должно быть получено/обработано и удалено из очереди.

На сегодняшний день срок хранения сообщения по умолчанию — 4 дня, а максимально допустимый — 14 дней.
</b></details>

<details>
<summary>Каково ограничение на размер сообщения в SQS?

* 128KB
* 128MB
* 256KB
* 256MB</summary><br><b>

256KB
</b></details>

<details>
<summary>Верно или неверно? В очереди могут быть дублирующиеся сообщения</summary><br><b>

Верно. Это называется "at least once delivery" (доставка как минимум один раз).
</b></details>

<details>
<summary>Верно или неверно? «Потребителями» (consumers) могут быть только экземпляры EC2</summary><br><b>

Неверно. Ими могут быть функции Lambda и даже локальные (on-premise) экземпляры
</b></details>

<details>
<summary>Верно или неверно? Процессы/приложения используют из SDK API SendMessage для отправки сообщений в очередь</summary><br><b>

Верно.
</b></details>

<details>
<summary>Что означает "best effort ordering" применительно к SQS?</summary><br><b>

Это значит, что порядок сообщений в очереди может нарушаться.
</b></details>

<details>
<summary>Что такое "Delay Queue" применительно к SQS?</summary><br><b>

Это время в секундах, на которое откладывается доставка новых сообщений (уже попавших в очередь).

На сегодняшний день ограничение — 15 минут.
</b></details>

<details>
<summary>Что такое "Visibility Timeout?"</summary><br><b>

Время в секундах, в течение которого сообщение не видно потребителям.

На сегодняшний день ограничение — 12 часов
</b></details>

<details>
<summary>Приведите пример архитектуры или процесса с участием SQS, EC2 и S3</summary><br><b>

Сайт, который позволяет пользователям загружать видео и добавляет к ним субтитры:

1. Сначала пользователь загружает видео через веб-интерфейс, который загружает его в бакет S3
2. В SQS приходит сообщение с расположением видео
3. Экземпляр EC2 (или функция Lambda) начинает добавлять субтитры
4. Видео с субтитрами загружается в бакет S3
5. В SQS приходит уведомление о результате, а именно о расположении видео
</b></details>

<details>
<summary>Что такое MessageGroupID?</summary><br><b>
</b></details>

### SNS

<details>
<summary>Что такое Simply Notification Service?</summary><br><b>

Определение AWS: «высокодоступный, надёжный, безопасный, полностью управляемый сервис обмена сообщениями pub/sub, позволяющий развязывать микросервисы, распределённые системы и бессерверные приложения.»

Подробнее [здесь](https://aws.amazon.com/sns)
</b></details>

<details>
<summary>Объясните следующие понятия применительно к SNS:

  - Topics
  - Subscribers
  - Publishers</summary><br><b>

  * Topics — используются для группировки нескольких эндпоинтов
  * Subscribers — эндпоинты, в которые топики отправляют сообщения
  * Publishers — источник сообщения (событие, человек, ...)
</b></details>

<details>
<summary>Чем SNS отличается от SQS?</summary><br><b>

SNS, в отличие от SQS, работает по модели издатель/подписчик (publisher/subscriber), а SQS — по модели производитель/потребитель (Producer/Consumer).

SQS доставляет сообщение одному потребителю, а SNS отправляет сообщение нескольким подписчикам.
</b></details>

<details>
<summary>Что такое паттерн Fan-Out?</summary><br><b>

Паттерн обмена сообщениями, при котором одно сообщение отправляется нескольким получателям (часто одновременно). То есть широковещательная рассылка «один ко многим».
</b></details>

### Мониторинг и логирование

<details>
<summary>Что такое AWS CloudWatch?</summary><br><b>

Определение AWS: «Amazon CloudWatch — сервис мониторинга и наблюдаемости (observability)...»

Подробнее о CloudWatch [здесь](https://aws.amazon.com/cloudwatch)
</b></details>

<details>
<summary>Что такое AWS CloudTrail?</summary><br><b>

Определение AWS: «AWS CloudTrail — сервис, обеспечивающий управление (governance), соответствие требованиям, операционный аудит и аудит рисков вашего аккаунта AWS.»

Подробнее о CloudTrail [здесь](https://aws.amazon.com/cloudtrail)
</b></details>

### Биллинг и поддержка

<details>
<summary>Что такое Service Control Policies и к какому сервису они относятся?</summary><br><b>

К сервису AWS organizations; определение Amazon: «SCP обеспечивают централизованный контроль над максимально доступными разрешениями для всех аккаунтов вашей организации, позволяя гарантировать, что аккаунты остаются в рамках правил управления доступом вашей организации.»

Подробнее [здесь](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html)
</b></details>

<details>
<summary>Объясните модель ценообразования AWS</summary><br><b>

В основном она работает по принципу "pay-as-you-go": вы платите только за то, что используете, и тогда, когда используете.
В s3 вы платите за: 1. Объём хранимых данных 2. Выполнение запросов (PUT, POST, ...)
В EC2 стоимость зависит от варианта покупки (on-demand, spot, ...), типа экземпляра, типа AMI и используемого региона.

Подробнее о модели ценообразования AWS [здесь](https://aws.amazon.com/pricing)
</b></details>

<details>
<summary>Как оценить затраты на AWS?</summary><br><b>

* TCO calculator
* AWS simple calculator
* Cost Explorer
* AWS Budgets
* Cost Allocation Tags
</b></details>

<details>
<summary>Что входит в базовую поддержку AWS?</summary><br><b>

* Круглосуточное (24x7) обслуживание клиентов
* Trusted Advisor
* AWS personal Health Dashoard
</b></details>

<details>
<summary>Как тарифицируются экземпляры EC2?</summary><br><b>
</b></details>

<details>
<summary>Для чего используется AWS Pricing Calculator?</summary><br><b>
</b></details>

<details>
<summary>Что такое Amazon Connect?</summary><br><b>

Определение Amazon: «Amazon Connect — простой в использовании омниканальный облачный контакт-центр, помогающий компаниям обеспечивать превосходное обслуживание клиентов с меньшими затратами.»

Подробнее [здесь](https://aws.amazon.com/connect)
</b></details>

<details>
<summary>Что такое "APN Consulting Partners"?</summary><br><b>

Определение Amazon: «APN Consulting Partners — компании профессиональных услуг, которые помогают клиентам любого типа и размера проектировать, строить, мигрировать и управлять своими нагрузками и приложениями в AWS, ускоряя их переход в облако.»

Подробнее [здесь](https://aws.amazon.com/partners/consulting)
</b></details>

<details>
<summary>Что из перечисленного является типами аккаунтов AWS (и отсортировано по порядку)?

  - Basic, Developer, Business, Enterprise
  - Newbie, Intermediate, Pro, Enterprise
  - Developer, Basic, Business, Enterprise
  - Beginner, Pro, Intermediate Enterprise
  </summary><br><b>

  - Basic, Developer, Business, Enterprise
</b></details>

<details>
<summary>Верно или неверно? Регион влияет на стоимость/цены EC2</summary><br><b>

Верно. Стоимость зависит от выбранного региона.
</b></details>

<details>
<summary>Что такое "AWS Infrastructure Event Management"?</summary><br><b>

Определение AWS: «AWS Infrastructure Event Management — структурированная программа, доступная клиентам Enterprise Support (и клиентам Business Support за дополнительную плату), которая помогает планировать крупномасштабные события, такие как запуск продуктов или приложений, миграции инфраструктуры и маркетинговые мероприятия.»
</b></details>
#### AWS Organizations

<details>
<summary>Что такое "AWS Organizations"?</summary><br><b>

Определение AWS: «AWS Organizations помогает централизованно управлять вашей средой по мере роста и масштабирования нагрузок в AWS.»

Подробнее об Organizations [здесь](https://aws.amazon.com/organizations)
</b></details>

<details>
<summary>Что такое OU применительно к AWS Organizations?'</summary><br><b>

OU (Organizational Units) — способ сгруппировать несколько аккаунтов, чтобы работать с ними как с единым целым.

По умолчанию в AWS Organizations создаётся OU "Root".

Чаще всего OU формируются по функциям или общему набору средств контроля. 
</b></details>
### Автоматизация

<details>
<summary>Что такое AWS CodeDeploy?</summary><br><b>

Определение Amazon: «AWS CodeDeploy — полностью управляемый сервис развёртывания, автоматизирующий развёртывание ПО на различные вычислительные сервисы, такие как Amazon EC2, AWS Fargate, AWS Lambda, и на ваши локальные серверы.»

Подробнее [здесь](https://aws.amazon.com/codedeploy)
</b></details>

<details>
<summary>Объясните, что такое CloudFormation</summary><br><b>

Определение AWS: «AWS CloudFormation — сервис, помогающий моделировать и настраивать ресурсы Amazon Web Services, чтобы тратить меньше времени на управление ими и больше — на приложения, работающие в AWS. Вы создаёте шаблон, описывающий все нужные ресурсы AWS (например, экземпляры Amazon EC2 или экземпляры БД Amazon RDS), а CloudFormation берёт на себя их создание и настройку.»
</b></details>

<details>
<summary>Что такое AWS CDK?</summary><br><b>

Определение AWS: «AWS Cloud Development Kit (AWS CDK) — фреймворк разработки ПО с открытым исходным кодом для описания облачной инфраструктуры как кода и её создания через AWS CloudFormation. CDK даёт возможность использовать для описания инфраструктуры популярные языки программирования, такие как TypeScript, JavaScript, Python, Java, C# и Go (в Developer Preview), а AWS CDK предоставляет набор библиотек для сервисов AWS, избавляющих от необходимости писать «сырые» шаблоны CloudFormation.

Подробнее [здесь](https://aws.amazon.com/cdk)
</b></details>

### Разное

<details>
<summary>С каким сервисом AWS вы работали, который, по вашему мнению, не очень распространён?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS CloudSearch?</summary><br><b>
</b></details>

<details>
<summary>Что такое AWS Lightsail?</summary><br><b>

Определение AWS: «Lightsail — простая в использовании облачная платформа, предлагающая всё необходимое для создания приложения или сайта, плюс экономичный ежемесячный тариф.»
</b></details>

<details>
<summary>Что такое AWS Rekognition?</summary><br><b>

Определение AWS: «Amazon Rekognition упрощает добавление анализа изображений и видео в ваши приложения с помощью проверенной, хорошо масштабируемой технологии глубокого обучения, не требующей экспертизы в машинном обучении.»

Подробнее [здесь](https://aws.amazon.com/rekognition)
</b></details>

<details>
<summary>Для чего используются AWS Resource Groups?</summary><br><b>

Определение Amazon: «Группы ресурсов позволяют упорядочить ресурсы AWS. Они упрощают управление и автоматизацию задач для большого числа ресурсов одновременно. »

Подробнее [здесь](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
</b></details>

<details>
<summary>Что такое AWS Global Accelerator?</summary><br><b>

Определение Amazon: «AWS Global Accelerator — сервис, повышающий доступность и производительность ваших приложений для локальных или глобальных пользователей...»

Подробнее [здесь](https://aws.amazon.com/global-accelerator)
</b></details>

<details>
<summary>Что такое AWS Config?</summary><br><b>

Определение Amazon: «AWS Config — сервис, позволяющий оценивать, проверять и анализировать конфигурации ваших ресурсов AWS.»

Подробнее [здесь](https://aws.amazon.com/config)
</b></details>

<details>
<summary>Что такое AWS X-Ray?</summary><br><b>

Определение AWS: «AWS X-Ray помогает разработчикам анализировать и отлаживать продакшен-приложения, в том числе распределённые, например построенные на микросервисной архитектуре.»
Подробнее [здесь](https://aws.amazon.com/xray)
</b></details>

<details>
<summary>Что такое AWS OpsWorks?</summary><br><b>

Определение Amazon: «AWS OpsWorks — сервис управления конфигурациями, предоставляющий управляемые экземпляры Chef и Puppet.»

Подробнее [здесь](https://aws.amazon.com/opsworks)
</b></details>

<details>
<summary>Что такое AWS Snowmobile?</summary><br><b>

«AWS Snowmobile — сервис передачи данных эксабайтного масштаба, используемый для переноса экстремально больших объёмов данных в AWS.»

Подробнее [здесь](https://aws.amazon.com/snowmobile)
</b></details>

<details>
<summary>Что такое AWS Athena?</summary><br><b>

«Amazon Athena — интерактивный сервис запросов, упрощающий анализ данных в Amazon S3 с помощью стандартного SQL.»

Подробнее об AWS Athena [здесь](https://aws.amazon.com/athena)
</b></details>

<details>
<summary>Что такое Amazon Cloud Directory?</summary><br><b>

Определение Amazon: «Amazon Cloud Directory — высокодоступное мультиарендное (multi-tenant) хранилище на основе каталогов в AWS. Эти каталоги автоматически масштабируются до сотен миллионов объектов по мере необходимости приложениям.»

Подробнее [здесь](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
</b></details>

<details>
<summary>Что такое AWS Elastic Beanstalk?</summary><br><b>

Определение AWS: «AWS Elastic Beanstalk — простой в использовании сервис для развёртывания и масштабирования веб-приложений и сервисов... Достаточно загрузить код, и Elastic Beanstalk автоматически выполнит развёртывание»

Подробнее [здесь](https://aws.amazon.com/elasticbeanstalk)
</b></details>

<details>
<summary>Что такое AWS SWF?</summary><br><b>

Определение Amazon: «Amazon SWF помогает разработчикам создавать, запускать и масштабировать фоновые задания с параллельными или последовательными шагами. Amazon SWF можно рассматривать как полностью управляемый трекер состояния и координатор задач в облаке.»

Подробнее об Amazon Simple Workflow Service [здесь](https://aws.amazon.com/swf)
</b></details>

<details>
<summary>Что такое AWS EMR?</summary><br><b>

Определение AWS: «платформа big data для обработки огромных объёмов данных с помощью инструментов с открытым исходным кодом, таких как Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi и Presto.»

Подробнее [здесь](https://aws.amazon.com/emr)
</b></details>

<details>
<summary>Что такое AWS Quick Starts?</summary><br><b>

Определение AWS: «Quick Starts создаются архитекторами решений AWS и партнёрами, чтобы помочь развернуть популярные технологии в AWS на основе лучших практик AWS по безопасности и высокой доступности.»

Подробнее [здесь](https://aws.amazon.com/quickstart)
</b></details>

<details>
<summary>Что такое Trusted Advisor?</summary><br><b>

Определение Amazon: «AWS Trusted Advisor даёт рекомендации, помогающие следовать лучшим практикам AWS. Trusted Advisor оценивает ваш аккаунт с помощью проверок. Эти проверки выявляют способы оптимизировать инфраструктуру AWS, повысить безопасность и производительность, снизить затраты и отслеживать квоты сервисов.»

Подробнее [здесь](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)

</b></details>

<details>
<summary>Что такое AWS Service Catalog?</summary><br><b>

Определение Amazon: «AWS Service Catalog позволяет организациям создавать каталоги ИТ-сервисов, одобренных для использования в AWS, и управлять ими.»

Подробнее [здесь](https://aws.amazon.com/servicecatalog)
</b></details>

<details>
<summary>Что такое AWS CAF?</summary><br><b>

Определение Amazon: «AWS Professional Services создали AWS Cloud Adoption Framework (AWS CAF), чтобы помочь организациям спроектировать и пройти ускоренный путь к успешному внедрению облака. »

Подробнее [здесь](https://aws.amazon.com/professional-services/CAF)
</b></details>

<details>
<summary>Что такое AWS Cloud9?</summary><br><b>

AWS: «AWS Cloud9 — облачная интегрированная среда разработки (IDE), позволяющая писать, запускать и отлаживать код, используя только браузер»
</b></details>

<details>
<summary>Что такое AWS CloudShell?</summary><br><b>

AWS: «AWS CloudShell — оболочка в браузере, упрощающая безопасное управление ресурсами AWS, их изучение и взаимодействие с ними.»
</b></details>

<details>
<summary>Что такое AWS Application Discovery Service?</summary><br><b>

Определение Amazon: «AWS Application Discovery Service помогает корпоративным клиентам планировать проекты миграции, собирая информацию об их локальных (on-premises) дата-центрах.»

Подробнее [здесь](https://aws.amazon.com/application-discovery)
</b></details>

<details>
<summary>Что такое AWS well-architected framework и на каких принципах (pillars) он основан?</summary><br><b>

Определение AWS: «Well-Architected Framework разработан, чтобы помочь облачным архитекторам строить безопасную, высокопроизводительную, устойчивую и эффективную инфраструктуру для своих приложений. Он основан на пяти принципах — операционное совершенство, безопасность, надёжность, эффективность производительности и оптимизация затрат»

Подробнее [здесь](https://aws.amazon.com/architecture/well-architected)
</b></details>

<details>
<summary>Какие сервисы AWS являются бессерверными (или имеют бессерверный вариант)?</summary><br><b>

AWS Lambda
AWS Athena
</b></details>

### Высокая доступность

<details>
<summary>Что означает высокая доступность с точки зрения AWS?</summary><br><b>

* Приложение/сервис работает как минимум в 2 зонах доступности
* Приложение/сервис должно пережить (= продолжить работать как обычно) аварию дата-центра
</b></details>

### Эксплуатация в продакшене и миграции

<details>
<summary>Опишите в общих чертах, как обновить систему в AWS (почти) без простоя</summary><br><b>

Один из способов — запустить новый экземпляр. Подробнее:

1. Запустить новый экземпляр
2. Установить все обновления и приложения
3. Протестировать экземпляр
4. Если все тесты прошли успешно, можно начать использовать новый экземпляр и переключиться со старого одним из нескольких способов:
  1. Перейти в route53 и обновить запись, указав IP нового экземпляра
  2. Если используется Elastic IP, перенести его на новый экземпляр
  ...
</b></details>

<details>
<summary>Вы пытаетесь использовать отключённый том EBS из us-east-1b в us-east-1a, но это не удаётся. В чём может быть причина?</summary><br><b>

Тома EBS привязаны к определённой зоне доступности. Чтобы использовать их в другой зоне доступности, нужно сделать снимок и восстановить его в целевой зоне доступности.
</b></details>

<details>
<summary>При запуске экземпляры EC2 долго загружаются из-за команд, выполняемых через user data. Как ускорить загрузку экземпляров?</summary><br><b>

Стоит создать собственный AMI, в котором команды из user data уже выполнены. Это позволит запускать экземпляры сразу.
</b></details>

<details>
<summary>Вы пытаетесь смонтировать EFS на экземпляре EC2, и это не работает (зависает...). В чём может быть причина?</summary><br><b>

К EFS не подключена группа безопасности, или в ней нет правила, разрешающего трафик NFS.
</b></details>

<details>
<summary>Как перенести том EBS в другую зону доступности?</summary><br><b>

1. Приостановить приложение
2. Сделать снимок тома EBS
3. Восстановить снимок в другой зоне доступности
</b></details>

<details>
<summary>Как зашифровать незашифрованный том EBS, подключённый к экземпляру EC2?</summary><br><b>

1. Создать снимок EBS тома
2. Скопировать снимок, отметив опцию "Encrypt"
3. Создать новый том EBS из зашифрованного снимка
</b></details>

<details>
<summary>Вы создали network load balancer, но он не работает (приложение на экземпляре EC2 недоступно). В чём может быть причина?</summary><br><b>

Отсутствует группа безопасности или она неправильно настроена.
Например, если открыть экземпляры в консоли AWS, можно увидеть, что экземпляры за NLB находятся в состоянии "unhealthy", и если для NLB не создана отдельная группа безопасности, значит, используется группа безопасности, подключённая к экземплярам EC2.

Нужно открыть группу безопасности экземпляра(ов) и разрешить трафик, который должен перенаправлять NLB (например, TCP на порт 80).
</b></details>

### Сценарии

<details>
<summary>Работает балансировщик нагрузки, за которым 5 веб-серверов. Пользователи жалуются, что при каждом переходе на новую страницу им приходится заново аутентифицироваться, а не один раз. Как это решить?</summary><br><b>


Включить sticky sessions. Так пользователь продолжит работать с одним и тем же экземпляром, а не будет перенаправляться на другой экземпляр при каждом запросе.
</b></details>

<details>
<summary>Работает балансировщик нагрузки, за которым 5 веб-серверов. Пользователи жалуются, что иногда приложение не работает. Вы выяснили, что некоторые экземпляры время от времени падают. Что делать?</summary><br><b>

Один из возможных способов — использовать проверки состояния в балансировщике нагрузки, чтобы убедиться, что экземпляры готовы к работе, прежде чем направлять на них трафик.
</b></details>

<details>
<summary>Приложение работает на 5 экземплярах EC2 в одной AZ и на 10 экземплярах EC2 в другой AZ. Трафик распределяется между всеми ними с помощью network load balancer, но похоже, что у экземпляров в одной AZ загрузка CPU выше, чем в другой. В чём может быть проблема и как её решить?</summary><br><b>

Возможно, трафик распределяется поровну между AZ, но это не значит, что он равномерно распределяется по всем экземплярам.

Чтобы равномерно распределить его между всеми экземплярами, нужно включить межзональную балансировку нагрузки (cross-zone load balancing).
</b></details>

<details>
<summary>Работает ALB, который маршрутизирует трафик по двум именам хостов: a.b.com и d.e.com. Можно ли настроить HTTPS для обоих имён хостов?</summary><br><b>

Да, с помощью SNI (Server Name Indication) у каждого приложения может быть свой SSL-сертификат (поддерживается с 2017 года).
</b></details>

<details>
<summary>Вы настроили реплики для чтения, чтобы масштабировать чтение, но пользователи жалуются, что при обновлении постов на форумах посты не обновляются. В чём может быть причина?</summary><br><b>

Реплики для чтения используют асинхронную репликацию, поэтому пользователи могут обращаться к экземпляру реплики, который ещё не синхронизирован.
</b></details>

<details>
<summary>Нужно постоянное общее хранилище для контейнеров, часть из которых работает в Fargate, а часть — в ECS. Что использовать?</summary><br><b>

EFS. Он даёт постоянное общее хранилище для контейнеров в нескольких AZ.
</b></details>

<details>
<summary>Нужно запускать задачу AWS Fargate каждый раз, когда в определённый бакет S3 загружается файл. Как это сделать?</summary><br><b>

Использовать Amazon EventBridge, чтобы при каждой загрузке файла в бакет S3 (событие) запускалась задача ECS.

У такой задачи должна быть ECS Task Role, чтобы она могла получить объект из бакета S3 (и, возможно, другие разрешения, например, если нужно обновить БД).
</b></details>

<details>
<summary>Ваши хосты довольно часто масштабируются вниз и затем снова вверх. Что вы об этом думаете? </summary><br><b>

Часто циклическое масштабирование (вниз, вверх и наоборот) — не признак того, что пороги для масштабирования вниз и вверх просто часто достигаются. В большинстве случаев это сигнал к тому, что нужно скорректировать пороги, чтобы масштабирование вниз происходило не так часто.
</b></details>

### Проектирование архитектуры

<details>
<summary>Вас попросили спроектировать архитектуру для высокопроизводительного приложения с низкой задержкой (миллионы запросов в секунду). Какой балансировщик нагрузки выбрать?</summary><br><b>

Network Load Balancer
</b></details>

<details>
<summary>Что использовать для масштабирования чтения?</summary><br><b>

Можно использовать кластер ElastiCache или RDS Read Replicas.
</b></details>

<details>
<summary>Два приложения взаимодействуют синхронно. Всё работало нормально, пока внезапно не случился всплеск трафика. Какое изменение можно применить в этом случае?</summary><br><b>

Для точного ответа не хватает деталей, но, возможно, лучше развязать приложения, введя одно из следующего:

* Модель очереди с SQS
* Модель издатель/подписчик с SNS
</b></details>

### Разное

<details>
<summary>Что такое ARN?</summary><br><b>

ARN (Amazon Resources Names) используются для уникальной идентификации различных ресурсов AWS.
Применяется, когда ресурс нужно однозначно идентифицировать во всей инфраструктуре AWS.
</b></details>

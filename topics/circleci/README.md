# Circle CI

## Вопросы по Circle CI

### Circle CI 101

<details>
<summary>Что такое Circle CI?</summary><br><b>

[Circle CI](https://circleci.com): «CircleCI — это платформа непрерывной интеграции и непрерывной доставки, которую можно использовать для внедрения практик DevOps.»
</b></details>

<details>
<summary>Каковы преимущества Circle CI?</summary><br><b>

[Документация Circle CI](https://circleci.com/docs/about-circleci): «Подключение по SSH к любому заданию для отладки проблем сборки.
Настройка параллелизма в файле .circleci/config.yml для ускорения выполнения заданий.
Настройка кэширования с помощью двух простых ключей для повторного использования данных из предыдущих заданий в workflow.
Настройка self-hosted раннеров для поддержки уникальных платформ.
Доступ к ресурсам Arm для machine executor.
Использование orbs — переиспользуемых пакетов конфигурации — для интеграции со сторонними сервисами.
Использование готовых Docker-образов для множества языков.
Использование API
 для получения информации о заданиях и workflows.
Использование CLI для локального доступа к расширенным инструментам.
Обнаружение нестабильных (flaky) тестов с помощью test insights.»
</b></details>

<details>
<summary>Объясните следующие понятия:

* Pipeline
* Workflow
* Jobs
* Steps
</summary><br><b>

* Pipeline: вся конфигурация CI/CD (.circleci/config.yaml)
* Workflow: в основном используется, когда в конфигурации больше одного задания, для оркестрации их выполнения
* Jobs: один или несколько шагов, выполняемых в рамках процесса CI/CD
* Steps: непосредственно выполняемые команды
</b></details>

<details>
<summary>Что такое Orb?</summary><br><b>

[Документация Circle CI](https://circleci.com/developer/orbs): «Orbs — это пакеты конфигурации CircleCI, которыми можно делиться и которые можно использовать для упрощения сборок» 

Они могут браться из публичного реестра или определяться приватно в рамках организации.
</b></details>

### Circle CI на практике 101

<details>
<summary>Где (в каком месте проекта) определяются pipelines Circle CI?</summary><br><b>

`.circleci/config.yml`
</b></details>

<details>
<summary>Объясните следующий файл конфигурации


```
version: 2.1

jobs:
  say-hello:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "Say hello"
          command: "echo Hello, World!"
workflows:
  say-hello-workflow:
    jobs:
      - say-hello
```
</summary><br><b>

Этот файл конфигурации создаёт одно задание, которое выполнит checkout кода проекта и запустит команду `echo Hello, World!`.
Задание будет выполняться в контейнере на основе образа `cimg/base:stable`.
</b></details>

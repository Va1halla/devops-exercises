## OpenShift

### Упражнения по OpenShift

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Проекты 101 | Проекты | [Упражнение](projects_101.md) | [Решение](solutions/projects_101.md)
| Моё первое приложение | Приложения | [Упражнение](my_first_app.md) | [Решение](solutions/my_first_app.md)

### Самопроверка по OpenShift

* [OpenShift 101](#Openshift-101)
* [Архитектура OpenShift](#Openshift-architecture)
* [Основы практической работы с OpenShift](#Openshift-hands-on-basics)
* [Проекты OpenShift](#Openshift-projects)

<a name="openshift-101"></a>
### OpenShift 101

<details>
<summary>Что такое OpenShift?</summary><br><b>

OpenShift — это платформа оркестрации контейнеров на основе Kubernetes.<br>
Её можно использовать для развёртывания приложений с минимальными накладными расходами на управление.
</b></details>

<details>
<summary>Как OpenShift связан с Kubernetes?</summary><br><b>

OpenShift построен поверх Kubernetes и, помимо встроенных ресурсов, определяет собственные пользовательские ресурсы (custom resources).
</b></details>

<details>
<summary>Верно или нет? OpenShift — это решение класса IaaS (инфраструктура как услуга)</summary><br><b>

Неверно. OpenShift — это решение класса PaaS (платформа как услуга).
</b></details>

<details>
<summary>Верно или нет? CLI OpenShift поддерживает всё, что поддерживает kubectl, а также дополнительную функциональность</summary><br><b>

Верно
</b></details>

<details>
<summary>Какие возможности OpenShift добавляет поверх Kubernetes?</summary><br><b>

- UI: OpenShift «из коробки» предоставляет единый пользовательский интерфейс
- Маршруты (Routes): простая процедура публикации сервисов
- Поддержка рабочего процесса разработчика: встроенный CI/CD (openshift pipelines), встроенный реестр контейнеров и инструменты для сборки артефактов из исходного кода в образы контейнеров
</b></details>

<details>
<summary>Верно или нет? Чтобы запускать контейнеры в OpenShift, нужны привилегии root</summary><br><b>

Неверно. OpenShift по умолчанию поддерживает контейнеры без root (rootless containers).
</b></details>

<a name="openshift-architecture"></a>
## OpenShift — архитектура

<details>
<summary>Какие типы узлов есть в OpenShift?</summary><br><b>

- Рабочие узлы (Workers): на них работают приложения конечных пользователей
- Мастер-узлы (Masters): отвечают за управление кластером
</b></details>

<details>
<summary>Какой компонент отвечает за определение размещения подов (Pod)?</summary><br><b>

Планировщик (Scheduler).
</b></details>

<details>
<summary>За что ещё, кроме размещения подов, отвечает планировщик?</summary><br><b>

За высокую доступность приложений путём распределения реплик подов между рабочими узлами
</b></details>

<a name="openshift-hands-on-basics"></a>
## OpenShift — основы практической работы

<details>
<summary>OpenShift поддерживает множество ресурсов. Как получить список всех этих ресурсов?</summary><br><b>

`oc api-resources`
</b></details>

<details>
<summary>Объясните, что такое CLI OpenShift, например <code>oc</code> и <code>odo</code></summary><br><b>

oc используется для создания приложений, а также для администрирования кластера OpenShift<br>
odo используется исключительно для управления приложениями в OpenShift (в основном с точки зрения разработчиков) и не имеет отношения к администрированию кластера
</b></details>

<a name="openshift-projects"></a>
## OpenShift — проекты

<details>
<summary>Что такое проект (project) в OpenShift?</summary><br><b>

Проект в OpenShift — это пространство имён (namespace) Kubernetes с аннотациями.<br>
Проще говоря, это изолированная среда, в которой пользователи управляют своими ресурсами и упорядочивают их (например, Pods, Deployments, Service и т.д.).
</b></details>

<details>
<summary>Как вывести список всех проектов? Что означает столбец "STATUS" в выводе списка проектов?</summary><br><b>

`oc get projects` выведет список всех проектов. По столбцу "STATUS" можно увидеть, какие проекты сейчас активны.
</b></details>

<details>
<summary>В команде новый участник, и ему нужно назначить роль "admin" в вашем проекте в OpenShift. Как это сделать?</summary><br><b>

`oc adm policy add-role-to-user <role> <user> -n <project>`
</b></details>

#### OpenShift — приложения

<details>
<summary>Как создать приложение MySQL, используя образ из Docker Hub?</summary><br><b>

`oc new-app mysql`
</b></details>

#### OpenShift — образы

<details>
<summary>Что такое поток образов (image stream)?</summary><br><b>
</b></details>

<details>
<summary>Как лучше всего запускать несколько сред OpenShift и управлять ими?</summary><br><b>

Федерация (Federation)
</b></details>

#### OpenShift — федерация

<details>
<summary>Что такое OpenShift Federation?</summary><br><b>

Управление и развёртывание сервисов и рабочих нагрузок в нескольких независимых кластерах через единый API
</b></details>

<details>
<summary>Объясните следующие понятия применительно к федерации:

  * Multi Cluster
  * Federated Cluster
  * Host Cluster
  * Member Cluster
</summary><br><b>

  * Multi Cluster — несколько кластеров, развёрнутых независимо и не знающих друг о друге
  * Federated Cluster — несколько кластеров, управляемых OpenShift Federation Control Plane
  * Host Cluster — кластер, на котором работает Federation Control Plane
  * Member Cluster — кластер, входящий в Federated Cluster и подключённый к Federation Control Plane
</b></details>

## OpenShift — хранилище

<details>
<summary>Что такое устройство хранения? Какие бывают устройства хранения?</summary><br><b>

* Жёсткие диски
* SSD
* USB
* Магнитная лента
</b></details>

<details>
<summary>Что такое время случайного позиционирования (Random Seek Time)?</summary><br><b>

Время, за которое диск добирается до места, где расположены данные, и считывает один блок/сектор.

Бонусный вопрос: каково время случайного позиционирования у SSD и магнитного диска?
Ответ: у магнитного — около 10 мс, у SSD — где-то между 0.08 и 0.16 мс
</b></details>

#### OpenShift — поды

<details>
<summary>Что происходит, когда под завершается с ошибкой или выходит из-за падения контейнера</summary><br><b>

Мастер-узел автоматически перезапускает под, если только он не падает слишком часто.
</b></details>

<details>
<summary>Что происходит, когда под падает слишком часто?</summary><br><b>

Мастер-узел помечает его как неисправный, и он временно больше не перезапускается.
</b></details>

<details>
<summary>Как узнать, на каком узле работает определённый под?</summary><br><b>

`oc get po -o wide`
</b></details>

#### OpenShift — сервисы

<details>
<summary>Объясните, что такое сервисы (Services) и в чём их преимущества</summary><br><b>

  - Сервисы в OpenShift определяют политику доступа к одному или нескольким наборам подов.<br>
  - Они связывают приложения между собой, обеспечивая взаимодействие между ними
  - Они предоставляют приложениям постоянные внутренние IP-адреса и имена хостов
  - Они могут обеспечивать базовую внутреннюю балансировку нагрузки
</b></details>

#### OpenShift — метки

<details>
<summary>Объясните, что такое метки (labels). Что это? Когда их использовать?</summary><br><b>

  - Метки используются для группировки или выбора объектов API
  - Это простые пары «ключ-значение», которые можно включать в метаданные некоторых объектов
  - Типичный сценарий: сгруппировать поды, сервисы, развёртывания (deployments), ... относящиеся к определённому приложению
</b></details>

#### OpenShift — сервисные учётные записи

<details>
<summary>Как вывести список сервисных учётных записей (Service Accounts)?</summary><br><b>

`oc get serviceaccounts`
</b></details>

#### OpenShift — сеть

<details>
<summary>Что такое маршрут (Route)?</summary><br><b>

Маршрут публикует сервис, назначая ему имя хоста, доступное извне
</b></details>

<details>
<summary>Из чего состоит Route?</summary><br><b>

  - имя
  - селектор сервиса
  - (необязательно) конфигурация безопасности
</b></details>

<details>
<summary>Верно или нет? Контейнер маршрутизатора (router) может работать только на мастер-узле</summary><br><b>

Неверно. Он может работать на любом узле.
</b></details>

<details>
<summary>Приведите пример использования маршрутизатора</summary><br><b>

1. Клиент использует адрес приложения, работающего в OpenShift
2. DNS разрешает адрес в хост, на котором работает маршрутизатор
3. Маршрутизатор проверяет, существует ли маршрут
4. Маршрутизатор проксирует запрос во внутренний под 
</b></details>

#### OpenShift — безопасность

<details>
<summary>Что такое "Security Context Constraints"?</summary><br><b>

Из [документации OpenShift](https://docs.openshift.com/container-platform/4.7/authentication/managing-security-context-constraints.html): «Подобно тому, как ресурсы RBAC управляют доступом пользователей, администраторы могут использовать ограничения контекста безопасности (security context constraints, SCC) для управления разрешениями подов».
</b></details>

<details>
<summary>Как дать пользователю `user1` возможность просматривать проект `wonderland`, при условии что у вас есть на это права</summary><br><b>

oc adm policy add-role-to-user view user1 -n wonderland
</b></details>

<details>
<summary>Как проверить, какой контекст сейчас текущий?</summary><br><b>

`oc whoami --show-context`
</b></details>

#### OpenShift — Serverless

<details>
<summary>Что такое OpenShift Serverless?</summary><br><b>

  - В общем случае «serverless» — это модель облачных вычислений, в которой масштабирование и выделение ресурсов берёт на себя платформа, а разработчики приложений могут сосредоточиться на разработке, а не на задачах, связанных с инфраструктурой
  - OpenShift Serverless позволяет динамически масштабировать приложения и даёт возможность создавать событийно-ориентированные (event-driven) приложения, независимо от того, где находятся источники — в Kubernetes, в облаке или в локальных (on-premise) решениях
  - OpenShift Serverless основан на проекте Knative.
</b></details>

<details>
<summary>Какие источники событий можно использовать с OpenShift Serverless?</summary><br><b>

  * Kafka
  * Kubernetes APIs
  * AWS Kinesis
  * AWS SQS
  * JIRA
  * Slack

Поддерживаются и поставляются с OpenShift и другие источники.
</b></details>

<details>
<summary>Объясните, что такое serverless-функции</summary><br><b>
</b></details>

<details>
<summary>В чём разница между Serverless Containers и Serverless functions?</summary><br><b>
</b></details>

#### OpenShift — разное

<details>
<summary>Что такое Replication Controller?</summary><br><b>

Replication Controller отвечает за то, чтобы в любой момент времени работало заданное количество подов.<br>
Если подов работает больше, чем нужно, -> он удаляет часть из них<br>
Если подов работает недостаточно -> он создаёт новые
</b></details>

# Kubernetes

<!-- {% raw %} -->

Какая цель?

* Подготовиться к сертификации CKA
  * См. страницу [CKA](CKA.md)
* Изучить Kubernetes, прорабатывая как теоретический, так и практический материал
  * Решать [упражнения](#упражнения-по-kubernetes)
  * Отвечать на [вопросы](#вопросы-по-kubernetes)
* Изучить Kubernetes на практике
  * Решать [упражнения](#упражнения-по-kubernetes)

- [Kubernetes](#kubernetes)
  - [Упражнения по Kubernetes](#упражнения-по-kubernetes)
    - [Pods](#pods)
    - [Service](#service)
    - [ReplicaSet](#replicaset)
    - [Метки и селекторы](#метки-и-селекторы)
    - [Планировщик (Scheduler)](#планировщик-scheduler)
    - [Kustomize](#kustomize)
  - [Вопросы по Kubernetes](#вопросы-по-kubernetes)
    - [Kubernetes 101](#kubernetes-101)
    - [Кластер и архитектура](#кластер-и-архитектура)
      - [Kubelet](#kubelet)
      - [Команды для узлов](#команды-для-узлов)
    - [Pods](#pods-1)
      - [Статические Pod](#статические-pod)
      - [Команды для Pod](#команды-для-pod)
      - [Устранение неполадок и отладка Pod](#устранение-неполадок-и-отладка-pod)
    - [Метки и селекторы](#метки-и-селекторы-1)
    - [Deployments](#deployments)
      - [Команды для Deployment](#команды-для-deployment)
    - [Services](#services)
    - [Ingress](#ingress)
    - [ReplicaSets](#replicasets)
    - [DaemonSet](#daemonset)
      - [DaemonSet - команды](#daemonset---команды)
    - [StatefulSet](#statefulset)
    - [Хранилище (Storage)](#хранилище-storage)
      - [Тома (Volumes)](#тома-volumes)
    - [Сеть](#сеть)
    - [Сетевые политики (Network Policies)](#сетевые-политики-network-policies)
    - [etcd](#etcd)
    - [Пространства имён (Namespaces)](#пространства-имён-namespaces)
      - [Пространства имён - команды](#пространства-имён---команды)
      - [Квоты ресурсов (Resources Quota)](#квоты-ресурсов-resources-quota)
    - [Операторы (Operators)](#операторы-operators)
    - [Secrets](#secrets)
    - [Тома (Volumes)](#тома-volumes-1)
    - [Управление доступом](#управление-доступом)
    - [Паттерны](#паттерны)
    - [CronJob](#cronjob)
    - [Разное](#разное)
    - [Gatekeeper](#gatekeeper)
    - [Тестирование политик](#тестирование-политик)
    - [Helm](#helm)
      - [Команды](#команды)
    - [Безопасность](#безопасность)
    - [Сценарии устранения неполадок](#сценарии-устранения-неполадок)
    - [Istio](#istio)
    - [Контроллеры (Controllers)](#контроллеры-controllers)
    - [Планировщик (Scheduler)](#планировщик-scheduler-1)
      - [Node Affinity](#node-affinity)
    - [Taints](#taints)
    - [Ограничения ресурсов (Resource Limits)](#ограничения-ресурсов-resource-limits)
      - [Ограничения ресурсов - команды](#ограничения-ресурсов---команды)
    - [Мониторинг](#мониторинг)
    - [Kustomize](#kustomize-1)
    - [Стратегии развёртывания](#стратегии-развёртывания)
    - [Сценарии](#сценарии)

## Упражнения по Kubernetes

### Pods

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Мой первый Pod | Pods | [Упражнение](pods_01.md) | [Решение](solutions/pods_01_solution.md)
| «Убийство» контейнеров | Pods | [Упражнение](killing_containers.md) | [Решение](solutions/killing_containers.md)

### Service

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Создание Service | Service | [Упражнение](services_01.md) | [Решение](solutions/services_01_solution.md)

### ReplicaSet

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Создание ReplicaSet | ReplicaSet | [Упражнение](replicaset_01.md) | [Решение](solutions/replicaset_01_solution.md)
| Управление ReplicaSet | ReplicaSet | [Упражнение](replicaset_02.md) | [Решение](solutions/replicaset_02_solution.md)
| Селекторы ReplicaSet | ReplicaSet | [Упражнение](replicaset_03.md) | [Решение](solutions/replicaset_03_solution.md)

### Метки и селекторы

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Метки и селекторы 101 | Метки, селекторы | [Упражнение](exercises/labels_and_selectors/exercise.md) | [Решение](exercises/labels_and_selectors/solution.md)
| Селекторы узлов (Node Selectors) | Метки, селекторы | [Упражнение](exercises/node_selectors/exercise.md) | [Решение](exercises/node_selectors/solution.md)


### Планировщик (Scheduler)

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Taints 101 | Taints | [Упражнение](exercises/taints_101/exercise.md) | [Решение](exercises/taints_101/solution.md)

### Kustomize

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Общие метки (common labels) | Kustomize | [Упражнение](exercises/kustomize_common_labels/exercise.md) | [Решение](exercises/kustomize_common_labels/solution.md)

## Вопросы по Kubernetes

### Kubernetes 101

<details>
<summary>Что такое Kubernetes? Почему организации его используют?</summary><br><b>

Kubernetes — это система с открытым исходным кодом, которая даёт пользователям возможность управлять контейнеризованными приложениями, масштабировать и развёртывать их.

Чтобы понять, для чего хорош Kubernetes, рассмотрим несколько примеров:

* Нужно запускать определённое приложение в контейнере в нескольких разных местах и синхронизировать изменения между всеми ними, где бы они ни работали
* Выполнение обновлений и изменений в сотнях контейнеров
* Обработка ситуаций, когда текущая нагрузка требует увеличить (или уменьшить) масштаб

</b></details>

<details>
<summary>Когда и почему НЕ стоит использовать Kubernetes?</summary><br><b>

  - Если речь идёт об управлении низкоуровневой инфраструктурой или «голым железом» (bare metal), Kubernetes, вероятно, не то, что нужно
  - Если команда небольшая (например, меньше 20 инженеров) и запускает меньше дюжины контейнеров, Kubernetes может оказаться избыточным (даже если нужны масштабирование, выкатка обновлений и т.д.). Можно по-прежнему получать выгоду от управляемого Kubernetes, но решение о его внедрении определённо стоит тщательно обдумать.

</b></details>

<details>
<summary>Назовите некоторые возможности Kubernetes</summary><br><b>

  - Самовосстановление (Self-Healing): Kubernetes использует проверки работоспособности (health checks), чтобы отслеживать контейнеры и выполнять определённые действия при сбое или других событиях, например перезапускать контейнер
  - Балансировка нагрузки (Load Balancing): Kubernetes может распределять и/или балансировать запросы к приложениям, работающим в кластере, с учётом состояния Pod, в которых работает приложение
  - Операторы (Operators): упакованные для Kubernetes приложения, которые могут использовать API кластера, чтобы обновлять его состояние и запускать действия в ответ на события и изменения состояния приложения
  - Автоматическая выкатка (Automated Rollout): постепенная выкатка обновлений приложений и поддержка отката, если что-то пошло не так
  - Масштабирование (Scaling): горизонтальное масштабирование (вниз и вверх) на основе различных параметров состояния и заданных пользователем критериев
  - Secrets: механизм хранения имён пользователей, паролей и адресов сервисов в закрытом виде, так что их могут видеть не все пользователи кластера

</b></details>

<details>
<summary>Какие объекты есть в Kubernetes?</summary><br><b>

  * Pod
  * Service
  * ReplicationController
  * ReplicaSet
  * DaemonSet
  * Namespace
  * ConfigMap
  ...
</b></details>

<details>
<summary>Какие поля обязательны для любого объекта Kubernetes?</summary><br><b>

metadata, kind и apiVersion

</b></details>

<details>
<summary>Что такое kubectl?</summary><br><b>

Kubectl — это инструмент командной строки Kubernetes, который позволяет выполнять команды в кластерах Kubernetes. Например, с помощью kubectl можно развёртывать приложения, просматривать ресурсы кластера и управлять ими, а также смотреть логи.

</b></details>

<details>
<summary>Какие объекты Kubernetes обычно используются при развёртывании приложений в Kubernetes?</summary><br><b>

* Deployment — создаёт Pod () и следит за ними
* Service: маршрутизирует трафик к Pod внутри кластера
* Ingress: маршрутизирует трафик извне кластера

</b></details>

<details>
<summary>Почему в Kubernetes нет такой команды? <code>kubectl get containers</code></summary><br><b>

Потому что контейнер не является объектом Kubernetes. Наименьшая единица-объект в Kubernetes — это Pod. В одном Pod может быть один или несколько контейнеров.

</b></details>

<details>
<summary>Какие действия или операции можно считать лучшими практиками при работе с Kubernetes?</summary><br><b>

  - Всегда проверять, что YAML-файлы Kubernetes корректны. Рекомендуется применять автоматические проверки и пайплайны.
  - Всегда задавать requests и limits, чтобы не допустить ситуации, когда контейнеры используют всю память кластера, что может привести к проблеме OOM
  - Задавать метки (labels) для логической группировки Pod, Deployment и т.д. Помимо прочего, метки можно использовать, например, для обозначения типа приложения

</b></details>

### Кластер и архитектура

<details>
<summary>Что такое кластер Kubernetes?</summary><br><b>

Определение Red Hat: «Кластер Kubernetes — это набор узлов (node machines) для запуска контейнеризованных приложений. Если вы используете Kubernetes, вы используете кластер.
Как минимум кластер содержит рабочий узел (worker node) и главный узел (master node).»

Подробнее [здесь](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-cluster)
</b></details>

<details>
<summary>Что такое узел (Node)?</summary><br><b>

Узел — это виртуальная или физическая машина, которая служит рабочей машиной (worker) для запуска приложений.<br>
В production-окружении рекомендуется иметь как минимум 3 узла.
</b></details>

<details>
<summary>За что отвечает master-узел?</summary><br><b>

Master координирует все рабочие процессы в кластере:

* Планирование (scheduling) приложений
* Управление желаемым состоянием (desired state)
* Выкатка новых обновлений

</b></details>

<details>
<summary>Кратко и на высоком уровне опишите, что происходит при выполнении <code>kubectl get nodes</code></summary><br><b>

1. Пользователь проходит аутентификацию
2. Запрос проверяется (валидируется) kube-apiserver
3. Данные извлекаются из etcd
</b></details>

<details>
<summary>Правда или ложь? В каждом кластере должно быть 0 или более master-узлов и как минимум 1 рабочий узел</summary><br><b>

Ложь. Кластер Kubernetes состоит как минимум из 1 master-узла и может иметь 0 рабочих узлов (хотя это было бы не очень полезно...)

</b></details> 

<details>
<summary>Какие компоненты входят в master-узел (он же control plane)?</summary><br><b>

  * API Server — API Kubernetes. Через него взаимодействуют все компоненты кластера
  * Scheduler — назначает приложению рабочий узел, на котором оно может работать
  * Controller Manager — обслуживание кластера (репликация, сбои узлов и т.д.)
  * etcd — хранит конфигурацию кластера

</b></details>

<details>
<summary>Какие компоненты входят в рабочий узел (он же data plane)?</summary><br><b>

  * Kubelet — агент, отвечающий за взаимодействие узла с master.
  * Kube-proxy — балансировка трафика между компонентами приложения
  * Container runtime — движок, запускающий контейнеры (Podman, Docker, ...)

</b></details>

<details>
<summary>Расставьте компоненты из правой части изображения по правильным местам на схеме<br>
<img src="images/cluster_architecture_exercise.png"/>
</summary><br><b>
<img src="images/cluster_architecture_solution.png"/>

</b></details>

<details>
<summary>Под управлением несколько кластеров Kubernetes. Как быстро переключаться между кластерами с помощью kubectl?</summary><br><b>

`kubectl config use-context`
</b></details>

<details>
<summary>Как предотвратить высокое потребление памяти в кластере Kubernetes и возможные проблемы вроде утечек памяти и OOM?</summary><br><b>

Задавать requests и limits, особенно для сторонних приложений (где неопределённость ещё выше)
</b></details>

<details>
<summary>Есть ли опыт развёртывания кластера Kubernetes? Если да, опишите процесс на высоком уровне</summary><br><b>

1. Создать несколько инстансов, которые будут использоваться как узлы/рабочие узлы Kubernetes. Также создать инстанс, который будет выполнять роль Master. Инстансы можно выделить в облаке, или это могут быть виртуальные машины на физических (bare metal) хостах.
2. Подготовить удостоверяющий центр (certificate authority), который будет использоваться для генерации TLS-сертификатов для различных компонентов кластера Kubernetes (kubelet, etcd, ...)
  1. Сгенерировать сертификат и закрытый ключ для различных компонентов
3. Сгенерировать kubeconfig, чтобы различные клиенты Kubernetes могли находить API-серверы и проходить аутентификацию.
4. Сгенерировать ключ шифрования, который будет использоваться для шифрования данных кластера
5. Создать кластер etcd
</b></details>

<details>
<summary>Какая команда выведет список всех типов объектов в кластере?</summary><br><b>

`kubectl api-resources`
</b></details>

<details>
<summary>Что делает <code>kubectl get componentstatus</code>?</summary><br><b>

Выводит состояние каждого из компонентов control plane.
</b></details>

#### Kubelet

<details>
<summary>Что происходит с работающими Pod, если остановить Kubelet на рабочих узлах?</summary><br><b>

После остановки сервиса kubelet на рабочем узле узел больше не сможет взаимодействовать с API-сервером Kubernetes. В результате узел будет помечен как NotReady, а Pod, работающие на этом узле, — как Unknown. Затем control plane Kubernetes попытается перепланировать эти Pod на другие доступные узлы кластера. 
</b></details>

#### Команды для узлов

<details>
<summary>Выполните команду, которая покажет все узлы кластера</summary><br><b>

`kubectl get nodes`

Примечание: имеет смысл создать псевдоним (`alias k=kubectl`) и привыкнуть к `k get no`
</b></details>

<details>
<summary>Создайте список всех узлов в формате JSON и сохраните его в файл "some_nodes.json"</summary><br><b>

`k get nodes -o json > some_nodes.json`
</b></details>

<details>
<summary>Проверьте, какие метки есть у одного из узлов кластера</summary><br><b>

`k get no minikube --show-labels`
</b></details>

### Pods

<details>
<summary>Объясните, что такое Pod</summary><br><b>

Pod — это группа из одного или нескольких контейнеров с общими ресурсами хранения и сети, а также спецификацией того, как запускать эти контейнеры.

Pod — это наименьшие развёртываемые вычислительные единицы, которые можно создавать и которыми можно управлять в Kubernetes. 

</b></details>

<details>
<summary>Разверните Pod с именем "my-pod" из образа nginx:alpine</summary><br><b>

`kubectl run my-pod --image=nginx:alpine`

Новичкам в Kubernetes стоит знать, что это не самый распространённый способ запускать Pod. Обычно запускают Deployment, который, в свою очередь, запускает Pod.

Кроме того, Pod и/или Deployment обычно описывают в файлах, а не создают напрямую только с помощью аргументов CLI.
</b></details>

<details>
<summary>Что можно сказать об утверждении «Pod не предназначены для создания напрямую»?</summary><br><b>

Pod действительно обычно не создают напрямую. Как правило, Pod создаются в составе других сущностей, таких как Deployment или ReplicaSet.

Если Pod «умирает», Kubernetes не восстановит его. Поэтому, например, полезнее определять ReplicaSet, который гарантирует, что заданное количество Pod будет работать всегда, даже после гибели какого-то Pod.
</b></details>

<details>
<summary>Сколько контейнеров может содержать Pod?</summary><br><b>

Pod может содержать несколько контейнеров, но в большинстве случаев, скорее всего, будет один контейнер на Pod.

Есть паттерны, в которых имеет смысл запускать больше одного контейнера, например паттерн "side-car", когда нужно вести логирование или выполнять другую операцию в отдельном контейнере, работающем вместе с контейнером приложения в том же Pod.
</b></details>

<details>
<summary>В каких случаях имеет смысл запускать несколько контейнеров в одном Pod?</summary><br><b>

Один из примеров — веб-приложение с отдельными (= в собственных контейнерах) компонентами/адаптерами логирования и мониторинга.<br>
Пайплайн CI/CD (например, на Tekton) может запускать несколько контейнеров в одном Pod, если Task содержит несколько команд.
</b></details>

<details>
<summary>Какие фазы может проходить Pod?</summary><br><b>

  * Running — Pod привязан к узлу, и как минимум один контейнер работает
  * Failed/Error — как минимум один контейнер в Pod завершился с ошибкой
  * Succeeded — все контейнеры в Pod завершились успешно
  * Unknown — состояние Pod не удалось получить
  * Pending — контейнеры ещё не запущены (возможно, образы ещё скачиваются или Pod ещё не запланирован)
</b></details>

<details>
<summary>Правда или ложь? По умолчанию Pod изолированы. Это значит, что они не могут получать трафик ни из какого источника</summary><br><b>

Ложь. По умолчанию Pod не изолированы = Pod принимают трафик из любого источника.
</b></details>

<details>
<summary>Правда или ложь? Фаза "Pending" означает, что Pod ещё не принят кластером Kubernetes, поэтому планировщик не может его запустить, пока он не будет принят</summary><br><b>

Ложь. "Pending" наступает после того, как Pod принят кластером, но контейнер не может запуститься по разным причинам, например образы ещё не скачаны.
</b></details>

<details>
<summary>Правда или ложь? Один Pod может быть распределён по нескольким узлам</summary><br><b>

Ложь. Один Pod может работать только на одном узле.
</b></details>

<details>
<summary>При запуске Pod виден статус <code>ContainerCreating</code></summary><br><b>
</b></details>

<details>
<summary>Правда или ложь? Том (volume), определённый в Pod, доступен всем контейнерам этого Pod</summary><br><b>

Правда.
</b></details>

<details>
<summary>Что происходит при запуске Pod с помощью kubectl?</summary><br><b>

1. Kubectl отправляет запрос API-серверу (kube-apiserver) на создание Pod
   1. В процессе пользователь проходит аутентификацию, а запрос — валидацию.
   2. Данные записываются в etcd
2. Scheduler, отслеживая API-сервер (kube-apiserver), обнаруживает, что есть Pod, не назначенный на узел
3. Scheduler выбирает узел, на который назначить Pod
   1. Информация записывается в etcd
4. Scheduler сообщает API-серверу, какой узел он выбрал
5. Kubelet (который тоже отслеживает API-сервер) замечает, что на узел, где он работает, назначен Pod и этот Pod не запущен
6. Kubelet отправляет запрос движку контейнеров (например, Docker) на создание и запуск контейнеров
7. Kubelet отправляет обновление API-серверу (сообщая, что Pod работает)
   1. API-сервер снова обновляет данные в etcd
</b></details>

<details>
<summary>Как убедиться, что контейнер работает, после выполнения команды <code>kubectl run web --image nginxinc/nginx-unprivileged</code></summary><br><b>

* Команда `kubectl describe pods <POD_NAME>` покажет, работает ли контейнер:
`Status:       Running`
* Выполнить команду внутри контейнера: `kubectl exec web -- ls`
</b></details>

<details>
<summary>После выполнения <code>kubectl run database --image mongo</code> виден статус "CrashLoopBackOff". Что могло пойти не так и как это проверить?</summary><br><b>

"CrashLoopBackOff" означает, что Pod запускается, падает, снова запускается... и так по кругу.<br>
Причин этой ошибки много — нехватка прав, неправильная настройка init-контейнера, проблема подключения persistent volume и т.д.

Один из способов выяснить причину — выполнить `kubectl describe po <POD_NAME>` и посмотреть на код выхода

```
 Last State:     Terminated
   Reason:       Error
   Exit Code:    100
```

Другой способ разобраться в происходящем — выполнить `kubectl logs <POD_NAME>`. Это даст логи контейнеров, работающих в этом Pod.
</b></details>

<details>
<summary>Объясните назначение следующих строк

```
livenessProbe:
  exec:
    command:
    - cat
    - /appStatus
  initialDelaySeconds: 10
  periodSeconds: 5
```
</summary><br><b>

В этих строках используется `liveness probe`. Она нужна, чтобы перезапускать контейнер, когда он переходит в нежелательное состояние.<br>
В данном случае, если команда `cat /appStatus` завершится с ошибкой, Kubernetes завершит контейнер и применит политику перезапуска (restart policy). `initialDelaySeconds: 10` означает, что Kubelet подождёт 10 секунд, прежде чем выполнить команду/проверку в первый раз. Начиная с этого момента он будет выполнять её каждые 5 секунд, как задано в `periodSeconds`
</b></details>

<details>
<summary>Объясните назначение следующих строк

```
readinessProbe:
      tcpSocket:
        port: 2017
      initialDelaySeconds: 15
      periodSeconds: 20
```
</summary><br><b>

Они задают readiness probe: Pod не будет помечен как "Ready", пока не удастся подключиться к порту 2017 контейнера. Первая проверка начнётся через 15 секунд после запуска контейнера, и затем проверка будет повторяться каждые 20 секунд, пока не удастся подключиться к заданному порту.
</b></details>

<details>
<summary>Что означает статус Pod "ErrImagePull"?</summary><br><b>

Не удалось скачать образ, указанный для запуска контейнера(ов). Например, такое бывает, если клиент не прошёл аутентификацию.<br>
Подробности можно получить с помощью `kubectl describe po <POD_NAME>`.
</b></details>

<details>
<summary>Что происходит при удалении Pod?</summary><br><b>

1. Основным процессам внутри контейнеров данного Pod отправляется сигнал `TERM` для их завершения
2. Каждому контейнеру даётся 30 секунд на корректное (graceful) завершение процессов
3. Если отведённый период истекает, используется сигнал `KILL`, чтобы принудительно завершить процессы, а также контейнеры
</b></details>

<details>
<summary>Объясните liveness probes</summary><br><b>

Liveness probes — полезный механизм, который перезапускает контейнер, когда определённая пользователем проверка (check/probe) завершается неудачей.<br>
Например, пользователь может задать, что команда `cat /app/status` будет выполняться каждые X секунд, и как только эта команда завершится с ошибкой, контейнер будет перезапущен.

Подробнее об этом можно прочитать на [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes)
</b></details>

<details>
<summary>Объясните readiness probes</summary><br><b>

Readiness probes используются Kubelet, чтобы понять, когда контейнер готов начать работу и принимать трафик.<br>
Например, readiness probe может заключаться в подключении к порту 8080 контейнера. Как только Kubelet удаётся подключиться, Pod помечается как готовый (ready)

Подробнее об этом можно прочитать на [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes)
</b></details>

<details>
<summary>Как статус readiness probe влияет на Service, если они используются вместе?</summary><br><b>

Получать запросы, отправленные в Service, смогут только контейнеры, состояние которых установлено в Success.
</b></details>

<details>
<summary>Почему в большинстве случаев в Pod обычно только один контейнер?</summary><br><b>

Одна из причин — так сложнее масштабировать, когда нужно масштабировать только один из контейнеров данного Pod.
</b></details>

<details>
<summary>Правда или ложь? После назначения Pod на рабочий узел он будет работать только на этом узле, даже если в какой-то момент упадёт и будет поднят новый Pod</summary><br><b>

Правда.
</b></details>

<details>
<summary>Правда или ложь? Каждый Pod при создании получает собственный публичный IP-адрес</summary><br><b>

Ложь. Каждый Pod получает IP-адрес, но внутренний и недоступный извне.

Чтобы сделать Pod доступным извне, в Kubernetes нужно использовать объект Service.
</b></details>

#### Статические Pod

<details>
<summary>Что такое статические Pod (Static Pods)?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/): «Статическими Pod управляет непосредственно демон kubelet на конкретном узле, без наблюдения со стороны API-сервера. В отличие от Pod, которыми управляет control plane (например, Deployment), за каждым статическим Pod следит kubelet (и перезапускает его в случае сбоя).»
</b></details>

<details>
<summary>Правда или ложь? Так же, как существуют «статические Pod», существуют и другие статические ресурсы, например "deployments" и "replicasets"</summary><br><b>

Ложь.
</b></details>

<details>
<summary>В каких случаях используют статические Pod?</summary><br><b>

Очевидный пример — запуск Pod control plane, то есть таких Pod, как kube-apiserver, scheduler и т.д. Они должны работать независимо от того, работают ли какие-то компоненты кластера, и должны запускаться на определённых узлах кластера.
</b></details>

<details>
<summary>Как определить, какие Pod являются статическими?</summary><br><b>

Суффикс имени таких Pod совпадает с именем узла, на котором они работают
TODO: проверить, всегда ли это так.
</b></details>

<details>
<summary>Что из перечисленного не является статическим Pod?:

* kube-scheduler
* kube-proxy
* kube-apiserver
</summary><br><b>

kube-proxy — это DaemonSet (поскольку он должен присутствовать на каждом узле кластера). Нет какого-то одного конкретного узла, на котором он должен работать.
</b></details>

<details>
<summary>Где находятся манифесты статических Pod?</summary><br><b>

Чаще всего в /etc/kubernetes/manifests, но это можно проверить с помощью `grep -i static /var/lib/kubelet/config.yaml`, найдя значение `statisPodsPath`.

Возможно, конфигурация находится по другому пути. Чтобы проверить, выполнить `ps -ef | grep kubelet` и посмотреть значение аргумента --config процесса `/usr/bin/kubelet`

Сам ключ, задающий путь к статическим Pod, — `staticPodPath`. Поэтому, если конфигурация находится в `/var/lib/kubelet/config.yaml`, можно выполнить `grep staticPodPath /var/lib/kubelet/config.yaml`.
</b></details>

<details>
<summary>Опишите, как удалить статический Pod
</summary><br><b>

Найти каталог статических Pod (см. `staticPodPath` в конфигурационном файле kubelet).

Перейти в этот каталог и удалить манифест/определение статического Pod (`rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`)
</b></details>

#### Команды для Pod

<details>
<summary>Как проверить, на какой рабочий узел были запланированы Pod? Другими словами, как проверить, на каком узле работает определённый Pod?</summary><br><b>

`kubectl get pods -o wide`
</b></details>

<details>
<summary>Как удалить Pod?</summary><br><b>

`kubectl delete pod pod_name`
</b></details>

<details>
<summary>Выведите список всех Pod с меткой "env=prod"</summary><br><b>

`k get po -l env=prod`

Чтобы посчитать их: `k get po -l env=prod --no-headers | wc -l`
</b></details>

<details>
<summary>Как вывести список Pod в текущем пространстве имён?</summary><br><b>

`kubectl get po`
</b></details>

<details>
<summary>Как посмотреть все Pod, работающие во всех пространствах имён?</summary><br><b>

`kubectl get pods --all-namespaces`
</b></details>

#### Устранение неполадок и отладка Pod

<details>
<summary>Pod при запуске находится в состоянии "Pending". В чём может быть причина?</summary><br><b>

Одна из возможных причин — не работает планировщик (scheduler), который должен распределять Pod по узлам. Чтобы проверить это, можно выполнить `kubectl get po -A | grep scheduler` или посмотреть непосредственно в пространстве имён `kube-system`.
</b></details>

<details>
<summary>Что делает команда <code>kubectl logs [pod-name]</code>?</summary><br><b>

Выводит логи контейнера в Pod.
</b></details>

<details>
<summary>Что делает команда <code>kubectl describe pod [pod name] does?</code>?</summary><br><b>

Показывает подробную информацию о конкретном ресурсе или группе ресурсов.
</b></details>

<details>
<summary>Создайте статический Pod из образа <code>python</code>, который выполняет команду <code>sleep 2017</code></summary><br><b>

Сначала перейти в каталог, который kubelet отслеживает для создания статических Pod: `cd /etc/kubernetes/manifests` (путь можно проверить в конфигурационном файле kubelet)

Затем создать в этом каталоге определение/манифест
`k run some-pod --image=python --command sleep 2017 --restart=Never --dry-run=client -o yaml > statuc-pod.yaml`
</b></details>

### Метки и селекторы

<details>
<summary>Объясните, что такое метки (Labels)</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/): «Метки — это пары ключ/значение, прикреплённые к объектам, например к Pod. Метки предназначены для задания идентифицирующих атрибутов объектов, которые значимы и важны для пользователей, но не несут непосредственной семантики для ядра системы. Метки можно использовать для организации и выбора подмножеств объектов. Метки можно прикреплять к объектам при создании, а затем в любой момент добавлять и изменять. У каждого объекта может быть определён набор меток ключ/значение. Каждый ключ должен быть уникальным в пределах объекта.»
</b></details>

<details>
<summary>Объясните, что такое селекторы (selectors)</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors): «В отличие от имён и UID, метки не обеспечивают уникальности. В общем случае ожидается, что одну и ту же метку (метки) будут нести многие объекты.

С помощью селектора меток (label selector) клиент/пользователь может определить набор объектов. Селектор меток — основной примитив группировки в Kubernetes.

Сейчас API поддерживает два типа селекторов: на основе равенства (equality-based) и на основе множеств (set-based). Селектор меток может состоять из нескольких требований, разделённых запятыми. Если требований несколько, должны выполняться все, поэтому разделитель-запятая работает как логический оператор И (&&).»
</b></details>

<details>
<summary>Приведите реальные примеры использования меток</summary><br><b>

* Планировщик может использовать их, чтобы размещать определённые Pod (с определёнными метками) на конкретных узлах
* ReplicaSet использует их, чтобы отслеживать Pod, которые нужно масштабировать
</b></details>

<details>
<summary>Что такое аннотации (Annotations)?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/): «С помощью аннотаций Kubernetes к объектам можно прикреплять произвольные неидентифицирующие метаданные. Клиенты, например инструменты и библиотеки, могут получать эти метаданные.»
</b></details>

<details>
<summary>Чем аннотации отличаются от меток?</summary><br><b>

[Kuberenets.io](Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects. The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels.): «Метки можно использовать для выбора объектов и поиска наборов объектов, удовлетворяющих определённым условиям. Аннотации, напротив, не используются для идентификации и выбора объектов. Метаданные в аннотации могут быть маленькими или большими, структурированными или неструктурированными и могут содержать символы, недопустимые в метках.»
</b></details>

<details>
<summary>Как посмотреть логи контейнера, работающего в Pod?</summary><br><b>

`k logs POD_NAME`
</b></details>

<details>
<summary>В Pod с именем "some-pod" два контейнера. Что произойдёт при выполнении <code>kubectl logs some-pod</code></summary><br><b>

Команда не сработает, потому что в Pod два контейнера и нужно указать один из них: `kubectl logs POD_NAME -c CONTAINER_NAME`
</b></details>

### Deployments

<details>
<summary>Что такое "Deployment" в Kubernetes?</summary><br><b>

Deployment в Kubernetes используется, чтобы сообщить Kubernetes, как создавать или изменять экземпляры Pod, в которых работает контейнеризованное приложение.
Deployment может масштабировать количество реплик Pod, обеспечивать контролируемую выкатку обновлённого кода или при необходимости откатываться к более ранней версии развёртывания. 

Deployment — это декларативное описание желаемого состояния для Pod и ReplicaSet.
</b></details>

<details>
<summary>Как создать Deployment из образа "nginx:alpine"?</code></summary><br><b>

`kubectl create deployment my-first-deployment --image=nginx:alpine`

ИЛИ

```
cat << EOF | kubectl create -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
```
</b></details>

<details>
<summary>Как убедиться, что Deployment создан?</code></summary><br><b>

`kubectl get deployments` или `kubectl get deploy`

Эта команда выводит список всех объектов Deployment, созданных и существующих в кластере. Это не означает, что развёртывания готовы и работают. Это можно проверить по столбцам "READY" и "AVAILABLE".
</b></details>

<details>
<summary>Как отредактировать Deployment?</code></summary><br><b>

`kubectl edit deployment <DEPLOYMENT_NAME>`
</b></details>

<details>
<summary>Что происходит после редактирования Deployment и смены образа?</summary><br><b>

Pod будет завершён, и будет создан другой, новый Pod.

Кроме того, если посмотреть на ReplicaSet, будет видно, что в старой реплике нет Pod и создан новый ReplicaSet.
</b></details>

<details>
<summary>Как удалить Deployment?</summary><br><b>

Один способ — указать имя Deployment: `kubectl delete deployment [deployment_name]`

Другой способ — использовать конфигурационный файл Deployment: `kubectl delete -f deployment.yaml`
</b></details>

<details>
<summary>Что происходит при удалении Deployment?</summary><br><b>

Pod, относящийся к Deployment, будет завершён, а ReplicaSet — удалён.
</b></details>

<details>
<summary>Что происходит «за кулисами» при создании объекта Deployment?</summary><br><b>

При выполнении `kubectl create deployment some_deployment --image=nginx` происходит следующее

1. API-серверу Kubernetes в кластере отправляется HTTP-запрос на создание нового Deployment
2. Создаётся новый объект Pod, который планируется на один из рабочих узлов
3. Kublet на рабочем узле замечает новый Pod и даёт указание движку container runtime скачать образ из реестра
4. Из только что скачанного образа создаётся новый контейнер
</b></details>

<details>
<summary>Как сделать приложение доступным в частной или внешней сети?</summary><br><b>

С помощью Service.
</b></details>

<details>
<summary>Можно ли использовать Deployment для stateful-приложений?</summary><br><b>
</b></details>

<details>
<summary>Исправьте следующий манифест Deployment

```yaml
apiVersion: apps/v1
kind: Deploy
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: dep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```
</summary><br><b>

Заменить `kind: Deploy` на `kind: Deployment`
</b></details>

<details>
<summary>Исправьте следующий манифест Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: depdep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```
</summary><br><b>

Селектор не совпадает с меткой (dep и depdep). Чтобы исправить, заменить depdep на dep.
</b></details>

#### Команды для Deployment

<details>
<summary>Создайте файл определения/манифест Deployment с именем "dep" с 3 репликами, использующий образ 'redis'</summary><br><b>

`k create deploy dep -o yaml --image=redis --dry-run=client --replicas 3 > deployment.yaml `

</b></details>

<details>
<summary>Удалите Deployment `depdep`</summary><br><b>

`k delete deploy depdep`

</b></details>

<details>
<summary>Создайте Deployment с именем "pluck" из образа "redis" и убедитесь, что он запускает 5 реплик</summary><br><b>

`kubectl create deployment pluck --image=redis`

`kubectl scale deployment pluck --replicas=5`
</b></details>

<details>
<summary>Создайте Deployment со следующими свойствами:

* имя "blufer"
* использует образ "python"
* запускает 3 реплики
* все Pod размещаются на узле с меткой "blufer"
</summary><br><b>

`kubectl create deployment blufer --image=python --replicas=3 -o yaml --dry-run=client > deployment.yaml`

Добавить следующий раздел (`vi deployment.yaml`):

```
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedlingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: blufer
            operator: Exists
```

`kubectl apply -f deployment.yaml`
</b></details>

### Services

<details>
<summary>Что такое Service в Kubernetes?</summary><br><b>

«Абстрактный способ предоставить доступ к приложению, работающему на наборе Pod, как к сетевому сервису.» — подробнее [здесь](https://kubernetes.io/docs/concepts/services-networking/service)

Проще говоря, он позволяет добавить внутреннюю или внешнюю связность для определённого приложения, работающего в контейнере.
</b></details>

<details>
<summary>Расставьте компоненты по правильным местам применительно к Service в Kubernetes<br>
<img src="images/service_exercise.png"/>
</summary><br><b>

<img src="images/service_solution.png"/>

</b></details>


<details>
<summary>Как создать Service для существующего Deployment с именем "alle" на порту 8080, чтобы Pod были доступны через Load Balancer?</summary><br><b>

Императивный способ:

`kubectl expose deployment alle --type=LoadBalancer --port 8080`
</b></details>

<details>
<summary>Правда или ложь? Жизненные циклы Pod и Service не связаны, поэтому когда Pod «умирает», Service остаётся </summary><br><b>

Правда
</b></details>

<details>
<summary>Как после создания Service проверить, что он создан?</summary><br><b>

`kubectl get svc`
</b></details>

<details>
<summary>Какой тип Service используется по умолчанию?</summary><br><b>

ClusterIP — используется для внутреннего взаимодействия.
</b></details>

<details>
<summary>Какие типы Service существуют?</summary><br><b>

* ClusterIP
* NodePort
* LoadBalancer
* ExternalName

Подробнее на эту тему [здесь](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
</b></details>

<details>
<summary>Как связаны Service и Deployment?</summary><br><b>

На самом деле они не связаны. Service указывает непосредственно на Pod, никак не связываясь с Deployment.
</b></details>

<details>
<summary>Какие шаги важны при определении/добавлении Service?</summary><br><b>

1. Убедиться, что targetPort у Service совпадает с containerPort у Pod
2. Убедиться, что селектор совпадает хотя бы с одной из меток Pod

</b></details>

<details>
<summary>Какой тип Service используется в Kubernetes по умолчанию и для чего он нужен?</summary><br><b>

По умолчанию используется ClusterIP, он нужен для предоставления порта внутри кластера. Он полезен, когда нужно обеспечить внутреннее взаимодействие между Pod и запретить любой внешний доступ.

</b></details>

<details>
<summary>Как получить информацию об определённом Service?</summary><br><b>

`kubctl describe service <SERVICE_NAME>`

Чаще используют `kubectl describe svc ...`

</b></details>

<details>
<summary>Что делает следующая команда?

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```
</summary><br><b>

Она открывает доступ к ReplicaSet, создавая сервис с именем 'replicaset-svc'. Открытый порт — 2017 (это порт, который использует приложение), а тип сервиса — NodePort, то есть он будет доступен извне.
</b></details>

<details>
<summary>Правда или ложь? При выполнении следующей команды целевой порт будет открыт только на одном из узлов кластера Kubernetes, но трафик будет направляться на все Pod

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```
</summary><br><b>

Ложь. Порт будет открыт на каждом узле кластера, и трафик будет направляться на один из Pod (принадлежащих ReplicaSet)
</b></details>

<details>
<summary>Как проверить, что определённый Service настроен на перенаправление запросов к заданному Pod</summary><br><b>

Выполнить `kubectl describe service` и посмотреть, совпадают ли IP из "Endpoints" с какими-либо IP из вывода `kubectl get pod -o wide`
</b></details>

<details>
<summary>Объясните, что произойдёт при выполнении apply для следующего блока

```
apiVersion: v1
kind: Service
metadata:
  name: some-app
spec:
  type: NodePort
  ports:
  - port: 8080
    nodePort: 2017
    protocol: TCP
  selector:
    type: backend
    service: some-app
```
</summary><br><b>

Будет создан новый Service типа "NodePort", то есть его можно использовать для внутреннего и внешнего взаимодействия с приложением.<br>
Порт приложения — 8080, и запросы будут перенаправляться на этот порт. Открытый порт — 2017. Заметим, что указывать nodePort — не распространённая практика.<br>
Порт использует TCP (а не UDP), и это значение по умолчанию, так что его можно не указывать.<br>
Селектор используется Service, чтобы знать, на какие Pod перенаправлять запросы. В данном случае — на Pod с метками "type: backend" и "service: some-app".<br>
</b></details>

<details>
<summary>Как сделать следующий Service внешним?

```
spec:
  selector:
    app: some-app
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
```
</summary><br><b>

Добавить `type: LoadBalancer` и `nodePort`

```
spec:
  selector:
    app: some-app
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
      nodePort: 32412
```
</b></details>

<details>
<summary>Что использовать для маршрутизации трафика извне кластера Kubernetes к сервисам внутри кластера?</summary><br><b>

Ingress
</b></details>

<details>
<summary>Правда или ложь? При использовании "NodePort" автоматически создаётся "ClusterIP"?</summary><br><b>

Правда
</b></details>

<details>
<summary>Когда стоит использовать тип "LoadBalancer"</summary><br><b>

В основном когда нужно объединить его с балансировщиком нагрузки облачного провайдера
</b></details>

<details>
<summary>Как сопоставить Service с внешним адресом?</summary><br><b>

С помощью директивы 'ExternalName'.
</b></details>

<details>
<summary>Подробно опишите, что происходит при создании Service</summary><br><b>

1. Kubectl отправляет API-серверу запрос на создание Service
2. Контроллер обнаруживает, что появился новый Service
3. Контроллер создаёт объекты Endpoint с тем же именем, что и у сервиса
4. Контроллер использует селектор Service, чтобы определить конечные точки (endpoints)
5. kube-proxy обнаруживает новый объект endpoint + новый сервис и добавляет правила iptables, чтобы перехватывать трафик на порт Service и перенаправлять его на конечные точки
6. kube-dns обнаруживает, что появился новый Service, и добавляет запись контейнера на DNS-сервер
</b></details>

<details>
<summary>Как вывести список конечных точек (endpoints) определённого приложения?</summary><br><b>

`kubectl get ep <name>`
</b></details>

<details>
<summary>Как узнать информацию о Service, связанном с определённым Pod, если можно использовать только <code>kubectl exec <POD_NAME> -- </code></summary><br><b>

Можно выполнить `kubectl exec <POD_NAME> -- env`, что покажет несколько переменных окружения, относящихся к Service.<br>
Переменные вроде `[SERVICE_NAME]_SERVICE_HOST`, `[SERVICE_NAME]_SERVICE_PORT`, ...
</b></details>

<details>
<summary>Опишите, что происходит, когда контейнер впервые пытается подключиться к соответствующему ему Service. Объясните, кто добавил каждый из компонентов, упомянутых в описании</summary><br><b>

  - Контейнер смотрит на сервер имён (nameserver), указанный в /etc/resolv.conf
  - Контейнер отправляет запрос серверу имён, и адрес разрешается в IP Service
  - Запросы, отправленные на IP Service, перенаправляются на конечную(ые) точку(и) с помощью правил iptables (или другого выбранного ПО).

Кто их добавил:

  - Сервер имён в контейнере добавляется kubelet во время планирования Pod с использованием kube-dns
  - DNS-запись сервиса добавляется kube-dns при создании Service
  - Правила iptables добавляются kube-proxy при создании Endpoint и Service
</b></details>

<details>
<summary>На высоком уровне опишите, что происходит при выполнении <code>kubctl expose deployment remo --type=LoadBalancer --port 8080</code></summary><br><b>

1. Kubectl отправляет запрос в API Kubernetes на создание объекта Service
2. Kubernetes просит облачного провайдера (например, AWS, GCP, Azure) выделить балансировщик нагрузки
3. Только что созданный балансировщик нагрузки перенаправляет входящий трафик на соответствующий(ие) рабочий(ие) узел(ы), которые перенаправляют трафик в соответствующие контейнеры
</b></details>

<details>
<summary>Как после создания Service, перенаправляющего входящий внешний трафик в контейнеризованное приложение, убедиться, что он работает?</summary><br><b>

Можно выполнить `curl <SERVICE IP>:<SERVICE PORT>` и изучить вывод.
</b></details>

<details>
<summary>Внутренний балансировщик нагрузки в Kubernetes называется <code>____</code>, а внешний — <code>____</code></summary><br><b>

Внутренний балансировщик нагрузки в Kubernetes называется Service, а внешний — Ingress
</b></details>

### Ingress

<details>
<summary>Что такое Ingress?</summary><br><b>

Из документации Kubernetes: «Ingress предоставляет HTTP- и HTTPS-маршруты извне кластера к сервисам внутри кластера. Маршрутизация трафика управляется правилами, определёнными в ресурсе Ingress.»

Подробнее [здесь](https://kubernetes.io/docs/concepts/services-networking/ingress/)
</b></details>

<details>
<summary>Дополните следующий конфигурационный файл, чтобы получился Ingress

```
metadata:
  name: someapp-ingress
spec:
```
</summary><br><b>
Ответить на этот вопрос можно по-разному.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - backend:
          serviceName: someapp-internal-service
          servicePort: 8080
```
</b></details>


<details>
<summary>Объясните значение директив "http", "host" и "backend"

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - backend:
          serviceName: someapp-internal-service
          servicePort: 8080
```
</summary><br><b>

host — точка входа в кластер, то есть, по сути, корректный доменный адрес, который сопоставлен с IP-адресом узла кластера<br>
строка http указывает, что входящие запросы будут перенаправляться во внутренний сервис по http.<br>
backend ссылается на внутренний сервис (serviceName — имя из раздела metadata, а servicePort — порт из раздела ports).
</b></details>

<details>
<summary>Почему использование wildcard в host у ingress может привести к проблемам?</summary><br><b>

Не стоит использовать wildcard в host (например, `- host: *`), потому что так кластеру Kubernetes, по сути, указывается перенаправлять весь трафик в контейнер, для которого используется этот ingress. Это может привести к отказу всего кластера.
</b></details>

<details>
<summary>Что такое Ingress Controller?</summary><br><b>

Реализация Ingress. По сути, это ещё один Pod (или набор Pod), который оценивает и обрабатывает правила Ingress и таким образом управляет всеми перенаправлениями. 

Существует несколько реализаций Ingress Controller (реализация от Kubernetes — Kubernetes Nginx Ingress Controller).
</b></details>

<details>
<summary>В каких случаях используют Ingress?</summary><br><b>

* Несколько поддоменов (несколько записей host, у каждой свой сервис)
* Один домен с несколькими сервисами (несколько путей, каждый из которых сопоставлен с отдельным сервисом/приложением)
</b></details>

<details>
<summary>Как вывести список Ingress в своём пространстве имён?</summary><br><b>

kubectl get ingress
</b></details>

<details>
<summary>Что такое Ingress Default Backend?</summary><br><b>

Он определяет, что делать с входящим в кластер Kubernetes запросом, который не сопоставлен ни с одним backend (= нет правила, сопоставляющего запрос с сервисом). Если сервис default backend не определён, рекомендуется его определить, чтобы пользователи всё же видели какое-то сообщение, а не пустоту или непонятную ошибку.
</b></details>

<details>
<summary>Как настроить default backend?</summary><br><b>

Создать ресурс Service, в котором указано имя default backend, как оно отображается в `kubectl describe ingress ...`, и порт в разделе ports.
</b></details>

<details>
<summary>Как настроить TLS для Ingress?</summary><br><b>

Добавить записи tls и secretName.

```
spec:
  tls:
  - hosts:
    - some_app.com
    secretName: someapp-secret-tls
```
</b></details>

<details>
<summary>Правда или ложь? При настройке Ingress с TLS компонент Secret должен находиться в том же пространстве имён, что и компонент Ingress</summary><br><b>

Правда
</b></details>

<details>
<summary>Какое понятие Kubernetes использовать для управления потоком трафика на уровне IP-адресов или портов? </summary><br><b>

Network Policies
</b></details>

<details>
<summary>Как масштабировать приложение (Deployment), чтобы работал более чем один экземпляр приложения?</summary><br><b>

Чтобы запустить два экземпляра приложения?

`kubectl scale deployment <DEPLOYMENT_NAME> --replicas=2`

Можно указать любое другое число, при условии что приложение умеет масштабироваться.
</b></details>

### ReplicaSets

<details>
<summary>Для чего нужен ReplicaSet?</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset): «Назначение ReplicaSet — поддерживать стабильный набор реплик Pod, работающих в любой момент времени. Поэтому его часто используют, чтобы гарантировать доступность заданного количества идентичных Pod.»

Проще говоря, ReplicaSet гарантирует, что для выбранного Pod работает заданное количество реплик. Если Pod больше, чем определено в ReplicaSet, часть из них будет удалена. Если меньше, чем определено в ReplicaSet, будут добавлены новые реплики.
</b></details>

<details>
<summary>Что делает следующий блок строк?

```
spec:
  replicas: 2
  selector:
    matchLabels:
      type: backend
  template:
    metadata:
      labels:
        type: backend
    spec:
      containers:
      - name: httpd-yup
        image: httpd
```
</summary><br><b>

Он определяет ReplicaSet для Pod, у которых type установлен в "backend", так что в любой момент времени будут одновременно работать 2 Pod.
</b></details>

<details>
<summary>Что произойдёт, если Pod, созданный ReplicaSet, удалить напрямую с помощью <code>kubectl delete po ...</code>?</summary><br><b>

ReplicaSet создаст новый Pod, чтобы достичь желаемого количества реплик.
</b></details>

<details>
<summary>Правда или ложь? Если ReplicaSet определяет 2 реплики, но работают 3 Pod, соответствующих селектору ReplicaSet, он ничего не будет делать</summary><br><b>

Ложь. Он завершит один из Pod, чтобы достичь желаемого состояния в 2 реплики.
</b></details>

<details>
<summary>Опишите последовательность событий при создании ReplicaSet</summary><br><b>

* Клиент (например, kubectl) отправляет API-серверу запрос на создание ReplicaSet
* Контроллер обнаруживает новое событие с запросом ReplicaSet
* Контроллер создаёт новые определения Pod (точное количество зависит от того, что задано в определении ReplicaSet)
* Планировщик обнаруживает неназначенные Pod и решает, на какие узлы их назначить. Эта информация отправляется API-серверу
* Kubelet обнаруживает, что на узел, где он работает, назначены два Pod (поскольку он постоянно отслеживает API-сервер)
* Kubelet отправляет запросы движку контейнеров на создание контейнеров, входящих в Pod
* Kubelet отправляет API-серверу запрос, чтобы сообщить, что Pod созданы
</b></details>

<details>
<summary>Как вывести список ReplicaSet в текущем пространстве имён?</summary><br><b>

`kubectl get rs`
</b></details>

<details>
<summary>Можно ли удалить ReplicaSet, не удаляя созданные им Pod?</summary><br><b>

Да, с помощью `--cascase=false`.

`kubectl delete -f rs.yaml --cascade=false`
</b></details>

<details>
<summary>Какое количество реплик используется по умолчанию, если оно не указано явно?</summary><br><b>

1
</b></details>

<details>
<summary>Что означает следующий вывод <code>kubectl get rs</code>?

NAME                    DESIRED   CURRENT   READY   AGE
web                     2         2         0       2m23s
</summary><br><b>

У ReplicaSet `web` 2 реплики. Похоже, контейнеры внутри Pod ещё не запущены, поскольку значение READY равно 0. Это может быть нормально, так как некоторым контейнерам нужно время на запуск, а может быть вызвано ошибкой. Выполнение `kubectl describe po POD_NAME` или `kubectl logs POD_NAME` даст больше информации.
</b></details>

<details>
<summary>Правда или ложь? Pod, указанные в поле selector у ReplicaSet, должны быть созданы самим ReplicaSet</summary><br><b>

Ложь. Pod могут уже работать, и изначально их мог создать любой объект. Для ReplicaSet это не важно и не является условием для того, чтобы взять их под контроль и отслеживать.
</b></details>

<details>
<summary>Правда или ложь? Если Pod, указанных в поле selector у ReplicaSet, не существует, ReplicaSet будет ждать их запуска, прежде чем что-либо делать</summary><br><b>

Ложь. Он сам позаботится о запуске недостающих Pod.
</b></details>

<details>
<summary>Какое поле в разделе spec обязательно для ReplicaSet?</summary><br><b>

Поле `template` в разделе spec обязательно. ReplicaSet использует его для создания новых Pod при необходимости.
</b></details>

<details>
<summary>После создания ReplicaSet как проверить, нашёл ли он подходящие Pod или создал новые?</summary><br><b>

`kubectl describe rs <ReplicaSet Name>`

Это будет видно в разделе `Events` (в самых последних строках)
</b></details>

<details>
<summary>Правда или ложь? Удаление ReplicaSet удалит созданные им Pod</summary><br><b>

Правда (и не только Pod, но и всё остальное, что он создал).
</b></details>

<details>
<summary>Правда или ложь? Удаление метки у Pod, который отслеживается ReplicaSet, приведёт к тому, что ReplicaSet создаст новый Pod</summary><br><b>

Правда. Когда метка, используемая ReplicaSet в поле selector, удаляется у Pod, этот Pod больше не управляется ReplicaSet, и ReplicaSet создаст новый Pod взамен «потерянного».
</b></details>

<details>
<summary>Как масштабировать Deployment до 8 реплик?</code></summary><br><b>

kubectl scale deploy <DEPLOYMENT_NAME> --replicas=8
</b></details>

<details>
<summary>ReplicaSet работают с того момента, как пользователь выполнил команду их создания (например, <code>kubectl create -f rs.yaml</code>)</summary><br><b>

Ложь. Это может занять некоторое время, в зависимости от того, что именно запускается. Чтобы проверить, запущены ли они и работают ли, выполнить `kubectl get rs` и посмотреть на столбец 'READY'.
</b></details>

<details>
<summary>Как открыть доступ к ReplicaSet в виде нового сервиса?</summary><br><b>

`kubectl expose rs <ReplicaSet Name> --name=<Service Name> --target-port=<Port to expose> --type=NodePort`

Несколько замечаний:
  - целевой порт зависит от того, какой порт приложение использует в контейнере
  - тип может быть другим и не обязательно должен быть именно "NodePort"
</b></details>

<details>
<summary>Исправьте следующее определение ReplicaSet

```yaml
apiVersion: apps/v1
kind: ReplicaCet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: cachy
    spec:
      containers:
      - name: redis
        image: redis
```
</summary><br><b>

kind должен быть ReplicaSet, а не ReplicaCet :)
</b></details>

<details>
<summary>Исправьте следующее определение ReplicaSet

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: cachy
    spec:
      containers:
      - name: redis
        image: redis
```
</summary><br><b>

Селектор не совпадает с меткой (cache и cachy). Чтобы исправить, заменить cachy на cache.
</b></details>

<details>
<summary>Как проверить, какой образ контейнера используется в ReplicaSet с именем "repli"?</summary><br><b>

`k describe rs repli | grep -i image`
</b></details>

<details>
<summary>Как проверить, сколько Pod в ReplicaSet с именем "repli" находятся в состоянии готовности?</summary><br><b>

`k describe rs repli | grep -i "Pods Status"`
</b></details>

<details>
<summary>Как удалить ReplicaSet с именем "rori"?</summary><br><b>

`k delete rs rori`
</b></details>

<details>
<summary>Как изменить ReplicaSet с именем "rori", чтобы он использовал другой образ?</summary><br><b>

`k edis rs rori`
</b></details>

<details>
<summary>Увеличьте масштаб ReplicaSet с именем "rori", чтобы он запускал 5 Pod вместо 2</summary><br><b>

`k scale rs rori --replicas=5`
</b></details>

<details>
<summary>Уменьшите масштаб ReplicaSet с именем "rori", чтобы он запускал 1 Pod вместо 5</summary><br><b>

`k scale rs rori --replicas=1`
</b></details>

### DaemonSet

<details>
<summary>Что такое DaemonSet?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset): «DaemonSet гарантирует, что на всех (или некоторых) узлах работает копия Pod. По мере добавления узлов в кластер на них добавляются Pod. По мере удаления узлов из кластера эти Pod удаляются сборщиком мусора. Удаление DaemonSet приводит к удалению созданных им Pod.»
</b></details>

<details>
<summary>В чём разница между ReplicaSet и DaemonSet?</summary><br><b>

Назначение ReplicaSet — поддерживать стабильный набор реплик Pod, работающих в любой момент времени.
DaemonSet гарантирует, что на всех узлах работает копия Pod. 
</b></details>

<details>
<summary>В каких случаях используют DaemonSet?</summary><br><b>

* Мониторинг: нужно вести мониторинг на каждом узле кластера. Например, Pod datadog работает на каждом узле с помощью DaemonSet
* Логирование: нужно настроить логирование на каждом узле кластера
* Сеть: есть сетевой компонент, который нужен на каждом узле, чтобы все узлы могли взаимодействовать друг с другом
</b></details>

<details>
<summary>Как работает DaemonSet?</summary><br><b>

Исторически, до версии 1.12, это делалось с помощью атрибута NodeName.

Начиная с 1.12, это достигается обычным планировщиком и node affinity.
</b></details>

#### DaemonSet - команды

<details>
<summary>Как вывести список всех DaemonSet в текущем пространстве имён?</summary><br><b>

`kubectl get ds`
</b></details>

### StatefulSet

<details>
<summary>Объясните, что такое StatefulSet</summary><br><b>

StatefulSet — это объект API рабочей нагрузки (workload), используемый для управления stateful-приложениями. Управляет развёртыванием и масштабированием набора Pod и даёт гарантии относительно порядка и уникальности этих Pod.[Подробнее](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
</b></details>

### Хранилище (Storage)

#### Тома (Volumes)

<details>
<summary>Что такое том (volume) применительно к Kubernetes?</summary><br><b>

Каталог, доступный контейнерам внутри определённого Pod. Механизм, отвечающий за создание каталога, управление им и т.д., в основном зависит от типа тома.

</b></details>

<details>
<summary>Какие типы томов известны?</summary><br><b>

* emptyDir: создаётся, когда Pod назначается на узел, и перестаёт существовать, когда Pod больше не работает на этом узле
* hostPath: монтирует путь с самого хоста. Обычно не используется из-за рисков безопасности, но есть ряд случаев, когда он нужен, например доступ к некоторым внутренним путям хоста (`/sys`, `/var/lib` и т.д.)

</b></details>

<details>
<summary>Какие проблемы решают тома в Kubernetes?</summary><br><b>

1. Совместное использование файлов контейнерами, работающими в одном Pod
2. Хранилище в контейнерах эфемерно — обычно оно существует недолго. Например, при падении контейнера теряются все данные на диске. Некоторые тома позволяют справиться с такой ситуацией с помощью persistent volumes

</b></details>

<details>
<summary>Объясните разницу между эфемерными типами томов и persistent volumes применительно к Pod</summary><br><b>

Эфемерные типы томов живут столько же, сколько Pod, в отличие от persistent volumes, которые существуют и после окончания жизни Pod.

</b></details>

<details>
<summary>Приведите хотя бы один сценарий использования для каждого из следующих типов томов:

* emptyDir
* hostPath
</summary><br><b>

* EmptyDir: нужны временные данные, потерю которых при удалении Pod можно допустить. Например, кратковременные данные, необходимые для разовых операций.
* hostPath: нужен доступ к путям на самом хосте (например, к данным из `/sys` или данным, генерируемым в `/var/lib`)
</b></details>

### Сеть

<details>
<summary>Правда или ложь? По умолчанию два Pod в двух разных пространствах имён не могут взаимодействовать</summary><br><b>

Ложь. По умолчанию два Pod в двух разных пространствах имён могут взаимодействовать друг с другом.

Можно проверить самостоятельно:

kubectl run test-prod -n prod --image ubuntu -- sleep 2000000000
kubectl run test-dev -n dev --image ubuntu -- sleep 2000000000

`k describe po test-prod -n prod`, чтобы получить IP Pod test-prod.

Зайти в Pod dev: `kubectl exec --stdin --tty test-dev -n dev -- /bin/bash`

И выполнить ping IP Pod test-prod, полученного ранее. Будет видно, что два Pod в двух разных пространствах имён взаимодействуют.

</b></details>

### Сетевые политики (Network Policies)

<details>
<summary>Объясните, что такое Network Policies</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies): «NetworkPolicies — это конструкция, ориентированная на приложения, которая позволяет указать, как Pod разрешено взаимодействовать с различными сетевыми «сущностями»...»

Проще говоря, Network Policies определяют, как Pod разрешено/запрещено взаимодействовать друг с другом и/или с другими сетевыми конечными точками.

</b></details>

<details>
<summary>В каких случаях используют Network Policies?</summary><br><b>

  - Безопасность: из соображений безопасности нужно запретить всем взаимодействовать с определённым Pod
  - Управление сетевым трафиком: нужно запретить сетевой поток между двумя определёнными узлами

</b></details>

<details>
<summary>Правда или ложь? Если к Pod не применено ни одной сетевой политики, то никакие соединения к нему или от него не разрешены</summary><br><b>

Ложь. По умолчанию Pod не изолированы.
</b></details>

<details>
<summary>Есть два Pod: на источнике действует egress-политика, запрещающая трафик, а на получателе — ingress-политика, разрешающая трафик. Будет ли трафик разрешён или запрещён?</summary><br><b>

Запрещён. Чтобы трафик был разрешён, его должны разрешать политики и источника, и получателя.
</b></details>

<details>
<summary>Где кластер Kubernetes хранит состояние кластера?</summary><br><b>

etcd
</b></details>

### etcd

<details>
<summary>Что такое etcd?</summary><br><b>

etcd — это распределённое хранилище ключ-значение с открытым исходным кодом, используемое для хранения и управления критически важной информацией, необходимой распределённым системам для продолжения работы.

[Подробнее здесь](https://www.redhat.com/en/topics/containers/what-is-etcd)

</b></details>

<details>
<summary>Правда или ложь? Etcd хранит текущее состояние любого компонента Kubernetes</summary><br><b>

Правда
</b></details>

<details>
<summary>Правда или ложь? API-сервер — единственный компонент, который напрямую взаимодействует с etcd</summary><br><b>

Правда
</b></details>

<details>
<summary>Правда или ложь? Данные приложений не хранятся в etcd</summary><br><b>

Правда
</b></details>

<details>
<summary>Почему etcd? Почему не какая-нибудь SQL- или NoSQL-база данных?</summary><br><b>

Когда etcd выбрали в качестве хранилища данных, оно было (и, конечно, остаётся):

* Высокодоступным (Highly Available) — можно развернуть несколько узлов
* Полностью реплицируемым (Fully Replicated) — любой узел кластера etcd является «основным» (primary) и имеет полный доступ к данным
* Согласованным (Consistent) — чтение возвращает самые свежие данные
* Защищённым (Secured) — поддерживает и TLS, и SSL
* Быстрым (Speed) — высокопроизводительное хранилище данных (10 тыс. записей в секунду!)
</b></details>

### Пространства имён (Namespaces)

<details>
<summary>Что такое пространства имён (namespaces)?</summary><br><b>

Пространства имён позволяют разделить кластер на виртуальные кластеры, в которых приложения можно сгруппировать осмысленным образом, полностью отделив их от других групп (так что, например, можно создать приложение с одним и тем же именем в двух разных пространствах имён)
</b></details>

<details>
<summary>Зачем использовать пространства имён? Чем плохо использовать одно пространство имён default?</summary><br><b>

При использовании только пространства имён default со временем становится сложно получить общее представление обо всех приложениях, которыми управляешь в кластере. Пространства имён упрощают организацию приложений в осмысленные группы, например пространство имён для всех приложений мониторинга, пространство имён для всех приложений безопасности и т.д.

Пространства имён также полезны для управления окружениями Blue/Green: каждое пространство имён может содержать свою версию приложения и при этом совместно использовать ресурсы из других пространств имён (например, logging, monitoring и т.д.).

Ещё один сценарий использования пространств имён — один кластер, несколько команд. Когда несколько команд используют один кластер, они могут мешать друг другу. Например, если они создадут приложение с одинаковым именем, это значит, что одна из команд перезапишет приложение другой, потому что в Kubernetes не может быть двух приложений с одинаковым именем (в одном пространстве имён).
</b></details>

<details>
<summary>Правда или ложь? При удалении пространства имён все ресурсы в нём не удаляются, а переносятся в другое пространство имён по умолчанию</summary><br><b>

Ложь. При удалении пространства имён ресурсы в нём тоже удаляются.
</b></details>

<details>
<summary>Какие специальные пространства имён существуют по умолчанию при создании кластера Kubernetes?</summary><br><b>

* default
* kube-system
* kube-public
* kube-node-lease
</b></details>

<details>
<summary>Что можно найти в пространстве имён kube-system?</summary><br><b>

* Процессы Master и Kubectl
* Системные процессы
</b></details>

<details>
<summary>Хотя пространства имён задают область видимости для ресурсов, они их не изолируют</summary><br><b>

Правда. Например, можно создать два Pod в двух разных пространствах имён — будет видно, что между ними есть связь.
</b></details>

#### Пространства имён - команды

<details>
<summary>Как вывести список всех пространств имён?</code></summary><br><b>

`kubectl get namespaces` ИЛИ `kubectl get ns`

</b></details>

<details>
<summary>Создайте пространство имён с именем 'alle'</summary><br><b>

`k create ns alle`

</b></details>

<details>
<summary>Проверьте, сколько существует пространств имён</summary><br><b>

`k get ns --no-headers | wc -l`

</b></details>

<details>
<summary>Проверьте, сколько Pod существует в пространстве имён "dev"</summary><br><b>

`k get po -n dev`

</b></details>

<details>
<summary>Создайте Pod с именем "kartos" в пространстве имён dev. Pod должен использовать образ "redis".</summary><br><b>

Если пространства имён ещё нет: `k create ns dev`

`k run kratos --image=redis -n dev`

</b></details>

<details>
<summary>Нужно найти Pod с именем "atreus". Как проверить, в каком пространстве имён он работает?</summary><br><b>

`k get po -A | grep atreus`

</b></details>

<details>
<summary>Что содержит kube-public?</summary><br><b>

* ConfigMap с информацией о кластере
* Общедоступные данные
</b></details>

<details>
<summary>Как получить имя текущего пространства имён?</code></summary><br><b>

`kubectl config view | grep namespace`
</b></details>

<details>
<summary>Что содержит kube-node-lease?</summary><br><b>

Он хранит информацию о heartbeat-сигналах узлов. Для каждого узла создаётся объект, хранящий информацию о его доступности.
</b></details>

<details>
<summary>Правда или ложь? С помощью пространств имён можно ограничивать ресурсы, потребляемые пользователями/командами</summary><br><b>

Правда. С помощью пространств имён можно ограничить использование CPU, RAM и хранилища.
</b></details>

<details>
<summary>Как переключиться на другое пространство имён? Другими словами, как сменить активное пространство имён?</code></summary><br><b>

`kubectl config set-context --current --namespace=some-namespace` и проверить с помощью `kubectl config view --minify | grep namespace:`

ИЛИ

`kubens some-namespace`
</b></details>

#### Квоты ресурсов (Resources Quota)

<details>
<summary>Что такое Resource Quota?</code></summary><br><b>
  
Resource quota задаёт ограничения на суммарное потребление ресурсов в пространстве имён. Она может ограничивать количество объектов каждого типа, которые можно создать в пространстве имён, а также общий объём вычислительных ресурсов, которые могут потреблять ресурсы этого пространства имён.
</b></details>

<details>
<summary>Как создать Resource Quota?</code></summary><br><b>

kubectl create quota some-quota --hard-cpu=2,pods=2
</b></details>

<details>
<summary>Какие ресурсы доступны из разных пространств имён?</code></summary><br><b>

Services.
</b></details>

<details>
<summary>На какой сервис и в каком пространстве имён ссылается следующий файл?

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
data:
  some_url: samurai.jack
```
</summary><br><b>

Он ссылается на сервис "samurai" в пространстве имён "jack".
</b></details>

<details>
<summary>Какие компоненты нельзя создать внутри пространства имён?</code></summary><br><b>

Volume и Node.
</b></details>

<details>
<summary>Как вывести список всех компонентов, привязанных к пространству имён?</code></summary><br><b>

`kubectl api-resources --namespaced=true`
</b></details>

<details>
<summary>Как создавать компоненты в пространстве имён?</code></summary><br><b>

Один способ — указать --namespace, например так: `kubectl apply -f my_component.yaml --namespace=some-namespace`
Другой способ — указать его в самом YAML:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
  namespace: some-namespace
```

и проверить можно с помощью: `kubectl get configmap -n some-namespace`
</b></details>

<details>
<summary>Как выполнить команду "ls" в существующем Pod?</code></summary><br><b>

kubectl exec some-pod -it -- ls
</b></details>

<details>
<summary>Как создать сервис, открывающий доступ к Deployment?</code></summary><br><b>

kubectl expose deploy some-deployment --port=80 --target-port=8080
</b></details>

<details>
<summary>Как создать Pod и сервис одной командой?</code></summary><br><b>

kubectl run nginx --image=nginx --restart=Never --port 80 --expose
</b></details>

<details>
<summary>Подробно опишите, что делает следующая команда: <code>kubectl create deployment kubernetes-httpd --image=httpd</code></summary><br><b>
</b></details>

<details>
<summary>Зачем создавать объект kind Deployment, если Pod можно запускать с помощью ReplicaSet?</summary><br><b>
</b></details>

<details>
<summary>Как получить список ресурсов, которые не привязаны к конкретному пространству имён?</code></summary><br><b>

kubectl api-resources --namespaced=false
</b></details>

<details>
<summary>Как удалить все Pod, статус которых не "Running"?</code></summary><br><b>

kubectl delete pods --field-selector=status.phase!='Running'
</b></details>

<details>
<summary>Как отобразить потребление ресурсов Pod?</summary><br><b>

kubectl top pod
</b></details>

<details>
<summary>Возможно, общий вопрос, но: есть подозрение, что у одного из Pod проблемы, и непонятно, какие именно. Что делать?</summary><br><b>

Начать с проверки статуса Pod. Можно использовать команду `kubectl get pods` (--all-namespaces для Pod в системном пространстве имён)<br>

Если виден статус "Error", можно продолжить отладку с помощью команды `kubectl describe pod [name]`. Если и это не дало ничего полезного, можно попробовать stern для просмотра логов в реальном времени (log tailing).<br>

Если выяснится, что была временная проблема с Pod или системой, можно попробовать перезапустить Pod следующим образом: `kubectl scale deployment [name] --replicas=0`<br>

Установка числа реплик в 0 остановит процесс. Теперь запустить его снова: `kubectl scale deployment [name] --replicas=1`
</b></details>

<details>
<summary>Что происходит, когда Pod используют слишком много памяти? (больше своего лимита)</summary><br><b>

Они становятся кандидатами на завершение.
</b></details>

<details>
<summary>Опишите, как работает откат (roll-back)</summary><br><b>
</b></details>

<details>
<summary>Правда или ложь? Память — сжимаемый (compressible) ресурс, то есть когда контейнер достигает лимита памяти, он продолжит работать</summary><br><b>

Ложь. CPU — сжимаемый ресурс, а память — несжимаемый: как только контейнер достигает лимита памяти, он будет завершён.
</b></details>

### Операторы (Operators)

<details>
<summary>Что такое оператор (Operator)?</summary><br><b>

Объяснение [здесь](https://kubernetes.io/docs/concepts/extend-kubernetes/operator)

«Операторы — это программные расширения Kubernetes, которые используют пользовательские ресурсы (custom resources) для управления приложениями и их компонентами. Операторы следуют принципам Kubernetes, в частности принципу цикла управления (control loop).»

Проще говоря, оператор можно рассматривать как пользовательский цикл управления в Kubernetes.
</b></details>

<details>
<summary>Зачем нужны операторы?</summary><br><b>

Управлять stateful-приложениями в Kubernetes не так просто, как stateless-приложениями, где достижение желаемого состояния и обновления обрабатываются одинаково для каждой реплики. В stateful-приложениях обновление каждой реплики может требовать особой обработки из-за природы приложения с состоянием: каждая реплика может находиться в своём состоянии. Поэтому для управления stateful-приложениями часто нужен человек-оператор. Kubernetes Operator призван помочь с этим.

Это также помогает автоматизировать стандартный процесс на нескольких кластерах Kubernetes
</b></details>

<details>
<summary>Из каких компонентов состоит оператор?</summary><br><b>

1. CRD (Custom Resource Definition) — известны ресурсы Kubernetes, такие как Deployment, Pod, Service и т.д. CRD — тоже ресурс, но такой, который определяет сам пользователь или разработчик оператора.
2. Controller — пользовательский цикл управления, работающий с CRD

</b></details>

<details>
<summary>Объясните, что такое CRD</summary><br><b>

CRD — это Custom Resource Definitions. Это пользовательский компонент Kubernetes, который расширяет API K8s.

TODO(abregman): добавить больше информации.

</b></details>

<details>
<summary>Как работает оператор?</summary><br><b>

Он использует цикл управления, который применяется в Kubernetes в целом. Он отслеживает изменения в состоянии приложения. Разница в том, что используется пользовательский цикл управления.

Кроме того, он использует CRD (Custom Resources Definitions), то есть, по сути, расширяет API Kubernetes.

</b></details>

<details>
<summary>Правда или ложь? Kubernetes Operator используется для stateful-приложений</summary><br><b>

Правда
</b></details>

<details>
<summary>Объясните, что такое OLM (Operator Lifecycle Manager) и для чего он используется</summary><br><b>

</b></details>

<details>
<summary>Что такое Operator Framework?</summary><br><b>

Набор инструментов с открытым исходным кодом для автоматизированного и эффективного управления нативными приложениями k8s, которые называются операторами.

</b></details>

<details>
<summary>Из каких компонентов состоит Operator Framework?</summary><br><b>

1. Operator SDK — позволяет разработчикам создавать операторы
2. Operator Lifecycle Manager — помогает устанавливать, обновлять и в целом управлять жизненным циклом всех операторов
3. Operator Metering — обеспечивает отчётность об использовании для операторов, предоставляющих специализированные сервисы
4. 
</b></details>

<details>
<summary>Подробно опишите, что такое Operator Lifecycle Manager</summary><br><b>

Это часть Operator Framework, используемая для управления жизненным циклом операторов. По сути, он расширяет Kubernetes так, что пользователь может декларативно управлять операторами (установка, обновление, ...).

</b></details>

<details>
<summary>Что входит в пространство имён openshift-operator-lifecycle-manager?</summary><br><b>

В него входят:

  * catalog-operator — разрешает и устанавливает ClusterServiceVersions и указанные в них ресурсы.
  * olm-operator — развёртывает приложения, определённые ресурсом ClusterServiceVersion

</b></details>

<details>
<summary>Что такое kubconfig? Для чего он используется?</summary><br><b>
  
Файл kubeconfig — это файл, используемый для настройки доступа к Kubernetes при работе с инструментом командной строки kubectl (или другими клиентами).
Файлы kubeconfig используются для организации информации о кластерах, пользователях, пространствах имён и механизмах аутентификации.
</b></details>

<details>
<summary>Что использовать для создания оператора — Helm, Go или что-то ещё?</summary><br><b>
  
Зависит от охвата и зрелости оператора. Если он в основном покрывает установку и обновления, может хватить Helm. Если нужно управление жизненным циклом, аналитика (insights) и режим автопилота (auto-pilot), здесь, вероятно, стоит использовать Go.
</b></details>

<details>
<summary>Какие инструменты и проекты используются для создания операторов?</summary><br><b>

Этот ответ больше зависит от личного опыта и вкуса...

* Operator Framework
* Kubebuilder
* Controller Runtime
...
</b></details>

### Secrets

<details>
<summary>Объясните, что такое Secrets в Kubernetes</summary><br><b>

Secrets позволяют хранить конфиденциальную информацию (пароли, ssh-ключи и т.д.) и управлять ею

</b></details>

<details>
<summary>Как создать Secret из ключа и значения?</summary><br><b>

`kubectl create secret generic some-secret --from-literal=password='donttellmypassword'`

</b></details>

<details>
<summary>Как создать Secret из файла?</summary><br><b>

`kubectl create secret generic some-secret --from-file=/some/file.txt`
</b></details>

<details>
<summary>Что означает <code>type: Opaque</code> в файле Secret? Какие ещё бывают типы?</summary><br><b>

Opaque — тип по умолчанию, используемый для пар ключ-значение.
</b></details>

<details>
<summary>Правда или ложь? Хранение данных в компоненте Secret автоматически делает их защищёнными</summary><br><b>

Ложь. Некоторые известные механизмы безопасности, например «шифрование», по умолчанию не включены.
</b></details>

<details>
<summary>Что не так со следующим файлом Secret:

```
apiVersion: v1   
kind: Secret
metadata:
    name: some-secret
type: Opaque
data:
    password: mySecretPassword
```
</summary><br><b>

Пароль не зашифрован.
Нужно выполнить что-то вроде `echo -n 'mySecretPassword' | base64` и вставить результат в файл вместо открытого текста.

</b></details>

<details>
<summary>Что означает следующий фрагмент в конфигурационном файле Deployment? 

```
spec:
  containers:
    - name: USER_PASSWORD
      valueFrom:
        secretKeyRef:
          name: some-secret
          key: password
```
</summary><br><b>

Переменная окружения USER_PASSWORD будет хранить значение ключа password из секрета с именем "some-secret"
Другими словами, это ссылка на значение из Kubernetes Secret.

</b></details>

<details>
<summary>Как коммитить секреты в Git и вообще как использовать зашифрованные секреты?</summary><br><b>

Возможный процесс выглядит так:

1. Создать Kubernetes secret (но не коммитить его)
2. Зашифровать его с помощью стороннего проекта (например, kubeseal)
3. Применить запечатанный/зашифрованный секрет
4. Закоммитить запечатанный (sealed) секрет в Git
5. Развернуть приложение, которому нужен секрет, — он может быть автоматически расшифрован, например, с помощью контроллера Bitnami Sealed secrets
</b></details>

### Тома (Volumes)

<details>
<summary>Правда или ложь? Kubernetes «из коробки» обеспечивает сохранность данных, поэтому при перезапуске Pod данные сохраняются</summary><br><b>

Ложь
</b></details>

<details>
<summary>Объясните, что такое "Persistent Volumes". Зачем они нужны?</summary><br><b>

Persistent Volumes позволяют сохранять данные, то есть, по сути, предоставляют хранилище, не зависящее от жизненного цикла Pod.
</b></details>

<details>
<summary>Правда или ложь? Persistent Volume должен быть доступен всем узлам, потому что Pod может перезапуститься на любом из них</summary><br><b>

Правда
</b></details>

<details>
<summary>Какие типы persistent volumes существуют?</summary><br><b>

* NFS
* iSCSI
* CephFS
* ...
</b></details>

<details>
<summary>Что такое PersistentVolumeClaim?</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое Volume Snapshots</summary><br><b>
  
Volume snapshots позволяют создать копию тома на определённый момент времени.
</b></details>

<details>
<summary>Правда или ложь? Kubernetes управляет сохранностью данных</summary><br><b>

Ложь
</b></details>

<details>
<summary>Объясните, что такое Storage Classes</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое "Dynamic Provisioning" и "Static Provisioning"</summary><br><b>
  
Основное различие — в том, в какой момент нужно настроить хранилище. Например, если нужно заранее заполнить том данными, выбирают статическое выделение (static provisioning). А если тома нужно создавать по запросу, выбирают динамическое выделение (dynamic provisioning).
</b></details>

<details>
<summary>Объясните, что такое режимы доступа (Access Modes)</summary><br><b>
</b></details>

<details>
<summary>Что такое CSI Volume Cloning?</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое "Ephemeral Volumes"</summary><br><b>
</b></details>

<details>
<summary>Какие типы эфемерных томов поддерживает Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>Что такое Reclaim Policy?</summary><br><b>
</b></details>

<details>
<summary>Какие бывают политики освобождения (reclaim policies)?</summary><br><b>

* Retain
* Recycle
* Delete
</b></details>

### Управление доступом

<details>
<summary>Что такое RBAC?</summary><br><b>
 
RBAC в Kubernetes — это механизм, который позволяет настраивать детальные и конкретные наборы прав, определяющие, как заданный пользователь или группа пользователей может взаимодействовать с любым объектом Kubernetes в кластере или в определённом пространстве имён (Namespace) кластера.
</b></details>

<details>
<summary>Объясните, что такое объекты <code>Role</code> и <code>RoleBinding"</code></summary><br><b>
</b></details>

<details>
<summary>В чём разница между объектами <code>Role</code> и <code>ClusterRole</code>?</summary><br><b>
  
Разница в том, что Role используется на уровне пространства имён, а ClusterRole — для всего кластера.
</b></details>

<details>
<summary>Объясните, что такое "Service Accounts" и в каком сценарии их стоит создавать/использовать</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account): «Сервисная учётная запись (service account) предоставляет идентичность процессам, работающим в Pod.»

Пример, когда она нужна:
Определяется пайплайн, который должен собрать и отправить (push) образ. Чтобы иметь достаточные права для сборки и отправки образа, пайплайну потребуется service account с достаточными правами.
</b></details>

<details>
<summary>Что происходит, если создать Pod и НЕ указать service account?</summary><br><b>

Pod автоматически назначается service account по умолчанию (в пространстве имён, где работает Pod).
</b></details>

<details>
<summary>Объясните, чем Service Accounts отличаются от User Accounts</summary><br><b>

  - User accounts глобальны, а Service accounts уникальны в пределах пространства имён
  - User accounts предназначены для людей или клиентских процессов, а Service accounts — для процессов, работающих в Pod
</b></details>

<details>
<summary>Как вывести список Service Accounts?</summary><br><b>

`kubectl get serviceaccounts`
</b></details>

<details>
<summary>Объясните, что такое "Security Context"</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/security-context): «Контекст безопасности (security context) определяет настройки привилегий и управления доступом для Pod или контейнера.»
</b></details>

### Паттерны



### CronJob

<details>
<summary>Объясните, что такое CronJob и для чего он используется</summary><br><b>
  
CronJob создаёт Job по повторяющемуся расписанию. Один объект CronJob похож на одну строку файла crontab (cron table). Он периодически запускает задание (job) по заданному расписанию, записанному в формате Cron.
</b></details>

<details>
<summary>Какая проблема может возникнуть при использовании следующей спецификации и как её исправить?

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: some-cron-job
spec:
  schedule: '*/1 * * * *'
  startingDeadlineSeconds: 10
  concurrencyPolicy: Allow
```
</summary><br><b>

Если cron job завершится с ошибкой, следующий job не заменит предыдущий из-за значения "concurrencyPolicy", равного "Allow". Будут порождаться всё новые job, и в итоге система заполнится упавшими cron job.
Чтобы избежать этой проблемы, значение "concurrencyPolicy" должно быть "Replace" или "Forbid".
</b></details>

<details>
<summary>Какая проблема может возникнуть при использовании следующего CronJob и как её исправить?

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: "some-cron-job"
spec:
  schedule: '*/1 * * * *'
jobTemplate:
  spec:
    template:
      spec:
      restartPolicy: Never
      concurrencyPolicy: Forbid
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
```
</summary><br><b>

Следующие строки размещены внутри template:

```
concurrencyPolicy: Forbid
successfulJobsHistoryLimit: 1
failedJobsHistoryLimit: 1
```

В результате эта конфигурация не входит в spec cron job, поэтому у cron job нет ограничений, что может вызвать проблемы вроде OOM и потенциально привести к отказу API-сервера.<br>
Чтобы исправить это, эти строки нужно поместить в spec cron job — выше или ниже директивы "schedule" в примере выше.
</b></details>

###  Разное

<details>
<summary>Объясните разницу между императивным (Imperative) и декларативным (Declarative) управлением</summary><br><b>

</b></details>

<details>
<summary>Объясните, что означает Service Discovery в Kubernetes</summary><br><b>
</b></details>

<details>
<summary>Есть один кластер Kubernetes и несколько команд, которые хотят его использовать. Нужно ограничить ресурсы, которые каждая команда потребляет в кластере. Какое понятие Kubernetes для этого использовать?</summary><br><b>

Пространства имён (Namespaces) позволят ограничить ресурсы, а также избежать конфликтов между командами при работе в кластере (например, при создании приложения с одинаковым именем).
</b></details>

<details>
<summary>Что делает Kube Proxy?</summary><br><b>
  Kube Proxy — это сетевой прокси, который работает на каждом узле кластера и реализует часть концепции Service в Kubernetes
</b></details>

<details>
<summary>Для чего и как используются "Resources Quotas"?</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое ConfigMap</summary><br><b>

Отделение конфигурации от Pod.
Подходит для случаев, когда в какой-то момент может понадобиться изменить конфигурацию, но не хочется перезапускать приложение или пересобирать образ: создаётся ConfigMap и подключается к Pod, но находится вне Pod.

В целом он хорош для:
* Совместного использования одной конфигурации разными Pod
* Хранения конфигурации вне Pod
</b></details>

<details>
<summary>Как использовать ConfigMap?</summary><br><b>

1. Создать его (из пары ключ-значение, файла или env-файла)
2. Подключить его. Смонтировать ConfigMap как том
</b></details>

<details>
<summary>Правда или ложь? Конфиденциальные данные, например учётные данные, следует хранить в ConfigMap</summary><br><b>

Ложь. Использовать secret.
</b></details>

<details>
<summary>Объясните, что такое "Horizontal Pod Autoscaler"</summary><br><b>

В Kubernetes HorizontalPodAutoscaler автоматически обновляет ресурс рабочей нагрузки (workload), чтобы автоматически масштабировать её в соответствии со спросом.
</b></details>

<details>
<summary>При удалении Pod удаляется ли он мгновенно? (через мгновение после выполнения команды)</summary><br><b>
</b></details>

<details>
<summary>Что значит быть cloud-native?</summary><br><b>
  Термин cloud native относится к концепции создания и запуска приложений так, чтобы использовать преимущества распределённых вычислений, которые предлагает облачная модель предоставления услуг.
</b></details>

<details>
<summary>Объясните подход к инфраструктуре «питомцы и скот» (pet and cattle) применительно к Kubernetes</summary><br><b>
</b></details>

<details>
<summary>Опишите, как запустить в K8s контейнеризованное веб-приложение, которое должно быть доступно по публичному URL.</summary><br><b>
</b></details>

<details>
<summary>Как искать неполадки в кластере, если некоторые приложения перестали быть доступны?</summary><br><b>
</b></details>

<details>
<summary>Опишите, какие CustomResourceDefinitions существуют в мире Kubernetes? Для чего их можно использовать?</summary><br><b>
</b></details>

<details>
<summary> Как работает планирование (scheduling) в Kubernetes?</summary><br><b>

Компонент control plane kube-scheduler задаёт следующие вопросы:
1. Что планировать? Он пытается понять спецификации из определения Pod
2. На какой узел планировать? Он пытается определить лучший узел со свободными ресурсами, чтобы запустить Pod
3. Привязывает Pod к выбранному узлу

Подробнее [здесь](https://www.youtube.com/watch?v=rDCWxkvPlAw)
</b></details>

<details>
<summary> Как используются метки и селекторы?</summary><br><b>
</b></details>

<details>
<summary>Какие существуют классы QoS?</summary><br><b>

* Guaranteed
* Burstable
* BestEffort
</b></details>

<details>
<summary>Объясните, что такое метки (Labels). Что это и зачем их использовать?</summary><br><b>
  
Метки Kubernetes — это пары ключ-значение, которые связывают идентифицирующие метаданные с объектами Kubernetes.
</b></details>

<details>
<summary>Объясните, что такое селекторы (Selectors)</summary><br><b>
</b></details>

<details>
<summary>Что такое Kubeconfig?</summary><br><b>
</b></details>

### Gatekeeper

<details>
<summary>Что такое Gatekeeper?</summary><br><b>

[Документация Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs): «Gatekeeper — это валидирующий (мутирующий — TBA) webhook, который применяет политики на основе CRD, исполняемые Open Policy Agent»
</b></details>

<details>
<summary>Объясните, как работает Gatekeeper</summary><br><b>

При каждом запросе к кластеру Kubernetes Gatekeeper отправляет политики и ресурсы в OPA (Open Policy Agent), чтобы проверить, нарушает ли запрос какую-либо политику. Если нарушает, Gatekeeper возвращает сообщение об ошибке политики. Если не нарушает ни одной политики, запрос попадёт в кластер.
</b></details>

### Тестирование политик

<details>
<summary>Что такое Conftest?</summary><br><b>

Conftest позволяет писать тесты для структурированных файлов. Его можно рассматривать как библиотеку тестов для ресурсов Kubernetes.<br>
В основном он используется в тестовых окружениях, таких как CI-пайплайны или локальные хуки.
</b></details>

<details>
<summary>Что такое Datree? Чем он отличается от Conftest?</summary><br><b>

Как и Conftest, он используется для тестирования и применения политик. Разница в том, что он поставляется со встроенными политиками.
</b></details>

### Helm

<details>
<summary>Что такое Helm?</summary><br><b>

Менеджер пакетов для Kubernetes. По сути, это возможность упаковывать YAML-файлы, распространять их среди других пользователей и применять в кластере (кластерах).

Как концепция это довольно распространено и встречается во многих платформах и сервисах. Например, менеджеры пакетов в операционных системах. В Fedora/RHEL это dnf. В Ubuntu — apt. Если Linux не используется, то стоит задать другой вопрос — почему? Но это уже другая тема :)
</b></details>

<details>
<summary>Зачем нужен Helm? В каких случаях его использовать?</summary><br><b>

Иногда для развёртывания определённого приложения в кластере нужно создать несколько YAML-файлов/компонентов, например Secret, Service, ConfigMap и т.д. Это может быть утомительно. Поэтому имеет смысл упростить процесс, введя нечто, что позволит делиться этим набором YAML каждый раз, когда нужно добавить приложение в кластер. Это нечто называется Helm.

Распространённый сценарий — несколько кластеров Kubernetes (prod, dev, staging). Вместо того чтобы применять разные YAML в каждом кластере по отдельности, логичнее создать один Chart и установить его в каждый кластер.

Другой сценарий — нужно поделиться созданным с сообществом, чтобы люди и компании могли легко развернуть приложение в своём кластере.
</b></details>

<details>
<summary>Объясните, что такое "Helm Charts"</summary><br><b>

Helm Charts — это набор YAML-файлов. Набор, который можно брать из репозиториев или создать свой и опубликовать его в репозиториях.
</b></details>

<details>
<summary>Говорят, что Helm — это ещё и шаблонизатор (Templating Engine). Что это значит?</summary><br><b>

Это полезно в сценариях, когда есть несколько похожих приложений, то есть различия в их конфигурационных файлах незначительны и большинство значений одинаковы. С помощью Helm можно определить общий шаблон для всех них, а значения, которые не фиксированы и меняются, сделать заполнителями (placeholders). Это называется файлом шаблона, и выглядит он примерно так

```
apiVersion: v1
kind: Pod
metadata:
  name: {[ .Values.name ]}
spec:
  containers:
  - name: {{ .Values.container.name }}
  image: {{ .Values.container.image }}
  port: {{ .Values.container.port }}
```

Сами значения будут в отдельном файле:

```
name: some-app
container:
  name: some-app-container
  image: some-app-image
  port: 1991
```
</b></details>

<details>
<summary>В каких случаях используют файл шаблона Helm?</summary><br><b>

* Развёртывание одного и того же приложения в нескольких разных окружениях
* CI/CD
</b></details>

<details>
<summary>Объясните структуру каталогов Helm Chart</summary><br><b>

someChart/     -> имя chart
  Chart.yaml   -> метаинформация о chart
  values.yaml  -> значения для файлов шаблонов
  charts/      -> зависимости chart
  templates/   -> файлы шаблонов :)
</b></details>

<details>
<summary>Как Helm поддерживает управление релизами?</summary><br><b>

Helm позволяет обновлять, удалять и откатываться к предыдущим версиям chart. В версии 2 Helm это делалось с помощью так называемого "Tiller". В версии 3 он был удалён из соображений безопасности.
</b></details>

#### Команды

<details>
<summary>Как искать chart?</summary><br><b>

`helm search hub [some_keyword]`
</b></details>

<details>
<summary>Можно ли переопределить значения из файла values.yaml при установке chart?</summary><br><b>
Да. Можно передать другой файл значений:
`helm install --values=override-values.yaml [CHART_NAME]`

Или прямо в командной строке: `helm install --set some_key=some_value`
</b></details>

<details>
<summary>Как вывести список развёрнутых релизов?</summary><br><b>

`helm ls` или `helm list`
</b></details>

<details>
<summary>Как выполнить откат?</summary><br><b>

`helm rollback RELEASE_NAME REVISION_ID`
</b></details>

<details>
<summary>Как посмотреть историю ревизий определённого релиза?</summary><br><b>

`helm history RELEASE_NAME`
</b></details>

<details>
<summary>Как обновить релиз?</summary><br><b>

`helm upgrade RELEASE_NAME CHART_NAME`
</b></details>

### Безопасность

<details>
<summary>Каким лучшим практикам безопасности стоит следовать применительно к кластеру Kubernetes?</summary><br><b>

  * Защищать взаимодействие между сервисами (один из способов — использовать Istio для взаимного TLS (mutual TLS))
  * Изолировать разные ресурсы в отдельные пространства имён на основе логических групп
  * Использовать поддерживаемый container runtime (если используется Docker, отказаться от него, потому что он устарел (deprecated). Можно использовать CRI-O в качестве движка и podman для CLI)
  * Как следует тестировать изменения в кластере (например, рассмотреть использование Datree для предотвращения ошибок конфигурации Kubernetes)
  * Ограничивать, кто и что может делать в кластере (например, с помощью OPA gatekeeper)
  * Использовать NetworkPolicy для обеспечения сетевой безопасности
  * Рассмотреть использование инструментов (например, Falco) для мониторинга угроз
</b></details>

### Сценарии устранения неполадок

<details>
<summary>При выполнении <code>kubectl get pods</code> видны Pod в статусе "Pending". Что делать?</summary><br><b>

Один из возможных путей — выполнить `kubectl describe pod <pod name>`, чтобы получить больше подробностей.<br>
Можно увидеть одно из следующего:
  * Кластер заполнен. В этом случае расширить кластер.
  * Достигнуты лимиты ResourcesQuota. В этом случае, возможно, стоит их изменить
  * Проверить, не ожидает ли монтирование PersistentVolumeClaim

Если ничего из перечисленного не помогло, выполнить команду (`get pods`) с `-o wide`, чтобы проверить, назначен ли Pod на узел. Если нет, возможно, проблема в планировщике.
</b></details>

<details>
<summary>Пользователи не могут получить доступ к приложению, работающему в Pod в Kubernetes. В чём может быть проблема и как это проверить?</summary><br><b>

Один из возможных путей — начать с проверки статуса Pod.
1. Pod в состоянии pending? Если да, выяснить причину с помощью `kubectl describe pod <pod name>`
TODO: дописать...
</b></details>

### Istio

<details>
<summary>Что такое Istio? Для чего он используется?</summary><br><b>
  
Istio — это service mesh с открытым исходным кодом, которая помогает организациям запускать распределённые приложения на основе микросервисов где угодно. Istio позволяет организациям защищать, связывать и отслеживать микросервисы, чтобы быстрее и безопаснее модернизировать свои корпоративные приложения.
</b></details>

### Контроллеры (Controllers)

<details>
<summary>Что такое контроллеры?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/architecture/controller): «В Kubernetes контроллеры — это циклы управления (control loops), которые отслеживают состояние кластера, а затем вносят или запрашивают изменения там, где это необходимо. Каждый контроллер пытается приблизить текущее состояние кластера к желаемому.»
</b></details>

<details>
<summary>Назовите два известных контроллера</summary><br><b>

1. Node Controller: управляет узлами кластера. Помимо прочего, контроллер отвечает за мониторинг состояния узлов: если узел внезапно становится недоступен, он эвакуирует все работающие на нём Pod и соответствующим образом пометит статус узла.
2. Replication Controller — отслеживает состояние реплик Pod на основе того, что должно работать. Он следит за тем, чтобы количество Pod, которые должны работать, действительно работало
</b></details>

<details>
<summary>Какой процесс отвечает за запуск и установку различных контроллеров?</summary><br><b>

Kube-Controller-Manager
</b></details>

<details>
<summary>Что такое цикл управления (control loop)? Как он работает?</summary><br><b>

Объяснение [здесь](https://www.youtube.com/watch?v=i9V4oCa5f9I)
</b></details>

<details>
<summary>Из каких фаз/шагов состоит цикл управления?</summary><br><b>

- Observe — определить текущее состояние кластера
- Diff — определить, есть ли разница между текущим и желаемым состоянием
- Act — привести текущее состояние кластера к желаемому (то есть, по сути, достичь состояния, в котором разницы нет)
</b></details>

### Планировщик (Scheduler)

<details>
<summary>Правда или ложь? Планировщик отвечает и за решение, где будет работать Pod, и за его фактический запуск</summary><br><b>

Ложь. Планировщик отвечает за выбор узла, на котором будет работать Pod, а фактически запускает Pod Kubelet.
</b></details>

<details>
<summary>Как запланировать Pod на узел с именем "node1"?</summary><br><b>

`k run some-pod --image=redix -o yaml --dry-run=client > pod.yaml`

`vi pod.yaml` и добавить:

```
spec:
  nodeName: node1
```

`k apply -f pod.yaml`

Примечание: если в кластере нет узла node1, Pod застрянет в состоянии "Pending".
</b></details>

#### Node Affinity

<details>
<summary>С помощью node affinity настройте Pod так, чтобы он планировался на узел, где ключ "region" имеет значение "asia" или "emea"</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedlingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: In
          values:
          - asia
          - emea
```
</b></details>

<details>
<summary>С помощью node affinity настройте Pod так, чтобы он никогда не планировался на узел, где ключ "region" имеет значение "neverland"</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedlingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: NotIn
          values:
          - neverland
```
</b></details>

<details>
<summary>Правда или ложь? Использование типа node affinity "requiredDuringSchedlingIgnoredDuringExecution" означает, что планировщик не может запланировать Pod, если правило не выполнено</summary><br><b>

Правда
</b></details>

<details>
<summary>Правда или ложь? Использование типа node affinity "preferredDuringSchedlingIgnoredDuringExecution" означает, что планировщик не может запланировать Pod, если правило не выполнено</summary><br><b>

Ложь. Планировщик пытается найти узел, удовлетворяющий требованиям/правилам, а если не находит, всё равно запланирует Pod.
</b></details>

<details>
<summary>Можно ли развернуть несколько планировщиков?</summary><br><b>

Да, это возможно. Можно запустить ещё один Pod с командой, похожей на следующую:

```
spec:
  containers:
  - command:
    - kube-scheduler
    - --address=127.0.0.1
    - --leader-elect=true
    - --scheduler-name=some-custom-scheduler
...
```
</b></details>

<details>
<summary>Есть несколько планировщиков. Как узнать, какой планировщик использовался для конкретного Pod?</summary><br><b>

Выполнив `kubectl get events`, можно увидеть, какой планировщик использовался.
</b></details>

<details>
<summary>Нужно запустить новый Pod так, чтобы его запланировал пользовательский планировщик. Как это сделать?</summary><br><b>

Добавить в spec Pod следующее:

```
spec:
  schedulerName: some-custom-scheduler
```
</b></details>

### Taints

<details>
<summary>Проверьте, есть ли ограничения (taints) на узле "master"</summary><br><b>

`k describe no master | grep -i taints`
</b></details>

<details>
<summary>Создайте taint на одном из узлов кластера с ключом "app", значением "web" и эффектом "NoSchedule". Убедитесь, что он применён</summary><br><b>

`k taint node minikube app=web:NoSchedule`

`k describe no minikube | grep -i taints`
</b></details>

<details>
<summary>На единственный узел кластера применили taint командой <code>k taint node minikube app=web:NoSchedule</code>, а затем выполнили <code>kubectl run some-pod --image=redis</code>. Что произойдёт?</summary><br><b>

Pod останется в статусе "Pending", потому что на единственном узле кластера есть taint "app=web".
</b></details>

<details>
<summary>На единственный узел кластера применили taint командой <code>k taint node minikube app=web:NoSchedule</code>, а затем выполнили <code>kubectl run some-pod --image=redis</code>, но Pod находится в состоянии pending. Как это исправить?</summary><br><b>

`kubectl edit po some-pod` и добавить следующее

```
  - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Выйти и сохранить. Теперь Pod должен быть в состоянии Running.
</b></details>

<details>
<summary>Удалите существующий taint с одного из узлов кластера</summary><br><b>

`k taint node minikube app=web:NoSchedule-`
</b></details>

<details>
<summary>Какие бывают эффекты taint? Объясните каждый из них</summary><br><b>

`NoSchedule`: не позволяет планировать ресурсы на определённый узел
`PreferNoSchedule`: планировщик предпочтёт размещать ресурсы на других узлах, прежде чем прибегнуть к размещению ресурса на выбранном узле (к которому применён taint)
`NoExecute`: применение "NoSchedule" не вытесняет (evict) с узла уже работающие Pod (или другие ресурсы), в отличие от "NoExecute", который вытесняет с узла любой уже работающий ресурс
</b></details>

### Ограничения ресурсов (Resource Limits)

<details>
<summary>Объясните, зачем задавать ограничения ресурсов (resource limits) для Pod</summary><br><b>

* Известно, сколько RAM и/или CPU должно потреблять приложение, и всё, что выше, недопустимо
* Нужно гарантировать, что каждый сможет запускать свои приложения в кластере и ресурсы не будут использоваться только одним типом приложений
</b></details>

<details>
<summary>Правда или ложь? Ограничения ресурсов применяются на уровне Pod, то есть если лимит — 2gb RAM и в Pod два контейнера, то у каждого по 1gb RAM</summary><br><b>

Ложь. Они задаются для каждого контейнера, а не для Pod.
</b></details>

#### Ограничения ресурсов - команды

<details>
<summary>Проверьте, заданы ли какие-либо ограничения (limits) у одного из Pod в кластере</summary><br><b>

`kubectl describe po <POD_NAME> | grep -i limits`
</b></details>

<details>
<summary>Запустите Pod с именем "yay" из образа "python" с запросом ресурсов (resources request) 64Mi памяти и 250m CPU</summary><br><b>

`kubectl run yay --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay
    resources:
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`
</b></details>

<details>
<summary>Запустите Pod с именем "yay2" из образа "python". Убедитесь, что запрос ресурсов составляет 64Mi памяти и 250m CPU, а ограничения — 128Mi памяти и 500m CPU</summary><br><b>

`kubectl run yay2 --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay2
    resources:
      limits:
        cpu: 500m
        memory: 128Mi
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`
</b></details>

### Мониторинг

<details>
<summary>Какие решения для мониторинга Kubernetes известны?</summary><br><b>

Существует много типов решений для мониторинга Kubernetes. Одни с открытым исходным кодом, другие хранят данные в памяти (in-memory), третьи платные, ... вот краткий список:

* metrics-server: мониторинг с открытым исходным кодом, хранящий данные в памяти
* datadog: $$$
* promethues: решение для мониторинга с открытым исходным кодом

</b></details>

<details>
<summary>Опишите, как используемое решение для мониторинга отслеживает Kubernetes и </summary><br><b>

Это сильно зависит от того, что выбрано. Рассмотрим некоторые решения:

* metrics-server: бесплатное решение для мониторинга с открытым исходным кодом, которое использует компонент kubelet cAdvisor для получения информации о кластере и его ресурсах и хранит её в памяти.
После установки через некоторое время можно выполнять команды вроде `kubectl top node` и `kubectl top pod`, чтобы смотреть метрики производительности узлов, Pod и других ресурсов.

TODO: добавить другие решения для мониторинга

</b></details>

### Kustomize

<details>
<summary>Что такое Kustomize?</summary><br><b>
</b></details>

<details>
<summary>Объясните, зачем нужен Kustomize, описав реальные сценарии использования</summary><br><b>

* Есть helm chart приложения, которое используют несколько команд в организации, и есть требование добавить к приложению аннотацию с именем команды, владеющей приложением
  * Без Kustomize пришлось бы скопировать файлы (в данном случае шаблон chart) и изменить их, добавив нужные аннотации
  * С Kustomize не нужно копировать весь репозиторий или файлы
* Нужно применить изменение/патч к какому-то приложению, не изменяя исходные файлы приложения
  * С Kustomize можно определить файл kustomization.yml, описывающий эти изменения, так что исходные файлы приложения трогать не нужно
</b></details>

<details>
<summary>На высоком уровне опишите, как работает Kustomize</summary><br><b>

1. Добавить файл kustomization.yml в каталог приложения, которое нужно изменить.
   1. Определить изменения, которые нужно выполнить
2. Выполнить `kustomize build APP_PATH` там же, где находится kustomization.yml
</b></details>

### Стратегии развёртывания

<details>
<summary>Какие стратегии выкатки/развёртывания известны?</summary><br><b>

* Blue/Green Deployments: новая версия приложения развёртывается, пока старая продолжает работать, и затем трафик начинают перенаправлять на новую версию приложения
* Canary Deployments: новая версия приложения развёртывается, и на неё начинают перенаправлять **часть** пользователей/трафика. Таким образом, переход на новую версию гораздо более постепенный
</b></details>

<details>
<summary>Подробно объясните развёртывание/выкатку Blue/Green</summary><br><b>

Шаги развёртывания Blue/Green:

1. Трафик от пользователей идёт через балансировщик нагрузки к приложению, текущая версия которого — 1

Users -> Load Balancer -> App Version 1

2. Развёртывается новая версия приложения 2 (пока версия 1 продолжает работать)

Users -> Load Balancer -> App Version 1
                          App Version 2

3. Если версия 2 работает правильно, трафик переключается на неё вместо версии 1

User -> Load Balancer     App version 1
                       -> App Version 2

4. Удалить ли старую версию или оставить её работать, но без перенаправления на неё пользователей, — решает команда или компания

Плюсы:
  * Можно в любой момент быстро откатиться/переключиться на предыдущую версию
Минусы:
  * В случае проблемы с новой версией затронуты ВСЕ пользователи (а не небольшая их часть/процент)

</b></details>

<details>
<summary>Подробно объясните развёртывание/выкатку Canary</summary><br><b>

Шаги развёртывания Canary:

1. Трафик от пользователей идёт через балансировщик нагрузки к приложению, текущая версия которого — 1

Users -> Load Balancer -> App Version 1

2. Развёртывается новая версия приложения 2 (пока версия 1 продолжает работать), и часть трафика перенаправляется на новую версию

Users -> Load Balancer ->(95% трафика) App Version 1
                       ->(5% трафика) App Version 2

3. Если новая версия (2) работает хорошо, на неё перенаправляется больше трафика

Users -> Load Balancer ->(70% трафика) App Version 1
                       ->(30% трафика) App Version 2

3. Если всё работает хорошо, в какой-то момент весь трафик перенаправляется на новую версию

Users -> Load Balancer -> App Version 2


Плюсы:
  * Если с новой развёрнутой версией приложения есть проблема, затронута только часть пользователей, а не все
Минусы:
  * Тестирование новой версии неизбежно происходит в production-окружении (поскольку пользовательский трафик есть только там)

</b></details>

<details>
<summary>Какие способы реализации стратегий развёртывания (например, canary, blue/green) в Kubernetes известны?</summary><br><b>

Способов несколько. Один из них — Argo Rollouts.
</b></details>

### Сценарии

<details>
<summary>Инженер из организации говорит, что хочет видеть в Kubernetes только ресурсы своей команды. Однако на деле он видит ресурсы всей организации, многих разных команд. Какое понятие Kubernetes можно использовать, чтобы решить эту проблему?</summary><br><b>

Пространства имён (Namespaces). Подробнее см. следующий [вопрос и ответ о пространствах имён](#namespaces-use-cases).
</b></details>

<details>
<summary>Инженер из команды запускает Pod, но видит статус "CrashLoopBackOff". Что это значит? Как найти проблему?</summary><br><b>

Контейнер не смог запуститься (по разным причинам), и Kubernetes пытается снова запустить Pod после некоторой задержки (= время BackOff).

Некоторые причины сбоя:
  - Ошибка конфигурации — опечатка, неподдерживаемое значение и т.д.
  - Ресурс недоступен — узлы не работают, PV не смонтирован и т.д.

Некоторые способы отладки:

1. `kubectl describe pod POD_NAME`
   1. Обратить внимание на `State` (должно быть Waiting, CrashLoopBackOff) и `Last State`, где должно быть указано, что произошло перед этим (то есть почему случился сбой)
2. Выполнить `kubectl logs mypod`
   1. Это должно дать точный вывод
   2. Для конкретного контейнера можно добавить `-c CONTAINER_NAME`
</b></details>

<details>
<summary>Инженер из организации спрашивает, можно ли запретить планирование Pod (с определённой меткой) на один из узлов кластера. Ответ:</summary><br><b>

Да, с помощью taints: можно выполнить следующую команду, и она запретит планирование всех ресурсов с меткой "app=web" на node1: `kubectl taint node node1 app=web:NoSchedule`
</b></details>

<details>
<summary>Нужно ограничить количество ресурсов, используемых в кластере. Например, не более 4 ReplicaSet, 2 сервисов и т.д. Как этого добиться?</summary><br><b>

С помощью ResourceQuats
</b></details>

<!-- {% endraw %} -->

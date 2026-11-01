# CKA (Certified Kubernetes Administrator)

- [CKA (Certified Kubernetes Administrator)](#cka-certified-kubernetes-administrator)
  - [Подготовка](#подготовка)
  - [Pods](#pods)
    - [Устранение неполадок с Pod](#устранение-неполадок-с-pod)
  - [Пространства имён (Namespaces)](#пространства-имён-namespaces)
  - [Узлы (Nodes)](#узлы-nodes)
  - [Services](#services)
  - [ReplicaSets](#replicasets)
    - [Устранение неполадок с ReplicaSet](#устранение-неполадок-с-replicaset)
  - [Deployments](#deployments)
    - [Устранение неполадок с Deployment](#устранение-неполадок-с-deployment)
  - [Планировщик (Scheduler)](#планировщик-scheduler)
    - [Node Affinity](#node-affinity)
  - [Метки и селекторы](#метки-и-селекторы)
    - [Node Selector](#node-selector)
  - [Taints](#taints)
  - [Ограничения ресурсов](#ограничения-ресурсов)
  - [Мониторинг](#мониторинг)
  - [Планировщик (Scheduler)](#планировщик-scheduler-1)

## Подготовка

* Развернуть кластер Kubernetes. Можно использовать один из вариантов:
   1. Minikube — бесплатный и простой локальный кластер
   2. Управляемый кластер (EKS, GKE, AKS)

* Задать псевдонимы (aliases)

```
alias k=kubectl
alias kd=kubectl delete
alias kds=kubectl describe
alias ke=kubectl edit
alias kr=kubectl run
alias kg=kubectl get
```

## Pods

<details>
<summary>Выполните команду, которая покажет все Pod в текущем пространстве имён</summary><br><b>

`kubectl get pods`

Примечание: стоит создать псевдоним (`alias k=kubectl`) и привыкнуть к `k get po`
</b></details>

<details>
<summary>Запустите Pod с именем "nginx-test" из образа "nginx"</summary><br><b>

`k run nginx-test --image=nginx`
</b></details>

<details>
<summary>Есть Pod с именем "nginx-test". Как его удалить?</summary><br><b>

`k delete po nginx-test`
</b></details>

<details>
<summary>В каком пространстве имён работает Pod <code>etcd</code>? Выведите список Pod в этом пространстве имён</summary><br><b>

`k get po -n kube-system`

Допустим, неизвестно, в каком пространстве имён он находится. Тогда можно выполнить `k get po -A | grep etc`, чтобы найти Pod и посмотреть, в каком пространстве имён он расположен.
</b></details>

<details>
<summary>Выведите список Pod из всех пространств имён</summary><br><b>

`k get po -A`

Полная версия команды: `kubectl get pods --all-namespaces`.
</b></details>

<details>
<summary>Напишите YAML для Pod с двумя контейнерами и создайте Pod с помощью этого YAML-файла (образы — любые)</summary><br><b>

```
cat > pod.yaml <<EOL
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  containers:
  - image: alpine
    name: alpine
  - image: nginx-unprivileged
    name: nginx-unprivileged
EOL

k create -f pod.yaml
```

Если возникает вопрос, как запомнить всё это, — не беда, можно просто выполнить `kubectl run some_pod --image=redis -o yaml --dry-run=client > pod.yaml`. А если возникает вопрос «как запомнить такую длинную команду», пора менять подход ;)
</b></details>

<details>
<summary>Создайте YAML для Pod с помощью команды kubectl, не запуская сам Pod (образ — любой)</summary><br><b>

`k run some-pod -o yaml --image nginx-unprivileged --dry-run=client > pod.yaml`
</b></details>

<details>
<summary>Как проверить, что манифест корректен?</summary><br><b>

С помощью флага `--dry-run`: объект не будет создан на самом деле, но манифест будет проверен, и так можно найти любые синтаксические ошибки.

`k create -f YAML_FILE --dry-run`
</b></details>

<details>
<summary>Как проверить, какой образ использует определённый Pod?</summary><br><b>

`k describe po <POD_NAME> | grep -i image`
</b></details>

<details>
<summary>Как проверить, сколько контейнеров работает в одном Pod?</summary><br><b>

`k get po POD_NAME` и посмотреть число в столбце "READY".

Также можно выполнить `k describe po POD_NAME`
</b></details>

<details>
<summary>Запустите Pod с именем "remo" из последнего образа redis с меткой 'year=2017'</summary><br><b>

`k run remo --image=redis:latest -l year=2017`
</b></details>

<details>
<summary>Выведите список Pod и их меток</summary><br><b>

`k get po --show-labels`
</b></details>

<details>
<summary>Удалите Pod с именем "nm"</summary><br><b>

`k delete po nm`
</b></details>

<details>
<summary>Выведите список всех Pod с меткой "env=prod"</summary><br><b>

`k get po -l env=prod`

Чтобы посчитать их: `k get po -l env=prod --no-headers | wc -l`
</b></details>

<details>
<summary>Создайте статический Pod из образа <code>python</code>, который выполняет команду <code>sleep 2017</code></summary><br><b>

Сначала перейти в каталог, который kubelet отслеживает для создания статических Pod: `cd /etc/kubernetes/manifests` (путь можно проверить в конфигурационном файле kubelet)

Затем создать в этом каталоге определение/манифест

`k run some-pod --image=python --command sleep 2017 --restart=Never --dry-run=client -o yaml > static-pod.yaml`

</b></details>

<details>
<summary>Опишите, как удалить статический Pod
</summary><br><b>

Найти каталог статических Pod (см. `staticPodPath` в конфигурационном файле kubelet).

Перейти в этот каталог и удалить манифест/определение статического Pod (`rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`)
</b></details>

### Устранение неполадок с Pod

<details>
<summary>При запуске Pod виден статус "CrashLoopBackOff". Что это значит? Как найти проблему?</summary><br><b>

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
3. Если по-прежнему непонятно, почему произошёл сбой, попробовать `kubectl get events`
4. 
</b></details>

<details>
<summary>Что означает ошибка <code>ImagePullBackOff</code>?</summary><br><b>

Скорее всего, неправильно указано имя образа, который нужно скачать и запустить. Или, возможно, такого образа нет в реестре.

Проверить это можно с помощью `kubectl describe po POD_NAME`
</b></details>

<details>
<summary>Как проверить, на каком узле работает определённый Pod?</summary><br><b>

`k get po POD_NAME -o wide`
</b></details>

<details>
<summary>Выполните следующую команду: <code>kubectl run ohno --image=sheris</code>. Сработало? Почему нет? Исправьте это, не удаляя Pod, используя любой образ</summary><br><b>

Потому что образа `sheris` не существует. По крайней мере пока :)

Чтобы исправить, выполнить `kubectl edit ohno` и заменить строку `- image: sheris` на `- image: redis` или любой другой образ.
</b></details>

<details>
<summary>Pod при запуске находится в состоянии "Pending". В чём может быть причина?</summary><br><b>

Одна из возможных причин — не работает планировщик (scheduler), который должен распределять Pod по узлам. Чтобы проверить это, можно выполнить `kubectl get po -A | grep scheduler` или посмотреть непосредственно в пространстве имён `kube-system`.
</b></details>

<details>
<summary>Как посмотреть логи контейнера, работающего в Pod?</summary><br><b>

`k logs POD_NAME`
</b></details>

<details>
<summary>В Pod с именем "some-pod" два контейнера. Что произойдёт при выполнении <code>kubectl logs some-pod</code></summary><br><b>

Команда не сработает, потому что в Pod два контейнера и нужно указать один из них: `kubectl logs POD_NAME -c CONTAINER_NAME`
</b></details>

## Пространства имён (Namespaces)

<details>
<summary>Выведите список всех пространств имён</summary><br><b>

`k get ns`
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

## Узлы (Nodes)

<details>
<summary>Выполните команду, которая покажет все узлы кластера</summary><br><b>

`kubectl get nodes`

Примечание: стоит создать псевдоним (`alias k=kubectl`) и привыкнуть к `k get no`
</b></details>

<details>
<summary>Создайте список всех узлов в формате JSON и сохраните его в файл "some_nodes.json"</summary><br><b>

`k get nodes -o json > some_nodes.json`
</b></details>

<details>
<summary>Проверьте, какие метки есть у одного из узлов кластера</summary><br><b>

`k get no minikube --show-labels`
</b></details>

## Services

<details>
<summary>Проверьте, сколько сервисов работает в текущем пространстве имён</summary><br><b>

`k get svc`
</b></details>

<details>
<summary>Создайте внутренний сервис с именем "sevi", чтобы открыть доступ к приложению 'web' на порту 1991</summary><br><b>
 
`kubectl expose pod web --port=1991 --name=sevi`
</b></details>

<details>
<summary>Как обратиться по имени к сервису "app-service" в том же пространстве имён?</summary><br><b>

app-service
</b></details>

<details>
<summary>Как проверить TargetPort сервиса?</summary><br><b>

`k describe svc <SERVICE_NAME>`
</b></details>

<details>
<summary>Как проверить, какие конечные точки (endpoints) есть у svc?</summary><br><b>

`k describe svc <SERVICE_NAME>`
</b></details>

<details>
<summary>Как обратиться по имени к сервису "app-service" из другого пространства имён с именем "dev"?</summary><br><b>

app-service.dev.svc.cluster.local
</b></details>

<details>
<summary>Есть работающее развёртывание (Deployment), и нужно создать Service, чтобы открыть доступ к его Pod. Требования/известные данные:

* Имя Deployment: jabulik
* Целевой порт: 8080
* Тип сервиса: NodePort
* Селектор: jabulik-app
* Порт: 8080
</summary><br><b>

`kubectl expose deployment jabulik --name=jabulik-service --target-port=8080 --type=NodePort --port=8080 --dry-run=client -o yaml -> svc.yaml`

`vi svc.yaml` (убедиться, что селектор задан как `jabulik-app`)

`k apply -f svc.yaml`
</b></details>

## ReplicaSets

<details>
<summary>Как проверить, сколько ReplicaSet определено в текущем пространстве имён?</summary><br><b>

`k get rs`
</b></details>

<details>
<summary>ReplicaSet настроен на запуск 3 Pod. Один из этих 3 Pod удалили. Что произойдёт дальше? Сколько будет Pod?</summary><br><b>

Теоретически по-прежнему будут работать 3 Pod, потому что задача ReplicaSet — обеспечивать именно это. Поэтому при удалении одного или нескольких Pod он запустит дополнительные, чтобы всегда было 3 Pod.
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

### Устранение неполадок с ReplicaSet

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

## Deployments

<details>
<summary>Как вывести список всех развёртываний (Deployment) в текущем пространстве имён?</summary><br><b>

`k get deploy`

</b></details>

<details>
<summary>Как проверить, какой образ использует определённый Deployment?</summary><br><b>

`k describe deploy <DEPLOYMENT_NAME> | grep image`

</b></details>

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

`kubectl create deployment pluck --image=redis --replicas=5`

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

### Устранение неполадок с Deployment

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

## Планировщик (Scheduler)

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

### Node Affinity

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

## Метки и селекторы

<details>
<summary>Как вывести список всех Pod с меткой "app=web"?</summary><br><b>

`k get po -l app=web`
</b></details>

<details>
<summary>Как вывести список всех объектов с меткой "env=staging"?</summary><br><b>

`k get all -l env=staging`
</b></details>

<details>
<summary>Как вывести список всех Deployment с метками "env=prod" и "type=web"?</summary><br><b>

`k get deploy -l env=prod,type=web`
</b></details>

### Node Selector

<details>
<summary>Повесьте метку "hw=max" на один из узлов кластера</summary><br><b>

`kubectl label nodes some-node hw=max`

</b></details>

<details>
<summary>Создайте и запустите Pod с именем `some-pod` из образа `redis` и настройте его на использование селектора `hw=max`</summary><br><b>

```
kubectl run some-pod --image=redis --dry-run=client -o yaml > pod.yaml

vi pod.yaml

spec:
  nodeSelector:
    hw: max

kubectl apply -f pod.yaml
```

</b></details>

<details>
<summary>Объясните, почему возможности селекторов узлов могут быть ограничены</summary><br><b>

Предположим, нужно запускать Pod на всех узлах, у которых `hw` равно max или min, а не только max. С nodeSelectors это невозможно — они довольно упрощённые, и здесь стоит рассмотреть `node affinity`.
</b></details>

## Taints

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

## Ограничения ресурсов

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

## Мониторинг

<details>
<summary>Разверните metrics-server</summary><br><b>

`kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`
</b></details>

<details>
<summary>С помощью metrics-server посмотрите следующее:

* самые нагруженные узлы кластера
* самые нагруженные Pod
</summary><br><b>

* узлы: `kubectl top nodes`
* Pod: `kubectl top pods`

</b></details>

## Планировщик (Scheduler)

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

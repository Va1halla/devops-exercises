# Argo Rollouts - Canary

## Требования

1. Работающий кластер Kubernetes
2. Argo Rollouts CLI
3. Развёрнутое приложение определённой версии

## Задачи

1. Установите контроллер Argo Rollouts
2. Напишите манифест rollout, использующий стратегию canary, и примените его
   1. Задайте 6 реплик
   2. Отключите автоматическое продвижение (auto-promotion)
3. Проверьте список rollout
4. Выкатите новую версию приложения любым удобным способом
   1. Проверьте статус rollout

## Решение

Установка:

1. `kubectl create namespace argo-rollouts`
   1. `kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml`

2. Ресурс Rollout:

```
---
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: some-app
spec:
  replicas: 6
  strategy:
    canary:
      stableService: k8s-service-stable
      canaryService: k8s-service-canary
      trafficRouting:
        ambassador:
          mappings:
            - k8s-mapping
      steps:
      - setWeight: 30
      - pause: {}
      - setWeight: 60
      - pause: {}
      - setWeight: 100
      - pause: {}   
  selector:
    matchLabels:
      app: some-web-app
  template:
    metadata:
      labels:
        app: some-web-app
    spec:
      containers:
      - name: web-app
        image: some/registry/and/image:v1.0
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
```

3. `kubectl argo rollouts list rollouts`
4. `kubectl argo rollouts set image SOME-APP web-app=some/registry/and/image:v2.0`
   1. `kubectl argo rollouts get rollout some-app --watch`
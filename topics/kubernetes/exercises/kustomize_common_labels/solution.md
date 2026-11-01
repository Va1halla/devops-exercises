# Kustomize — общие метки (Common Labels)

## Требования

1. Работающий кластер Kubernetes
2. Kubctl версии 1.14 или выше

## Цели

В текущем каталоге находится приложение, состоящее из Deployment и Service.

1. Написать файл kustomization.yml, который добавит и в Service, и в Deployment метку "team-name: aces"
2. Выполнить команду kustomize, которая сгенерирует изменённые файлы k8s с добавленной меткой

## Решение

1. Добавить следующее в kustomization.yml в каталоге someApp:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

commonLabels:
  team-name: aces

resources:
  - service.yml
  - deployment.yml
```

2. Выполнить `kubectl apply -k someApp`

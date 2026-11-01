# Helm-приложение в ArgoCD

## Требования

1. Работающий кластер Kubernetes
2. ArgoCD, установленный в кластере k8s
3. Репозиторий с Helm-чартом

## Задачи

1. Создайте в ArgoCD новое приложение, указывающее на репозиторий вашего Helm-чарта

## Решение

```
argocd app create some-app \
--project default \
--repo https://repo-with-helm-chart
--path "./helm" \
--sync-policy auto \
--dest-namespace default \
--dest-server https://kubernetes.cluster
```
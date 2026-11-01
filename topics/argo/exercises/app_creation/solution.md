# Создание приложения

## Требования

1. Нужен репозиторий с какими-либо манифестами Kubernetes
2. Нужен работающий кластер Kubernetes с установленным ArgoCD

## Задачи

1. С помощью CLI или UI создайте новое приложение со следующими свойствами:
   1. имя приложения: app-demo
   2. проект: app-project
   3. URL репозитория: ваш репозиторий с манифестами k8s
   4. пространство имён (namespace): default
2. Убедитесь, что приложение создано
3. Синхронизируйте (sync) приложение
4. Убедитесь, что ресурсы Kubernetes созданы
5. Удалите приложение

## Решение

### UI

1. Нажмите "New App"
   1. Введите имя приложения: `app-demo`
   2. Введите проект: `app-project`
   3. В разделе source укажите URL вашего GitHub-репозитория с манифестами Kubernetes
      1. Задайте путь (path) к приложению
   4. В разделе destination укажите адрес кластера Kubernetes и задайте namespace `default`
   5. Нажмите "Create"
2. Нажмите кнопку "Sync" в форме "app-demo"
   1. Нажмите "Synchronize"
3. Убедитесь, что ресурсы Kubernetes созданы
   1. `kubectl get deployments`
4. Удалите приложение

### CLI

```
argocd app create app-demo \
--project app-project \
--repo https://fake.repo.address \
--path ./some_app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster

# Проверить состояние приложения
argocd app list
argocd app get app-demo

# Синхронизировать состояние приложения
argocd app sync app-demo
argocd app wait app-demo

# Убедиться, что ресурсы kubernetes созданы
kubectl get deployments

# Удалить приложение
argocd app delete app-demo
```
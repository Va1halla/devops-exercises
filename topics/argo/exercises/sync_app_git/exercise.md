# Синхронизация приложения — Git

## Требования

1. Нужен репозиторий с какими-либо манифестами Kubernetes
2. Нужен работающий кластер Kubernetes с установленным ArgoCD


## Задачи

1. Создайте новое приложение через UI или CLI
   1. Имя приложения: app-demo
   2. Проект: project-demo
   3. Пространство имён Kubernetes: default
2. Синхронизируйте приложение
3. Убедитесь, что приложение работает, выполнив `kubectl get deploy` в пространстве имён `default`
4. Теперь измените в репозитории один из манифестов Kubernetes (например, обновите тег в deployment)
5. Вернитесь в ArgoCD и проверьте состояние приложения
6. Синхронизируйте состояние приложения

## Решение

Нажмите [здесь](solution.md), чтобы посмотреть решение

### UI

1. Нажмите "New App"
   1. Введите имя приложения: `app-demo`
   2. Введите проект: `project-demo`
   3. В разделе source укажите URL вашего GitHub-репозитория с манифестами Kubernetes
      1. Задайте путь (path) к приложению
   4. В разделе destination укажите адрес кластера Kubernetes и задайте namespace `default`
   5. Нажмите "Create"
2. Нажмите на только что созданное приложение
   1. Нажмите кнопку "sync" и затем "Synchronize"
3. Внесите изменение в Git-репозиторий, где лежат манифесты Kubernetes
   1.  `git add .`
   2.  `git commit -a`
   3.  `git push origin <BRANCH_NAME>`
4.  Вернитесь в UI ArgoCD и проверьте статус приложения
    1.  Оно должно быть в состоянии "out-of-sync". Если это не так, попробуйте нажать "Refresh"
    2.  Также можно нажать "App diff", чтобы увидеть различия, которые привели к "out-of-sync"
5.  Нажмите "Sync" и "Synchronize", чтобы синхронизировать приложение

### CLI 

```
argocd app create app-demo \
--project project-demo \
--repo https://fake.repo.address \
--path ./some_app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster

# В Git-репозитории
cd <git repo>
vi <k8s manifest>
git add .
git commit -a
git push origin <BRANCH_NAME>

# Проверить состояние приложения
argocd app get app-demo

# Синхронизировать состояние приложения
argocd app sync app-demo
argocd app wait app-demo
```
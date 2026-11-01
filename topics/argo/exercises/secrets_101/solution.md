# Секреты в ArgoCD 101

## Требования

1. Работающий кластер Kubernetes
2. Манифесты k8s приложения, содержащие секреты (secrets)
3. Установленный бинарный файл Kubeseal

## Задачи

1. Установите контроллер bitnami sealed (sealed secrets controller) как приложение ArgoCD
2. Зашифруйте секреты и закоммитьте их в репозиторий с манифестами k8s
3. Создайте приложение, использующее зашифрованные секреты

## Решение

1. Нажмите "New App"
   1. имя приложения: controller
   2. проект: default
   3. политика синхронизации (sync policy): automatic
   4. URL репозитория: URL манифестов контроллера bitnami sealed
   5. пространство имён (namespace): kube-system

2. Для каждого секрета выполните: `kubeseal < some/secret.yml > sealed_secrets/some/encrypted_secret.yaml -o yaml`

3. Нажмите "New App"
   1. имя приложения: some-app
   2. проект: default
   3. политика синхронизации (sync policy): automatic
   4. URL репозитория: URL манифестов k8s (включая зашифрованные секреты)
   5. пространство имён (namespace): default

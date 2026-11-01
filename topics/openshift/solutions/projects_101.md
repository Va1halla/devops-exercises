## OpenShift — проекты 101

### Цели

В только что развёрнутом кластере (желательно) выполнить следующее:

1. Войти в кластер OpenShift
2. Вывести список всех проектов
3. Создать новый проект с именем 'neverland'
4. Проверить общий статус текущего проекта

### Решение

```
oc login -u YOUR_USER -p YOUR_PASSWORD_OR_TOKEN
oc get projects # Empty output in new cluster
oc new-project neverland
oc status
```

## ReplicaSet 02 — решение

1. Создать ReplicaSet с 2 репликами. Приложение может быть любым.

```
cat >> rs.yaml <<EOL
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web
  labels:
    app: somewebapp
    type: web
spec:
  replicas: 2
  selector:
    matchLabels:
      type: web
  template:
    metadata:
      labels:
        type: web
    spec:
      containers:
      - name: httpd
        image: registry.redhat.io/rhscl/httpd-24-rhel7
EOL

kubectl apply -f rs.yaml
```

2. Убедиться, что ReplicaSet создан и в нём 2 реплики

```
kubectl get rs
# ИЛИ более конкретный способ: kubectl get -f rs.yaml
```

3. Удалить ReplicaSet, но НЕ созданные им Pod

```
kubectl delete -f rs.yaml --cascade=orphan
```

4. Убедиться, что ReplicaSet удалён, а Pod по-прежнему работают

```
kubectl get rs # реплик нет
kubectl get po # Pod по-прежнему работают
```

5. Снова создать тот же ReplicaSet, ничего не меняя

```
kubectl apply -f rs.yaml
```

6. Убедиться, что ReplicaSet использовал существующие Pod и не создал новые

```
kubectl describe rs web  # Новых событий быть не должно, а если вывести список Pod через 'kubectl get po -f rs.yaml`, будет видно, что у них те же имена
```

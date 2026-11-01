## ReplicaSet 01 — решение

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

3. Удалить один из Pod, созданных ReplicaSet

```
kubectl delete po <POD_NAME>
```

4. Что будет видно, если сейчас вывести список всех Pod?

```
The same number of Pods. Since we defined 2 replicas, the ReplicaSet will make sure to create another Pod that will replace the one you've deleted.
```

5. Удалить созданный ReplicaSet

```
kubectl delete -f rs.yaml
```

6. Убедиться, что ReplicaSet удалён

```
kubectl get rs
# ИЛИ более конкретный способ: kubectl get -f rs.yaml
```

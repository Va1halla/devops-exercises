## ReplicaSet 03 — решение

1. Создать ReplicaSet с 2 репликами. Метка, используемая в селекторе и в Pod, должна быть "type=web"

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

3. Вывести список запущенных Pod и где-нибудь сохранить вывод

```
kubectl get po > running_pods.txt
```

4. Удалить метку (type=web) у одного из Pod, созданных ReplicaSet

```
kubectl label pod <POD_NAME> type-
```

5. Вывести список запущенных Pod. Стало ли Pod больше после удаления метки? Почему?

```
Yes, there is an additional Pod running because once the label (used as a matching selector) was removed, the Pod became independent meaning, it's not controlled by the ReplicaSet anymore and the ReplicaSet was missing replicas based on its definition so, it created a new Pod.
```

6. Убедиться, что ReplicaSet действительно создал новый Pod

```
kubectl describe rs web
```

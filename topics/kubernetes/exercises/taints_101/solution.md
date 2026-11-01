# Taints 101

## Цели

1. Проверить, есть ли у одного из узлов кластера ограничения (taints) (неважно, у какого узла)
2. Создать taint на одном из узлов кластера с ключом "app", значением "web" и эффектом "NoSchedule"
   1. Объяснить, что именно он делает
   2. Убедиться, что он применён

## Решение

1. `kubectl describe no minikube | grep -i taints`
2. `kubectl taint node minikube app=web:NoSchedule`
   1. Ни один ресурс с парой ключ-значение "app=web" не будет запланирован (scheduled) на узел `minikube`
   2. `kubectl describe no minikube | grep -i taints`
3. 

```
kubectl run some-pod --image=redis
kubectl edit po some-pod
```

```
 - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Сохранить и выйти. Pod должен запуститься.
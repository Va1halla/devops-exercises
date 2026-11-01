# Селекторы узлов (Node Selectors)

## Цели

1. Повесить метку "hw=max" на один из узлов кластера
2. Создать и запустить Pod с именем `some-pod` из образа `redis` и настроить его на использование селектора `hw=max`
3. Объяснить, почему возможности селекторов узлов могут быть ограничены


## Решение

Нажмите [здесь](solution.md), чтобы посмотреть решение

1. `kubectl label nodes some-node hw=max`
2. 

```
kubectl run some-pod --image=redis --dry-run=client -o yaml > pod.yaml

vi pod.yaml

spec:
  nodeSelector:
    hw: max

kubectl apply -f pod.yaml
```

3. Предположим, нужно запускать Pod на всех узлах, у которых `hw` равно max или min, а не только max. С nodeSelectors это невозможно — они довольно упрощённые, и здесь стоит рассмотреть `node affinity`.
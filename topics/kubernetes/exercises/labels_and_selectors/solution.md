# Метки и селекторы (Labels and Selectors) 101

## Цели

1. Как вывести список всех Pod с меткой "app=web"?
2. Как вывести список всех объектов с меткой "env=staging"?
3. Как вывести список всех развёртываний (Deployment) с метками "env=prod" и "type=web"?

## Решение

`k get po -l app=web`
`k get all -l env=staging`
`k get deploy -l env=prod,type=web`
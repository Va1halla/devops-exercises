## «Убийство» контейнеров — решение

1. Запустить Pod с веб-сервисом (например, httpd) - `kubectl run web --image registry.redhat.io/rhscl/httpd-24-rhel7`
2. С помощью команды `ps` убедиться, что веб-сервис работает - `kubectl exec web -- ps`
3. Проверить, сколько перезапусков выполнил Pod - `kubectl get po web`
4. Завершить (kill) процесс веб-сервиса -`kubectl exec web -- kill 1`
5. Проверить, сколько перезапусков выполнил Pod - `kubectl get po web`
6. Снова убедиться, что веб-сервис работает - `kubectl exec web -- ps`

## После выполнения упражнения


* Почему увеличилось значение счётчика "RESTARTS"? - `Kubernetes restarted the Pod because we killed the process and the container was not running properly.`
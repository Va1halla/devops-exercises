## ELK + Filebeat

Настройте следующее, используя любой лог на ваш выбор:

* Запустите elasticsearch, logstash, kibana и filebeat (каждый в своём контейнере)
* Настройте filebeat на передачу лога в logstash для обработки
* После обработки в logstash проиндексируйте данные с помощью elasticsearch
* Наконец, убедитесь, что данные доступны в Kibana

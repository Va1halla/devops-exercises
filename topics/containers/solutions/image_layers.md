## Слой за слоем

### Цель

Изучить слои образов

### Требования

Убедитесь, что в системе установлен Docker и служба запущена

```
# Fedora/RHEL/CentOS
rpm -qa | grep docker
systemctl status docker
```

### Инструкции

1. Напишите Dockefile. Любой Dockefile! :) (только убедитесь, что он корректный)

```
FROM ubuntu
EXPOSE 212
ENV foo=bar
WORKDIR /tmp
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
```

2. Соберите образ с помощью написанного Dockerfile

`docker image build -t super_cool_app:latest .`

3. Какие из использованных инструкций создали новые слои, а какие добавили метаданные образа?

```
FROM, RUN -> new layer
EXPOSE, ENV, WORKDIR -> metadata
```

4. Какими способами можно проверить ответ на предыдущий вопрос?

Можно выполнить `docker image history super_cool_app`. Команда покажет каждую инструкцию и её размер. Обычно инструкции, создающие новые слои, имеют ненулевой размер, но полагаться только на это нельзя, поскольку некоторые команды run могут иметь нулевой размер в выводе `docker image history` (например, `ls -l`).

Также можно использовать `docker image inspect super_cool_appl` и проверить, совпадает ли в выводе, в разделе "RootFS", количество слоёв с количеством инструкций, которые должны создавать новые слои.

5. Можно ли уменьшить размер созданного образа?

Да, например, объединить все инструкции RUN в одну инструкцию RUN следующим образом:

`RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024`

В данном случае изменение размера может быть не очень заметным, но в некоторых случаях это сильно влияет на размер образа.

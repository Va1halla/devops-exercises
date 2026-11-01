# Веб-сервер в контейнере

1. Запустите веб-сервер в контейнере в фоновом режиме и привяжите его порт (8080) к локальному порту
2. Убедитесь, что порт (8080) привязан
3. Обратитесь к веб-серверу с локального хоста
4. Теперь запустите то же веб-приложение, но привяжите его к локальному порту 8080

## Решение

```
$ podman run -d -p 8080 httpd # запустить контейнер и привязать порт 8080 к локальному порту
$ podman port -l 8080 # показать, к какому локальному порту привязан порт 8080 контейнера
0.0.0.0:41203
$ curl http://0.0.0.0:41203 # использовать порт из вывода предыдущей команды

!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<title>Test Page for the HTTP Server on Red Hat Enterprise Linux</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

$ podman run -d -p 8080:8080 httpd
```

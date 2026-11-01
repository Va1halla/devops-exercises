## Grafana

<details>
<summary>Объясните, что такое Grafana</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/introduction): «Grafana — это полноценный стек наблюдаемости, позволяющий мониторить и анализировать метрики, логи и трассировки. Он позволяет выполнять запросы, визуализировать, настраивать оповещения и понимать данные, где бы они ни хранились. Создавайте, исследуйте красивые дашборды и делитесь ими с командой, развивая культуру, основанную на данных.»
</b></details>

<details>
<summary>Что такое Grafana Cloud?</summary><br><b>

[Grafana cloud](https://grafana.com/products/cloud/) — это редакция Grafana, предлагаемая как сервис через облако. Стек наблюдаемости настраивается, администрируется и поддерживается Grafana Labs; доступны бесплатные и платные варианты. Также можно отправлять данные из существующих источников данных, например Promethetus, Loki, и визуализировать существующие данные временных рядов.
</b></details>

<details>
<summary>Что такое Grafana Enterprise?</summary><br><b>

[Grafana Enterprise](https://grafana.com/docs/grafana/latest/enterprise/#enterprise-plugins) — это коммерческая редакция Grafana с корпоративными возможностями, такими как плагины _Enterprise datasource_ и встроенные функции совместной работы. Редакция включает постоянную поддержку и обучение от команды Grafana.
</b></details>
 
<details>
<summary>Какой HTTP-порт у Grafana по умолчанию?</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): по умолчанию Grafana работает на порту 3000.
</b></details>

<details>
<summary>Объясните, как принудительно включить HTTPS</summary><br><b>

[Сообщество Grafana](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): установите протокол _https_ в настройках конфигурации, после чего Grafana будет ожидать, что клиенты отправляют запросы по протоколу HTTPS. Любой клиент, использующий HTTP, получит ошибку SSL/TLS.
</b></details>

<details>
<summary>Как установить плагины для Grafana?</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/plugins/installation/): перейдите на [страницу плагинов Grafana](https://grafana.com/grafana/plugins/), найдите нужный плагин и нажмите на него, затем откройте вкладку installation. Есть два способа установки в зависимости от того, где работает сервер Grafana:
- Cloud: в поле **For** на вкладке установки выберите имя организации, в которую нужно установить плагин (если вы не состоите только в одной), затем нажмите **install plugin**. Grafana cloud автоматически установит плагин в ваш инстанс Grafana, 
возможно, потребуется выйти и снова войти, чтобы увидеть плагин.
- Локальная grafana: можно использовать Grafana CLI, который позволяет выводить список доступных плагинов и устанавливать их.
```
grafana-cli plugins list-remote
grafana-cli plugins install <plugin-id>
```
Также можно установить упакованный плагин, скачав файл с вкладки установки и распаковав архив в каталог плагинов. Путь к каталогу плагинов указан в файле конфигурации 
 ```
 unzip my-plugin-0.2.0.zip -d YOUR_PLUGIN_DIR/my-plugin
 ```
</b></details>

<details>
<summary>Объясните, что такое 'Data source'</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/datasources/): источник данных (data source) — это бэкенд хранения, который служит источником данных для Grafana. Популярные источники данных: Prometheus, InfluxDB, Loki, AWS cloudwatch.
</b></details>

<details>
<summary>Что такое "Default configuration"?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/administration/configuration/): конфигурация по умолчанию содержит настройки, которые Grafana использует по умолчанию. Расположение зависит от ОС; обратите внимание, что $WORKING_DIR обозначает рабочий каталог Grafana.
- Windows: ```$WORKING_DIR/conf/defaults.ini```
- Linux: ```/etc/grafana/grafana.ini```
- macOS: ```/usr/local/etc/grafana/grafana.ini```
</b></details>
 
<details>
<summary>Объясните, как добавить пользовательскую конфигурацию (Custom configuration) в Grafana</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/administration/configuration/): 
Пользовательскую конфигурацию можно задать, изменив файл пользовательской конфигурации либо добавив переменные окружения, которые переопределяют конфигурацию по умолчанию. Настройка зависит от ОС:
- Windows: в том же каталоге, что и файл defaults.ini, есть файл ```sample.ini```; скопируйте sample.ini и назовите копию ```custom.ini```. Раскомментируйте настройки, которые нужно переопределить.
- Linux: отредактируйте файл конфигурации ```/etc/grafana/grafana.ini```
- macOS: добавьте файл конфигурации с именем ```custom.ini``` в папку conf; если Grafana установлена через Homebrew, можно вручную отредактировать ```conf/defaults.ini```
- Docker: существующую конфигурацию Grafana можно переопределить переменными окружения. Пример — задание имени инстанса Grafana: ```E.g. export GF_DEFAULT_INSTANCE_NAME=my-instance```
</b></details>

<details>
<summary>Какая внешняя аутентификация поддерживается «из коробки»?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/auth/overview/): Grafana Auth — это встроенная система аутентификации, в которой по умолчанию включена аутентификация по паролю.
</b></details>

<details>
<summary>Как импортировать дашборд в инстанс Grafana?</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/dashboards/export-import/): дашборды Grafana можно импортировать через интерфейс Grafana. Нажмите на значок + на боковой панели, а затем import. Импортировать дашборд можно следующими способами:
- Загрузить JSON-файл дашборда, экспортированный из интерфейса Grafana или полученный через [HTTPS API](https://grafana.com/docs/grafana/latest/http_api/dashboard/#create-update-dashboard
)
- Вставить в текстовое поле URL дашборда Grafana, который можно найти на [grafana Dashboards](https://grafana.com/grafana/dashboards/), или уникальный id дашборда.
- Вставить «сырой» JSON дашборда в область панели.
После этого нажмите load.
</b></details>

<details>
<summary>В каком формате хранятся данные дашборда?</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/dashboards/json-model/): дашборды Grafana представлены в JSON-файлах в виде объектов; они хранят метаданные дашборда, например свойства дашборда, метаданные панелей и переменные.

</b></details>

<details>
<summary>Опишите шаги, чтобы поделиться дашбордом с командой</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/sharing/share-dashboard/): перейдите на главную страницу инстанса grafana. Нажмите на значок share в верхней навигации — появятся три вкладки, открыта будет вкладка link.
- Direct link: нажмите copy и отправьте ссылку пользователю Grafana; учтите, что у пользователя должны быть права на просмотр ссылки. Это делается добавлением пользователя в команду (team).
- Public Snapshot: нажмите local snapshot, чтобы опубликовать снимок в локальном инстансе Grafana, или Publish to snapshots.raintank.io — бесплатный сервис для публикации снимков дашбордов во внешний инстанс Grafana
Можно настроить истечение срока действия снимков через определённое время и значение таймаута для сбора метрик дашборда
</b></details>
 
<details>
<summary>Как организовать дашборды и пользователей в Grafana?</summary><br><b>

[Документация Grafana](https://grafana.com/blog/2022/03/14/how-to-best-organize-your-teams-and-resources-in-grafana/
): Grafana labs рекомендует создавать папки (Folders) для группировки дашбордов, библиотечных панелей и оповещений. Пользователей можно организовывать с помощью команд (Teams), которые выдают права участникам группы.
- [Folders](https://grafana.com/docs/grafana/latest/dashboards/dashboard_folders/): нажмите на значок + на боковой панели, затем "Create folder". На странице создания папки введите уникальное имя папки и нажмите "Create"
- [Teams](https://grafana.com/tutorials/create-users-and-teams/) Для создания Teams нужно быть администратором сервера. 
 1. Нажмите на значок администратора сервера (щит) на боковой панели, затем на вкладке Users нажмите New user.
 2. Введите данные пользователя, например имя, E-mail, Username и Password. Пользователь может позже сменить пароль
 3. Нажмите Create, чтобы создать учётную запись пользователя.
</b></details>
 
<details>
<summary>Опишите шаги создания 'Alert'</summary><br><b>

[Документация Grafana](https://grafana.com/docs/grafana/latest/alerting/old-alerting/create-alerts/): 
 
 «Перейдите к панели, для которой нужно добавить или изменить правило оповещения, нажмите на заголовок, а затем Edit. На вкладке Alert нажмите Create Alert. Если для этой панели оповещение уже существует, можно просто отредактировать поля на вкладке Alert. Заполните поля. Описания приведены ниже в разделе Alert rule fields. Закончив писать правило, нажмите Save в правом верхнем углу, чтобы сохранить правило оповещения и дашборд. (Необязательно, но рекомендуется) Нажмите Test rule, чтобы убедиться, что правило возвращает ожидаемые результаты»
</b></details>

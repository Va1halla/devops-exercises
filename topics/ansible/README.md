## Ansible

<!-- {% raw %} -->

### Упражнения по Ansible

|Название|Тема|Цель и инструкции|Решение|Комментарии|
|--------|--------|------|----|----|
| Моя первая задача | Задачи (Tasks) | [Упражнение](my_first_task.md) | [Решение](solutions/my_first_task.md)
| Задача обновления (upgrade и update) | Задачи (Tasks) | [Упражнение](update_upgrade_task.md) | [Решение](solutions/update_upgrade_task.md)
| Мой первый playbook | Playbooks | [Упражнение](my_first_playbook.md) | [Решение](solutions/my_first_playbook.md)
	

### Самопроверка по Ansible

<details>
<summary>Опишите каждый из следующих компонентов Ansible, включая связи между ними:

  * Task
  * Inventory	
  * Module
  * Play
  * Playbook
  * Role
</summary><br><b>

Task (задача) — вызов определённого модуля Ansible
Module (модуль) — собственно единица кода, которую Ansible выполняет на вашем или удалённом хосте. Модули распределены по категориям (database, file, network, …) и также называются плагинами задач (task plugins).
	
Inventory (инвентарь) — файл инвентаря определяет хосты и/или группы хостов, на которых выполняются задачи Ansible. Файл инвентаря может быть в одном из многих форматов в зависимости от имеющихся плагинов инвентаря. Самые распространённые форматы — INI и YAML.

Play (сценарий) — одна или несколько задач, выполняемых на заданном хосте (хостах)

Playbook — один или несколько play. Каждый play может выполняться на тех же или на других хостах

Role (роль) — роли Ansible позволяют группировать ресурсы по определённой функциональности/сервису так, чтобы их было легко переиспользовать. В роли есть каталоги для переменных (variables), значений по умолчанию (defaults), файлов (files), шаблонов (templates), обработчиков (handlers), задач (tasks) и метаданных (metadata). Затем роль можно использовать, просто указав её в playbook.
</b></details>

<details>
<summary>Чем Ansible отличается от других инструментов автоматизации? (например, Chef, Puppet и т. д.)</summary><br><b>

Ansible:

* Не требует агентов (agentless)
* Минимальные требования для запуска (Python и SSH) и простота использования
* Режим по умолчанию — "push" (поддерживается и pull)
* Ориентирован на простоту и удобство использования
</b></details>


<details>
<summary>Верно или неверно? Ansible следует парадигме изменяемой (mutable) инфраструктуры</summary><br><b>

Верно. При подходе с неизменяемой (immutable) инфраструктурой инфраструктура заменяется, а не изменяется.<br>
Ansible скорее следует парадигме изменяемой инфраструктуры, позволяя менять конфигурацию различных компонентов, но этот подход не идеален и имеет свои недостатки, например «дрейф конфигурации» (configuration drift), когда разные компоненты по разным причинам могут прийти к разному состоянию.
</b></details>

<details>
<summary>Верно или неверно? Ansible использует декларативный стиль для описания ожидаемого конечного состояния</summary><br><b>

Неверно. Он использует процедурный стиль.
</b></details>

<details>
<summary>Какую автоматизацию не стоит делать с помощью Ansible и почему?</summary><br><b>

Хотя с помощью Ansible можно создавать (provision) ресурсы, некоторые предпочитают инструменты, следующие парадигме неизменяемой инфраструктуры.
Ansible по умолчанию не сохраняет состояние (state). Поэтому задача, которая, например, создаёт 5 инстансов, при повторном выполнении создаст ещё 5 инстансов (если
не реализована дополнительная проверка или не заданы явные имена), тогда как другие инструменты могут проверить, существуют ли 5 инстансов. Если существует только 4 (например, по файлу состояния), будет создан один дополнительный инстанс, чтобы достичь конечной цели — 5 инстансов.
</b></details>

<details>
<summary>Как вывести список всех модулей и как посмотреть подробности о конкретном модуле?</summary><br><br>

1. Онлайн-документация Ansible
2. `ansible-doc -l` — список модулей, `ansible-doc [module_name]` — подробная информация о конкретном модуле
</b></details>

#### Ansible — инвентарь (Inventory)

<details>
<summary>Что такое файл инвентаря и как его определить?</summary><br><b>

Файл инвентаря определяет хосты и/или группы хостов, на которых выполняются задачи Ansible.

Пример файла инвентаря:

```
192.168.1.2
192.168.1.3
192.168.1.4

[web_servers]
190.40.2.20
190.40.2.21
190.40.2.22
```
</b></details>

<details>
<summary>Что такое динамический инвентарь? Когда его использовать?</summary><br><br>

Динамический файл инвентаря отслеживает хосты из одного или нескольких источников, таких как облачные провайдеры и системы CMDB.

Его следует использовать при работе с внешними источниками, особенно когда хосты в вашей среде автоматически<br>
создаются и выключаются, а вы не отслеживаете каждое изменение в этих источниках.
</b></details>

#### Ansible — переменные

<details>
<summary>Измените следующую задачу так, чтобы вместо значения "zlib" использовалась переменная, а "zlib" было значением по умолчанию, если переменная не определена

```
- name: Install a package
  package:
    name: "zlib"
    state: present
```
</summary><br><b>

```
- name: Install a package
  package:
    name: "{{ package_name|default('zlib') }}"
    state: present
```
</b></details>

<details>
<summary>Как сделать переменную "use_var" необязательной?

```
- name: Install a package
  package:
    name: "zlib"
    state: present
    use: "{{ use_var }}"
```
</summary><br><b>


С помощью "default(omit)"
```
- name: Install a package
  package:
    name: "zlib"
    state: present
    use: "{{ use_var|default(omit) }}"
```
</b></details>

<details>
<summary>Каким будет результат выполнения следующего play?</summary><br><b>

```
---
- name: Print information about my host
  hosts: localhost
  gather_facts: 'no'
  tasks:
      - name: Print hostname
        debug:
            msg: "It's me, {{ ansible_hostname }}"
```

Получив готовый код, всегда тщательно его изучайте. Если ваш ответ — «это завершится ошибкой», то вы правы. Мы используем факт (ansible_hostname) — информацию, собранную с хоста, на котором выполняется play. Но в данном случае сбор фактов отключён (gather_facts: no), поэтому переменная будет не определена, что приведёт к ошибке.
</b></details>

<details>
<summary>Когда в этом случае будет использовано значение '2017'': `{{ lookup('env', 'BEST_YEAR') | default('2017', true) }}`?</summary><br><b>

когда переменная окружения 'BEST_YEAR' пуста или имеет значение false.
</b></details>

<details>
<summary>Если значение некоторой переменной равно 1, нужно использовать значение "one", иначе — "two". Как это сделать?</summary><br><b>

`{{ (certain_variable == 1) | ternary("one", "two") }}`
</b></details>

<details>
<summary>Значение используемой переменной — строка "True". Нужно, чтобы значение было булевым. Как выполнить приведение типа?</summary><br><b>

`{{ some_string_var | bool }}`
</b></details>

<details>
<summary>Нужно запускать playbook Ansible только на определённой минорной версии ОС. Как этого добиться?</summary><br><b>
</b></details>

<details>
<summary>Для чего в Ansible используется директива "become"?</summary><br><b>
</b></details>

<details>
<summary>Что такое факты (facts)? Как посмотреть все факты определённого хоста?</summary><br><b>
</b></details>

<details>
<summary>Каким будет результат выполнения следующей задачи? Как это исправить?

```
- hosts: localhost
  tasks:
      - name: Install zlib
        package:
          name: zlib
          state: present
```
</summary><br><b>
</b></details>

<details>
<summary>Какие лучшие практики Ansible вам известны? Назовите хотя бы три</summary><br><b>
</b></details>

<details>
<summary>Объясните структуру каталогов роли Ansible</summary><br><b>
</b></details>

<details>
<summary>Для чего в Ansible используются блоки ('blocks')?</summary><br><b>
</b></details>

<details>
<summary>Как обрабатывать ошибки в Ansible?</summary><br><b>
</b></details>

<details>
<summary>Нужно выполнить определённую команду, если задача завершилась с ошибкой. Как этого добиться?</summary><br><b>
</b></details>

<details>
<summary>Напишите playbook, устанавливающий ‘zlib’ и ‘vim’ на все хосты, если в системе существует файл ‘/tmp/mario’.</summary><br><b>

```
---
- hosts: all
  vars:
      mario_file: /tmp/mario
      package_list:
          - 'zlib'
          - 'vim'
  tasks:
      - name: Check for mario file
        stat:
            path: "{{ mario_file }}"
        register: mario_f

      - name: Install zlib and vim if mario file exists
        become: "yes"
        package:
            name: "{{ item }}"
            state: present
        with_items: "{{ package_list }}"
        when: mario_f.stat.exists
```
</b></details>

<details>
<summary>Напишите одну задачу, которая проверяет, что все файлы из переменной files_list существуют на хосте</summary><br><b>

```
- name: Ensure all files exist
  assert:
    that:
      - item.stat.exists
  loop: "{{ files_list }}"
```
</b></details>

<details>
<summary>Напишите playbook, размещающий файл ‘/tmp/system_info’ на всех хостах, кроме группы controllers, со следующим содержимым</summary><br><b>

  ```
  I'm <HOSTNAME> and my operating system is <OS>
  ```

  Замените <HOSTNAME> и  <OS> реальными данными конкретного хоста, на котором выполняется playbook

Playbook для размещения файла system_info

```
---
- name: Deploy /tmp/system_info file
  hosts: all:!controllers
  tasks:
      - name: Deploy /tmp/system_info
        template:
            src: system_info.j2
            dest: /tmp/system_info
```

Содержимое шаблона system_info.j2

```
# {{ ansible_managed }}
I'm {{ ansible_hostname }} and my operating system is {{ ansible_distribution }
```
</b></details>

<details>
<summary>Переменная 'whoami' определена в следующих местах:

  * role defaults -> whoami: mario
  * extra vars (переменные, передаваемые в Ansible CLI через -e) -> whoami: toad
  * host facts -> whoami: luigi
  * переменные инвентаря (тип не важен) -> whoami: browser

Какое значение будет использовано согласно приоритету переменных?</summary><br><b>

Правильный ответ — ‘toad’.

Приоритет переменных (variable precedence) определяет, как переменные переопределяют друг друга, когда они заданы в разных местах. Если вы с этим ещё не сталкивались, уверен, однажды столкнётесь, поэтому эту тему полезно знать.

В контексте нашего вопроса порядок будет таким: extra vars (всегда переопределяют любые другие переменные) -> host facts -> переменные инвентаря -> role defaults (самые слабые).

Ниже порядок приоритета от наименьшего к наибольшему (последние в списке побеждают):

1. значения из командной строки (например, “-u user”)
2. role defaults [[1\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id15)
3. group vars из файла или скрипта инвентаря [[2\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id16)
4. inventory group_vars/all [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
5. playbook group_vars/all [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
6. inventory group_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
7. playbook group_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
8. host vars из файла или скрипта инвентаря [[2\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id16)
9. inventory host_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
10. playbook host_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
11. host facts / кэшированные set_facts [[4\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id18)
12. play vars
13. play vars_prompt
14. play vars_files
15. role vars (определённые в role/vars/main.yml)
16. block vars (только для задач в блоке)
17. task vars (только для данной задачи)
18. include_vars
19. set_facts / registered vars
20. параметры role (и include_role)
21. параметры include
22. extra vars (всегда имеют наивысший приоритет)

Полный список можно найти в разделе  [PlayBook Variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#ansible-variable-precedence) . Также учтите, что между Ansible 1.x и 2.x есть существенная разница.
</b></details>

<details>
<summary>Для каждого из следующих утверждений определите, верно оно или нет:

  * Модуль — это набор задач
  * Лучше использовать shell или command, чем специализированный модуль
  * Host facts переопределяют переменные play
  * Роль может включать следующее: vars, meta и handlers
  * Динамический инвентарь формируется путём извлечения информации из внешних источников
  * Лучшая практика — использовать отступ в 2 пробела вместо 4
  * ‘notify’ используется для запуска обработчиков (handlers)
  * Запись “hosts: all:!controllers” означает ‘выполнять только на хостах группы controllers</summary><br><b>
</b></details>

<details>
<summary>Объясните разницу между Forks, Serial и Throttle.</summary><br><b>

`Serial` — это как запуск playbook для каждого хоста по очереди: прежде чем перейти к следующему хосту, ожидается завершение всего playbook. `forks`=1 означает, что первая задача play выполняется на одном хосте, прежде чем та же задача будет выполнена на следующем, то есть первая задача выполнится для каждого хоста до того, как начнётся следующая задача. По умолчанию в ansible fork равен 5.

```
[defaults]
forks = 30
```

```
- hosts: webservers
  serial: 1
  tasks:
    - name: ...
```

Ansible также поддерживает `throttle`. Это ключевое слово ограничивает число рабочих процессов (workers) вплоть до максимума, заданного через forks или serial. Это может быть полезно для ограничения задач, которые сильно нагружают CPU или взаимодействуют с API, ограничивающим частоту запросов (rate limiting)

```
tasks:
- command: /path/to/cpu_intensive_command
  throttle: 1
```

</b></details>

<details>
<summary>Что такое ansible-pull? Чем он отличается от того, как работает ansible-playbook?</summary><br><b>
</b></details>

<details>
<summary>Что такое Ansible Vault?</summary><br><b>
</b></details>

<details>
<summary>Продемонстрируйте с помощью Ansible каждое из следующего:

  * Условия (conditionals)
  * Циклы (loops)
</summary><br><b>
</b></details>

<details>
<summary>Что такое фильтры (filters)? Есть ли у вас опыт написания фильтров?</summary><br><b>
</b></details>

<details>
<summary>Напишите фильтр, делающий первую букву строки заглавной</summary><br><b>

```
def cap(self, string):
    return string.capitalize()
```
</b></details>

<details>
<summary>Нужно выполнить задачу, только если предыдущая задача что-то изменила. Как этого добиться?</summary><br><b>
</b></details>

<details>
<summary>Что такое callback-плагины? Чего можно добиться с их помощью?</summary><br><b>
</b></details>

<details>
<summary>В чём разница между `include_task` и `import_task`?</summary><br><b>
</b></details>

<details>
<summary>Файл '/tmp/exercise' содержит следующее

```
Goku = 9001
Vegeta = 5200
Trunks = 6000
Gotenks = 32
```

С помощью одной задачи измените содержимое на:

```
Goku = 9001
Vegeta = 250
Trunks = 40
Gotenks = 32
```
</summary><br><b>

```
- name: Change saiyans levels
  lineinfile:
    dest: /tmp/exercise
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
  with_items:
    - { regexp: '^Vegeta', line: 'Vegeta = 250' }
    - { regexp: '^Trunks', line: 'Trunks = 40' }
    ...
```
</b></details>


#### Ansible — выполнение и стратегия

<details>
<summary>Верно или неверно? По умолчанию Ansible выполняет все задачи play на одном хосте, прежде чем перейти к следующему хосту</summary><br><b>

Неверно. Ansible выполняет одну задачу на всех хостах, прежде чем перейти к следующей задаче в play. На сегодняшний день по умолчанию используется 5 форков (forks).<br>
Это поведение в Ansible называется «стратегией» (strategy), и оно настраивается.
</b></details>

<details>
<summary>Что такое «стратегия» (strategy) в Ansible? Какая стратегия используется по умолчанию?</summary><br><b>

Стратегия в Ansible описывает, как Ansible будет выполнять задачи на хостах. По умолчанию Ansible использует «линейную стратегию» (Linear strategy), при которой каждая задача выполняется на всех хостах, прежде чем перейти к следующей задаче.
</b></details>

<details>
<summary>Какие стратегии Ansible вам известны?</summary><br><b>

  - Linear: стратегия по умолчанию в Ansible. Каждая задача выполняется на всех хостах, прежде чем перейти дальше.
  - Free: для каждого хоста все задачи до конца play выполняются как можно быстрее
  - Debug: задачи выполняются в интерактивном режиме
</b></details>

<details>
<summary>Для чего используется ключевое слово <code>serial</code>?</summary><br><b>

Оно задаёт количество (или процент) хостов, на которых выполняется весь play, прежде чем перейти к следующей порции хостов в группе.

Например:
```
- name: Some play
  hosts: databases
  serial: 4
```

Если в группе 8 хостов, весь play будет выполнен на 4 хостах, а затем тот же play — на других 4 хостах.
</b></details>

#### Тестирование Ansible

<details>
<summary>Как вы тестируете проекты на основе Ansible?</summary><br><b>
</b></details>

<details>
<summary>Что такое Molecule? Как он работает?</summary><br><b>

Он используется для быстрой разработки и тестирования ролей Ansible.  С помощью Molecule можно одновременно тестировать роли Ansible на множестве дистрибутивов Linux.  Такая возможность тестирования помогает быть уверенным в автоматизации как сейчас, так и со временем, пока роль сопровождается.  

</b></details>

<details>
<summary>При запуске тестов Ansible вы получаете "idempotence test failed". Что это значит? Почему важна идемпотентность?</summary><br><b>
</b></details>

#### Ansible — отладка

<details>
<summary>Как узнать тип данных определённой переменной в одном из playbook?</summary><br><b>

"{{ some_var | type_debug }}"
</b></details>

#### Ansible — коллекции (Collections)

<details>
<summary>Что такое коллекции в Ansible?</summary><br><b>
Коллекции Ansible (Ansible Collections) — это способ упаковывать и распространять модули, роли, плагины и документацию в структурированном формате. Они помогают эффективно организовывать и распространять код автоматизации, особенно для сложных сред.
</b></details>

<details>
<summary>Зачем использовать коллекции Ansible?</summary><br><b>

  - Модульные и переиспользуемые компоненты
  - Упрощают управление собственными и сторонними модулями
  - Дают стандартизированный способ распространения контента автоматизации
  - Помогают в управлении версиями и зависимостями
</b></details>

<!-- {% endraw %} -->

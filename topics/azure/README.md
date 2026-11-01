# Azure

- [Azure](#azure)
  - [Вопросы](#вопросы)
    - [Azure 101](#azure-101)
    - [Azure Resource Manager](#azure-resource-manager)
    - [Вычисления](#вычисления)
    - [Сеть](#сеть)
    - [Хранилище](#хранилище)
    - [Безопасность](#безопасность)

## Вопросы

### Azure 101

<details>
<summary>Что такое Azure Portal?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): «Azure portal — это веб-консоль с единым интерфейсом, которая служит альтернативой инструментам командной строки. С помощью Azure portal можно управлять подпиской Azure через графический интерфейс пользователя.»
</b></details>

<details>
<summary>Что такое Azure Marketplace?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): «Azure marketplace помогает связать пользователей с партнёрами Microsoft, независимыми поставщиками ПО и стартапами, которые предлагают свои решения и сервисы, оптимизированные для работы в Azure.»
</b></details>

<details>
<summary>Объясните, что такое availability sets и availability zones</summary><br><b>

Availability set (группа доступности) — это логическая группировка VM, которая позволяет Azure понять, как построено приложение, чтобы обеспечить избыточность и доступность. Рекомендуется создавать две или более VM в группе доступности, чтобы обеспечить высокую доступность приложения и соответствие SLA Azure в 99.95%.
</b></details>

<details>
<summary>Что такое Azure Policy?</summary><br><b>


[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/overview): «Azure Policy помогает применять организационные стандарты и оценивать соответствие (compliance) в масштабе. Через свой дашборд соответствия он предоставляет агрегированное представление для оценки общего состояния среды с возможностью детализации до уровня отдельных ресурсов и политик. Он также помогает привести ресурсы в соответствие с помощью массового исправления для существующих ресурсов и автоматического исправления для новых ресурсов.»
</b></details>

<details>
<summary>Объясните, что такое управляемые диски (managed disks) Azure</summary><br><b>
</b></details>

### Azure Resource Manager

<details>
<summary>Объясните, что такое Azure Resource Manager</summary><br><b>

Из [документации Azure](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview): «Azure Resource Manager — это сервис развёртывания и управления для Azure. Он предоставляет уровень управления, позволяющий создавать, обновлять и удалять ресурсы в аккаунте Azure. Функции управления, такие как контроль доступа, блокировки (locks) и теги, используются для защиты и организации ресурсов после развёртывания.»
</b></details>

<details>

<summary>Из каких разделов состоит шаблон ARM?</summary><br><b>

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview): Шаблон состоит из следующих разделов:

Parameters - передают значения во время развёртывания, что позволяет использовать один и тот же шаблон в разных средах.

Variables - определяют значения, которые повторно используются в шаблонах. Их можно строить из значений параметров.

User-defined functions - пользовательские функции, упрощающие шаблон.

Resources - задают ресурсы для развёртывания.

Outputs - возвращают значения из развёрнутых ресурсов.
</b></details>

<details>

<summary>Что такое Azure Resource Group?</summary><br><b>

Из [документации Azure](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal): «Группа ресурсов (resource group) — это контейнер, который содержит связанные ресурсы решения Azure. Группа ресурсов может включать все ресурсы решения или только те, которыми нужно управлять как группой.»
</b></details>

### Вычисления

<details>
<summary>С какими вычислительными сервисами Azure вы знакомы?</summary><br><b>

  * Azure Virtual Machines
  * Azure Batch
  * Azure Service Fabric
  * Azure Container Instances
  * Azure Virtual Machine Scale Sets
</b></details>

<details>

<summary>Для чего используется сервис "Azure Virtual Machines"?</summary><br><b>

Azure VM поддерживают ОС Windows и Linux. Их можно использовать для размещения веб-серверов, приложений, резервных копий, баз данных, а также в качестве jump-сервера или self-hosted агента Azure для сборки и развёртывания приложений.
</b></details>

<details>
<summary>Для чего используется сервис "Azure Virtual Machine Scale Sets"?</summary><br><b>

Для масштабирования виртуальных машин Linux или Windows; он позволяет создавать группу VM с балансировкой нагрузки и управлять ею. Количество инстансов VM может автоматически увеличиваться или уменьшаться в зависимости от нагрузки или заданного расписания.
</b></details>

<details>
<summary>Для чего используется сервис "Azure Functions"?</summary><br><b>

Azure Functions — это бессерверный (serverless) вычислительный сервис Azure.
</b></details>

<details>
<summary>Что такое "Durable Azure Function"?</summary>
<br>

[Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): Durable Functions — это расширение Azure Functions, позволяющее писать функции с сохранением состояния (stateful) в бессерверной вычислительной среде.
</details>

<details>
<summary>Для чего используется сервис "Azure Container Instances"?</summary><br><b>

Для запуска контейнеризированных приложений (без необходимости создавать виртуальные машины).
</b></details>

<details>
<summary>Для чего используется сервис "Azure Batch"?</summary><br><b>

Для запуска параллельных и высокопроизводительных вычислительных приложений
</b></details>

<details>
<summary>Для чего используется сервис "Azure Service Fabric"?</summary><br><b>
</b></details>

<details>
<summary>Для чего используется сервис "Azure Kubernetes"?</summary><br><b>
</b></details>

### Сеть

<details>
<summary>С какими сетевыми сервисами Azure вы знакомы?</summary><br><b>
</b></details>
<details>
<summary>Объясните, что такое VNet peering</summary><br><b>

VNet peering позволяет соединять виртуальные сети. Это означает, что можно маршрутизировать трафик между ресурсами соединённых VNet в частном порядке через IPv4-адреса. Соединение VNet в пределах одного региона называется regional VNet Peering, а соединение VNet в разных регионах Azure — global VNet Peering.

</b></details>

<details>
<summary>Что такое регион Azure?</summary><br><b>

Регион Azure — это набор центров обработки данных, развёрнутых в пределах определённого периметра и соединённых выделенной региональной сетью с низкой задержкой.
</b></details>

<details>
<summary>Что такое N-уровневая (N-tier) архитектура?</summary><br><b>

N-уровневая архитектура делит приложение на логические слои (layers) и физические уровни (tiers). У каждого слоя своя зона ответственности. Уровни физически разделены и работают на отдельных машинах. N-уровневое приложение может иметь архитектуру с закрытыми слоями или с открытыми слоями. N-уровневые архитектуры обычно реализуются как приложения infrastructure-as-service (IaaS), где каждый уровень работает на отдельном наборе VM
</b></details>

### Хранилище

<details>
<summary>С какими сервисами хранения Azure вы знакомы?</summary><br><b>
</b></details>

<details>
<summary>Какие варианты хранения поддерживает Azure?</summary><br><b>
</b></details>

### Безопасность

<details>
<summary>Что такое Azure Security Center? Каковы некоторые из его возможностей?</summary><br><b>

Это сервис мониторинга, который обеспечивает защиту от угроз для всех сервисов в Azure.
В частности, он:

* Предоставляет рекомендации по безопасности на основе использования
* Отслеживает настройки безопасности и непрерывно — все сервисы
* Анализирует и выявляет потенциальные входящие атаки
* Обнаруживает и блокирует вредоносное ПО с помощью машинного обучения
</b></details>

<details>
<summary>Что такое Azure Active Directory?</summary><br><b>

Azure AD — это облачный сервис идентификации. Его можно использовать как самостоятельный сервис или интегрировать с уже работающим сервисом Active Directory.
</b></details>

<details>
<summary>Что такое Azure Advanced Threat Protection?</summary><br><b>
</b></details>

<details>
<summary>Какие компоненты входят в Azure ATP?</summary><br><b>
</b></details>

<details>
<summary>Где хранятся логи в Azure Monitor?</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое Azure Site Recovery</summary><br><b>
</b></details>

<details>
<summary>Объясните, что делает advisor</summary><br><b>
</b></details>

<details>

<summary>Какие протоколы доступны для настройки health probe</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое Azure Active</summary><br><b>
</b></details>

<details>
<summary>Что такое подписка (subscription)? Какие типы подписок существуют?</summary><br><b>
</b></details>

<details>
<summary>Объясните, что такое сервис blob storage</summary><br><b>
</b></details>

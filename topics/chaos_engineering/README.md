# Chaos Engineering

- [Chaos Engineering](#chaos-engineering)
  - [Вопросы по Chaos Engineering](#вопросы-по-chaos-engineering)
    - [Основы](#основы)

## Вопросы по Chaos Engineering

### Основы

<details>
<summary>Что такое Chaos Engineering?</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Chaos_engineering): «Хаос-инжиниринг (Chaos Engineering) — это дисциплина проведения экспериментов над системой с целью укрепить уверенность в её способности выдерживать нестабильные условия в production.»

[TechTarget](https://www.techtarget.com/searchitoperations/definition/chaos-engineering): «Хаос-инжиниринг — это процесс тестирования распределённой вычислительной системы, чтобы убедиться, что она способна выдерживать неожиданные сбои.»

</b></details>

<details>
<summary>Как выглядит типичный процесс Chaos Engineering?</summary><br><b>

Согласно [Gremlin](gremlin.com), есть три шага:

1. Планирование эксперимента: проектирование и выбор сценария, в котором система должна перестать нормально работать
2. Проведение минимально возможного эксперимента для проверки теории
3. Если ничего не сломалось, эксперимент масштабируется, а радиус поражения (blast radius) увеличивается. Если система ломается, нужно лучше понять причину и начать её устранять

Затем процесс повторяется — с тем же сценарием или с новым.

</b></details>

<details>
<summary>Назовите несколько инструментов для проведения хаос-экспериментов</summary><br><b>

- AWS Fault Injection Simulator: внедрение сбоев в ресурсы AWS
- Azure Chaos Studio: внедрение сбоев в ресурсы Azure
- Chaos Monkey: один из самых известных инструментов для оркестрации хаоса у различных облачных провайдеров
- Litmus - фреймворк для Kubernetes 
- Chaos Mesh: для облачных платформ Kubernetes


Обширный список можно найти [здесь](https://github.com/dastergon/awesome-chaos-engineering)

</b></details>

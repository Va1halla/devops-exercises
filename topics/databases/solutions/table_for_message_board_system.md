## Таблица базы данных для системы доски сообщений

### Инструкции

Спроектировать таблицу базы данных для системы доски сообщений. Она должна включать следующую информацию:

  * Личные данные
  * Кто и когда видел сообщение
  * Ответы
  * Люди, отмеченные в сообщении
  * Категории сообщений

Примечания:

  * SQL не нужен
  * Нужно указать: имена таблиц, имена полей, типы данных, а также используемые внешние ключи.

### Решение

Примечание: это лишь один из возможных вариантов
Примечание 2: PK = первичный ключ (primary key), FK = внешний ключ (Foreign key)

                                ----- People -----
                                ID int PK
                                FirstName varchar(255)
                                LastName varchar(255)
                                DOB date
                                Gender varchar(1)
                                Phone varchar(10)

                                       |               \
                                       |                \ 
                                       |                 \
                                       v                  \ 
                                                           \
                                --- Messages ---            v
                                ID int PK
                                MessageBoardID FK             --- MessageTags ---
--- MessageBoards ---           PeopleID int FK               ID int PK
ID int PK              ---->    MsgDate datetime       --->   MessageID FK
Board text                      Message text                  PeopleID int Fk
                                MessageID (FK)
                                       ^      |
                                       |      |
                                       |______|


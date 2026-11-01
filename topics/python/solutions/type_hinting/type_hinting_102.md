## Аннотации типов 102 — решение

Добавить аннотации типов для каждой из следующих переменных:

1. `abc` — список из двух целых чисел
2. `qwery` — словарь, в котором ключи — строки, а значения — целые числа
3. `elmer` — None, но в какой-то момент может стать строкой
4. `norie` — переменная, содержащая функцию, которая принимает два целочисленных аргумента и возвращает строку

### Решение

1.
```
from typing import List

abc: List[int, int]
```

2.
```
from typing import Dict

abc: Dict[str, int]
```

3. 
```
from typing import Optional

elmer: Optional[str]
```

4.
```
from typing import Callable

norie: Callable[[int, int], str]
```

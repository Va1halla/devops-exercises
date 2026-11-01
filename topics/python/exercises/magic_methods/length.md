## Магический метод длины

1. Почему приведённый ниже код завершается ошибкой при выполнении?
2. Исправить его, чтобы он работал

```
import collections

Mushroom = collections.namedtuple('Mushroom', ['name', 'poisonous'])

class MushroomsBusket:

    def __init__(self):

        self._mushrooms = [Mushroom('Oyster', False), Mushroom('Portobello', False)]

mushroom_basket = MushroomsBusket()
print(len(mushroom_basket))
```

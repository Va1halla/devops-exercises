## Магический метод длины

1. Код завершится ошибкой, потому что класс MushroomsBasked не реализует магический метод __len__

2.

```python
import collections

Mushroom = collections.namedtuple('Mushroom', ['name', 'poisonous'])

class MushroomsBusket:

    def __init__(self):

        self._mushrooms = [Mushroom('Oyster', False), Mushroom('Portobello', False)]

    def __len__(self):
        return len(self._mushrooms)

mushroom_basket = MushroomsBusket()
print(len(mushroom_basket))
```

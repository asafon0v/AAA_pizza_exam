from decorators_pizza import splitter

"""
Основной класс для готовки пиццы
"""

STRIP_CHARS = [' ', '.', ',', '-', '(', ')',
               '!', '"', "'", '#', "@", "$",
               '%', '^', '&', '*', '+', '`']


class BasePizza:
    """
    Фундаментальный класс для готовки пиццы.
    Характерищует каждую пиццу двумя параметрами -
    соусом и размером.
    """

    def __init__(self, base_sauce: str = 'tomato sauce', size: str = 'L'):
        if base_sauce.lower() in ['tomato sauce', 'white', 'white sauce']:
            self.sauce = base_sauce.lower()
        else:
            raise ValueError('Cannot make base pizza with this base sauce!')
        if isinstance(size, int):
            self.size = 'L' if size < 31 else 'XL'
        else:
            self.size = size

    def __eq__(self, other):
        if self.sauce == other.sauce and self.size == other.size:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.sauce + self.size)

    def __iter__(self):
        yield 'sauce', self.sauce
        yield 'size', self.size

    def __repr__(self):
        return f'{self.sauce}, {self.size}'


class Pizza(BasePizza):
    """
    Дополняет готовку пиццы из предыдущего класса
    другими ингредиентами.
    """

    PIZZAS = ['Margherita', 'Pepperoni', 'Hawaiian']
    RECIPES = dict({'Margherita': {'sauce': 'tomato sauce',
                                    'cheese': 'mozzarella',
                                    0: 'tomatoes'},
                    'Pepperoni': {'sauce': 'tomato sauce',
                                  'cheese': 'mozzarella',
                                  0: 'pepperoni'},
                    'Hawaiian': {'sauce': 'tomato sauce',
                                 'cheese': 'mozzarella',
                                 0: 'chicken',
                                 1: 'pineapples'}})

    def __init__(self, pizza: str, size):
        super().__init__(Pizza.RECIPES[pizza]['sauce'], size)
        self.pizza = pizza

    def __iter__(self):
        yield self.pizza, Pizza.RECIPES[self.pizza]

    def __repr__(self):
        return f'{self.pizza}, {self.size}'


if __name__ == '__main__':
    info = splitter('$Hawaiian$, tomato sauce%, 35 ! &', char=',')
    print(info)
    for i, word in enumerate(info):
        info[i] = word.strip(''.join(STRIP_CHARS))
    pizza_name, sauce, size = info[:3]
    try:
        if size not in ['L', 'XL']:
            size = int(size)
    except ValueError:
        raise ValueError('You should use integer size for base pizza'
                         ' but also you can use "L" or "XL" instead')
    finally:
        if sauce not in ['tomato sauce', 'white', 'white sauce']:
            raise ValueError('You should use sauce from ["tomato sauce", "white", "white sauce"]')
        if pizza_name not in ['Pepperoni', 'Margherita', 'Hawaiian']:
            raise ValueError('You should use pizza_name from ["Pepperoni", "Margherita", "Hawaiian"]')

    print(pizza_name + ',', sauce + ',', size)
    pizza = Pizza(pizza_name, size)
    print(dict(pizza))
    print(pizza.__dict__)

from time import sleep
from random import randint
from decorators_pizza import log
import click

from pizza_base import Pizza

"""
CLI - система готовки, доставки и хранения пиццы ресторана
"""


@click.group()
def cli() -> None:
    """CLI ресторана"""
    pass


@log('Baked in {:.2f} s!')
def bake(pizza: str) -> None:
    """
    Готовит пиццу
    """
    if pizza in Pizza.RECIPES:
        print(f'Start baking {pizza}!')
        sleep(randint(4, 6))
        print(f'Pizza {pizza} is ready to delivery!')
    else:
        print(f"Sorry, we don't have recipe of {pizza}!")


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Заказ пиццы с возможной доставкой (доп. опция)
    """
    print(f'Your order is {pizza}! Start baking...')
    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@log('Pizza is delivered in {:.2f} s!'
     'Thank you for the order!')
def deliver(pizza: str) -> None:
    """Доставка приготовленной пиццы заказчику"""
    if pizza in Pizza.RECIPES:
        print(f'{pizza} is coming!')
        sleep(randint(2, 5))


@log('picked up in {}s!')
def pickup(pizza: str) -> None:
    """Забирание пиццы заказчиком"""
    if pizza in Pizza.RECIPES:
        print(f'{pizza} is ready for pick-up!')
        sleep(randint(3, 7))


@cli.command()
def menu() -> None:
    """Показывает меню ресторана -
    набор пицц с ингредиентами"""
    for pizza, ingr in Pizza.RECIPES.items():
        print(f'{pizza}: {", ".join(ingr.values())}')


if __name__ == '__main__':
    cli()

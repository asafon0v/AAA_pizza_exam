from typing import Callable, Iterable, List
from time import time


def log(text: str) -> Callable:
    """
    Дополняет вызов функции временем выполнения кода
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            ret = func(*args, **kwargs)
            end_time = time()
            print(text.format(end_time - start_time))
            return ret

        return wrapper

    return decorator


def splitter(iter: Iterable, char: str = ' ', ) -> List:
    """
    Разбивает итерируемый объект по некоторому
    (заданному) строковому символу
    """
    return [el for el in iter.split(char) if el is not []]


def stripper(iter: Iterable, char: str = ' ', ) -> List:
    """
    Обрезает заданные символы для каждого элемента
    некоторого итерируемого объекта
    """
    return [el.strip(char) for el in iter if el is not []]

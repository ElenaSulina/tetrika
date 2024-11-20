# Необходимо реализовать декоратор @strict 
# Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов, объявленным в прототипе функции. 
# (подсказка: аннотации типов аргументов можно получить из атрибута объекта функции func.__annotations__ или с помощью модуля inspect) 
# При несоответствии типов бросать исключение TypeError 
# Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str 
# Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию
from functools import wraps


def strict(func):

    # @wraps
    def wrapper(*args, **kwargs):

        # Получаем в список все заданные типы параметров, кроме return
        annotation_types = [value for key, value in func.__annotations__.items() if key != "return"]

        # Получаем в список все типы переданных аргументов
        args_types = [type(arg) for arg in args]
        
        # Сравниваем списки, если не совпадают, то бросаем TypeError
        if annotation_types != args_types:
            raise TypeError(f"Переданые в функцию {func.__name__} аргументы имеют неверный тип данных")

        return func(*args, **kwargs)
    
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

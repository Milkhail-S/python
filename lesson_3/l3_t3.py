def my_func(a1, a2, a3):
    """Возвращает сумму 2 оставшихся максимальных элемента

    - создаём лист аргументов
    - убираем из него минимальный
    - вычисляем сумму 2х оставшихся

    """
    lst = [a1, a2, a3]
    lst.remove(min(lst))
    res = sum(lst)
    return res


print(my_func(10, 5, 1))

def my_func(x, y):
#     Через **
#     try:
#         res = x ** y
#     except ZeroDivisionError as err:
#         print(err)
#         return
#     return res
    z = x
    for i in range(1, abs(y)):
        x *= z
    res = 1 / x
    return res
b = my_func(float(input('Введите действительное положительное число: ')), int(input('Введите целое отрицательное число: ')))
print(b)

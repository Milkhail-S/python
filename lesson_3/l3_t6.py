def int_func(sl):
    res = sl.capitalize()
    return res


lst = input('Введите текст строчными буквами, разделяя пробелами: ').split()
print(lst)
for i in range(len(lst)):
    lst[i] = int_func(lst[i])
str = ' '.join(lst)
print(str)

from random import randint


old_lst = [randint(-10, 30) for i in range(30)]
print(old_lst)
new_lst = [old_lst[i] for i in range(1, len(old_lst)) if old_lst[i] > old_lst[i-1]]
print(new_lst)

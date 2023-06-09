from random import randrange as rr

first_iteration = True

def tree_generator() -> list:
    """Генерирует дерево с произвольным количеством веток и листьев. Роль листа играет строка 'leaf'."""
    # КОММЕНТАРИЙ: интересное использование глобальной переменной!
    global first_iteration

    result = []
    for _ in range(rr(1 if first_iteration else 0, 5)):
        first_iteration = False
        if rr(0, 2) == 1:
            result.append('leaf')
        else:
            result.append(tree_generator())
    first_iteration = True
    return result


# >>> tree_generator()
# [['leaf'], 'leaf', 'leaf']
# >>> tree_generator()
# ['leaf', ['leaf', 'leaf', ['leaf', 'leaf']], 'leaf', ['leaf', 'leaf']]
# >>> tree_generator()
# [['leaf'], 'leaf', 'leaf', ['leaf', [], ['leaf', 'leaf', [], 'leaf'], [[], [], 'leaf']]]
# >>>


# ИТОГ: отлично — 5/5

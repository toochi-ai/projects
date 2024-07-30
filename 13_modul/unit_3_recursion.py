def recursive_func(n=0):
    print('Вывод до запуска рекурсии:', n)
    if n < 3:
        recursive_func(n + 1)
    print('Вывод после запуска рекурсии:', n)


recursive_func()
print('---')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(f'факториал: {factorial(5)}')

print('---')


#  Дерево реализовано как вложенные списки. Каждый узел
#  представляет собой список, состоящий из двух
#  элементов — значения узла и списка его детей:
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []


root = Node(5, [
    Node(3, [
        Node(1),
        Node(4)
    ]),
    Node(2, [
        Node(6),
        Node(-1)
    ])
])

# Получение значения в узле-корне
print(f'корень дерева: {root.value}')
# Получение значений дочерних узлов
print(f'дети корня: {root.children[0].value, root.children[1].value}')
# Получение значений листьев
print(f'листья дерева: {root.children[0].children[0].value, root.children[0].children[1].value}')
print(f'листья дерева: {root.children[1].children[0].value, root.children[1].children[1].value}')


#  Применяем рекурсию:
def test_tree_structure(node):
    # у node есть  value — значение
    # и children — список других node

    # Базовый случай
    if node.value < 0:
        return False

    # Рекурсия
    for child in node.children:
        if not test_tree_structure(child):
            return False

    return True


print('---')
#  Итог работы функции: если не было найдено ни одного отрицательного узла,
#  она вернёт True, в противном случае — False:

# Тестируем наше дерево
if test_tree_structure(root) is not True:
    print(f'{test_tree_structure(root)} - в дереве присутствует отрицательный узел')
else:
    print(f'{test_tree_structure(root)} - в дереве отсутствует отрицательный узел')

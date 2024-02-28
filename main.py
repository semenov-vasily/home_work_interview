class Stack:
    def __init__(self):
        self.elems = []

    # Метод проверяет стек (список) на пустоту
    def is_empty(self):
        return self.elems == []

    # Метод добавляет новый элемент на вершину стека (в конец списка)
    def push(self, item):
        self.elems.append(item)

    # Метод удаляет верхний элемент стека (списка). Стек изменяется.
    # Метод возвращает верхний элемент стека (последний элемент списка)
    def pop(self):
        if self.is_empty:
            return self.elems.pop()

    # Метод возвращает верхний элемент стека (последний элемент списка),
    # но не удаляет его. Стек (список) не меняется
    def peek(self):
        if self.is_empty:
            return self.elems[-1]

    # Метод возвращает количество элементов в стеке (строке)
    def size(self, brackets):
        return len(brackets)


# Функция, проверяющая строку из скобок на сбалансированность
def balanc(brackets: str) -> str:
    # Создаем экземпляр класса Stack()
    stack = Stack()
    # Проверяем, что кол-во элементов строки четное
    if stack.size(brackets) % 2 != 0:
        return 'Несбалансированно'
    # Проверяем, что строка не пустая
    if len(brackets) == 0:
        return 'Пустая строка'
    # Берем каждый элемент строки
    for elem in brackets:
        # Если открывающая скобка
        if elem in ['(', '{', '[']:
            # Добавляем в конец списка self.elems
            stack.push(elem)
        # Если закрывающая скобка
        elif elem in [')', '}', ']']:
            # Если список self.elems пустой
            if stack.is_empty():
                return 'Несбалансированно'
            # Берем последний элемент списка self.elems
            last_stack = stack.peek()
            # Если последний элемент списка self.elems - открывающая скобка
            # и ей не соответствует нужная закрывающая скобка
            if ((last_stack == '(' and elem != ')')
                    or (last_stack == '[' and elem != ']')
                    or (last_stack == '{' and elem != '}')):
                return 'Несбалансированно'
            # Удаляем последний элемент списка self.elems
            stack.pop()
    # Если перебрали весь список self.elems и в завершении он пустой
    # (все открывающие скобки соответствуют закрывающим)
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == "__main__":
    print(balanc('[([])((([[[]]])))]{()}'))
    print(balanc('[[{())}]'))
    print(balanc(''))

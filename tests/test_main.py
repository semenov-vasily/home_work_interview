import pytest

from main import balanc


class Tests_pytest:
    # Задаем параметры для тестирующей функции test_balanc
    @pytest.mark.parametrize('brackets, result', [
        ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
        ('[[{())}]', 'Несбалансированно')
    ])
    # Тест функции проверяющей стек (строку) на сбалансированность
    def test_balanc(self, brackets: str, result: str):
        # Проверяем, что функция balanc вернула правильный вариант ответа
        assert balanc(brackets) == result

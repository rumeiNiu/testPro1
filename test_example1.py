import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


class TestDemo:
    def test_a(self):
        print('a')

    def test_b(self):
        print('b')


if __name__ == '__main__':
    pytest.main(['test_example1.py', '-vs'])

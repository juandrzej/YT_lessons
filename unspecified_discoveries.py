from warnings import deprecated
from functools import lru_cache


# function to test 'deprecated' in action
@deprecated('Use "new_func()" instead!')
def old_func() -> None:
    print('old_func() called!')


def new_func() -> None:
    print('new_func() called!')


# function to test OR implementation alongside empty strings
def input_or_na() -> None:
    user_input = input('Name: ')
    name = user_input or 'N/A'
    print(name)

def test_disjoint() -> None:
    a: set[int] = {1, 2, 3, 4}
    b: set[int] = {5, 6, 7}
    print(a.isdisjoint(b))

@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def test_fib() -> None:
    for i in range(0, 40):
        print(f"{i}: {fib(i)}")
        i += 1


def main() -> None:
    # old_func()
    # new_func()
    # input_or_na()
    # test_disjoint()
    test_fib()
    # pass


if __name__ == '__main__':
    main()
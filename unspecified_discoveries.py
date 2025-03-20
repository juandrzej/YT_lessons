from warnings import deprecated


@deprecated('Use "new_func()" instead!')
def old_func() -> None:
    print('old_func() called!')


def new_func() -> None:
    print('new_func() called!')


def main() -> None:
    old_func()
    new_func()

if __name__ == '__main__':
    main()
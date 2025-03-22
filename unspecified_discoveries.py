from warnings import deprecated


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


def main() -> None:
    # old_func()
    # new_func()
    # input_or_na()
    pass


if __name__ == '__main__':
    main()
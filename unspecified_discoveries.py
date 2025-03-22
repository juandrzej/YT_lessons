from warnings import deprecated


@deprecated('Use "new_func()" instead!')
def old_func() -> None:
    print('old_func() called!')


def new_func() -> None:
    print('new_func() called!')


def input_or_na() -> None:
    user_input = input('Name: ')
    name = user_input or 'N/A'
    print(name)


def mask_str(
    current_str: str,
    mask_character: str = "*",
    start: int = 2,
    end: int = 2
) -> str:
    
    a = current_str[:start]
    b = mask_character * len(current_str[start:end])
    c = current_str[end:]

    return a + b + c
    
    
def masking_str() -> None:
    current_str = "1234567890"
    print(f"{current_str=}")

    masked_str = mask_str(
        current_str, "*", 0, -2
    )
    print(f"{masked_str=}")

def main() -> None:
    # old_func()
    # new_func()
    # input_or_na()
    masking_str()

if __name__ == '__main__':
    main()
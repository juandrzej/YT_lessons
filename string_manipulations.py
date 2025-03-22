def mask_str(
    current_str: str,
    mask_character: str = "*",
    start: int = 2,
    end: int = 2
) -> str:
    """Function to mask part of string, e.g. for tax ID"""
    
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

# function to show nice presenttion of %
def show_pct() -> None:
    percent: float = .032758
    print(f"{percent:,.2%}")
    

def fill_str() -> None:
    current_str: str = "Hello"
    print(f"{current_str:~^10}")

def main() -> None:
    # masking_str()
    # show_pct()
    fill_str()

if __name__ == '__main__':
    main()
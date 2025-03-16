from itertools import count, cycle , repeat

def test_count() -> None:
    count1: count = count()
    count2: count = count(5, 2)
    count3: count = count(2, -1)
    count4: count = count(0.0, 0.5)

    for _ in range(10):
        print((next(count1), next(count2), next(count3), next(count4)))

def test_cycle() -> None:
    people: list[str] = ['Tom', 'Bob', 'Alice']
    my_cycle: cycle = cycle(people)
    
    for _ in range(5):
        print(next(my_cycle))

def main() -> None:
    test_count()
    test_cycle()

if __name__ == '__main__':
    main()
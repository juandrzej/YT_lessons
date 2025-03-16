from itertools import count, cycle , repeat

def test_count() -> None:
    count1: count = count()
    count2: count = count(5, 2)
    count3: count = count(2, -1)
    count4: count = count(0.0, 0.5)

    for _ in range(10):
        print((next(count1), next(count2), next(count3), next(count4)))

def main() -> None:
    test_count()

if __name__ == '__main__':
    main()
from itertools import count, cycle , repeat
import timeit

def test_count_iterator() -> None:
    count1: count = count()
    count2: count = count(5, 2)
    count3: count = count(2, -1)
    count4: count = count(0.0, 0.5)

    for _ in range(10):
        print((next(count1), next(count2), next(count3), next(count4)))

def test_cycle_iterator() -> None:
    people: list[str] = ['Tom', 'Bob', 'Alice']
    my_cycle: cycle = cycle(people)
    
    for _ in range(5):
        print(next(my_cycle))

def test_repeat_iterator() -> None:
    my_repeat: repeat = repeat('Hello', 3)
    for _ in range(3):
        print(next(my_repeat))
    # print(next(my_repeat))
    
    
def test_while() -> None:
    counter: int = 0
    while counter < 1_000_000:
        counter += 1
            
def test_for() -> None:
    for _ in range(1_000_000):
        pass
        
def test_repeat() -> None:                
    for _ in repeat(None, 1_000_000):
        pass
            
    
def test_repeat_with_time() -> None:
    """
    Compare performance of different loop implementations.
    Using timeit with externally defined functions for more accurate results.
    """
    while_time: float = timeit.timeit(test_while, number=100)
    for_time: float = timeit.timeit(test_for, number=100)
    repeat_time: float = timeit.timeit(test_repeat, number=100)    
    
    print(f'While loop time: {while_time:.3f}')
    print(f'For loop time: {for_time:.3f}')
    print(f'Repeat loop time: {repeat_time:.3f}') 
    
def main() -> None:
    # test_count_iterator()
    # test_cycle_iterator()
    # test_repeat_iterator()
    test_repeat_with_time()

if __name__ == '__main__':
    main()
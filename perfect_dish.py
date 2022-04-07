from typing import Generator


def perfect_dish() -> Generator:
    """
    "Perfect dish for share" - a dish that if we sum up all the possibilities to divide it,
     we will reach the size of the dish itself.
    @:return: All the options available for perfect dishes.
    """
    i = 1
    while True:
        total = 0
        for j in range(1, i+1):
            if j != i:
                if i % j == 0:
                    total += j
        i += 1
        if total == i - 1:
            yield total


if __name__ == '__main__':
    gen = perfect_dish()
    while True:
        print(next(gen))

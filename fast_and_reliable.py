# C:\Users\IMOE001\Downloads\words.txt
import re
from time import process_time
import typing


def fast_and_reliable(path: str) -> None:
    """
    A function that checks how long on average a word search in a list and group lasts.
    :param path: Path of file "words.txt"
    """
    with open(path, 'r') as f:
        words_list = f.read()
    words_list = re.findall(r'\w+', words_list)
    words_set = set(words_list)
    list_time = average_runtime(words_list)
    set_time = average_runtime(words_set)
    print("The search in the list took: " + str(list_time))
    print("The search in the set took: " + str(set_time))


def average_runtime(words: typing.Iterable) -> float:
    """
    The function returns the average time the search takes in a data structure.
    :param words: List or set of words.
    :return: The average time.
    """
    t_start = process_time()
    for i in range(1000):
        if 'zwitterion' in words:
            break
    t_stop = process_time()
    return t_stop - t_start


if __name__ == '__main__':
    fast_and_reliable("C:/Users/IMOE001/Downloads/words.txt")

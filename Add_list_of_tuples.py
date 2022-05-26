from pickle import APPEND
from readline import append_history_file


def add_tuple_lists(list_a, list_b):
    list_f = []
    for i in range(len(list_a)):
        res = []
        for (x,y) in zip(list_a[i], list_b[i]):
            res.append(x+y)
        list_f.append(tuple(res))
    return list_f

    """ Add together two lists of tuples of integers.

    Keyword arguments:
    list_a -- a list of tuples of integers, all of which have the same length
    list_b -- another list of tuples of integers, which have the same length as list_a

    Returns:
    a single list of tuples, each one being the sum of the equivalent tuples in list a and list b
    """

    # Oh dear, there's nothing here!

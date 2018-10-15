def reverse_list_in_place(lst):
    """Write a function that takes a list of characters and reverses the list in place.

    >>> reverse_list_in_place(['c', 'a', 't'])
    ['t', 'a', 'c']

    >>> reverse_list_in_place(['r', 'a', 'c', 'e', 'c', 'a', 'r'])
    ['r', 'a', 'c', 'e', 'c', 'a', 'r']

    >>> reverse_list_in_place(['h', 'i'])
    ['i', 'h']

    >>> reverse_list_in_place(['z'])
    ['z']

    >>> reverse_list_in_place([])
    []

    """

    # OPTION 1: reverse() method, returns an iterator in place
    # lst.reverse()

    # return lst


    # OPTION 2: reversed() function, returns an iterable in place
    # reversed_lst = []

    # for x in reversed(lst):
    #     reversed_lst.append(x)

    # return reversed_lst


    # OPTION 3: reversed() function, listified

    # return list(reversed(lst))


    # OPTION 4: list slicing, [start:stop:step]

    # return lst[::-1]
    

    # OPTION 5: reverse without using built-in methods or functions

    left_idx = 0
    right_idx = len(lst)-1

    while left_idx < right_idx:
        lst[left_idx], lst[right_idx] = lst[right_idx], lst[left_idx]
        left_idx += 1 
        right_idx += 1

    return lst





if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
    
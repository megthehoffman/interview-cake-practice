def reverse_list_in_place(lst):
    """Write a function that takes a list of characters and reverses the list in place.

    >>> reverse_list_in_place(['c','a','t'])
    ['t','a','c']

    >>> reverse_list_in_place(['r','a','c','e','c','a','r'])
    ['r','a','c','e','c','a','r']

    >>> reverse_list_in_place(['h','i'])
    ['i','h']

    >>> reverse_list_in_place(['z'])
    ['z']

    >>> reverse_list_in_place([])
    []
    
    """

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
    
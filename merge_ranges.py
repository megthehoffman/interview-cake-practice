def merge_ranges(meetings):
    """Write a function that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
       Ranges are written in terms of 30-min blocks after 9am, but the function should be able to handle no upper bounds.
       EX: UNIX timestamps

    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    """


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
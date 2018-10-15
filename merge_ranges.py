def merge_ranges(meetings):
    """Write a function that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
       Ranges are written in terms of 30-min blocks after 9am, but the function should be able to handle no upper bounds.
       EX: UNIX timestamps

    Meeting times out of order
    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    Duplicate meeting times
    >>> merge_ranges([(0, 1), (0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    Subsumed meeting times
    >>> merge_ranges([(1, 5), (2, 3)])
    [(1, 5)]

    Connected meeting times
    >>> merge_ranges([(1, 2), (2, 3)])
    [(1, 3)]

    Result of merge may need to be merged with next
    >>> merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)])
    [(1, 10)]

    One meeting time
    >>> merge_ranges([(0, 1)])
    [(0, 1)]

    No meeting times
    >>> merge_ranges([])
    []

    """
    sorted_meetings = sorted(meetings, key = lambda x: x[0])
    # print(sorted_meetings)

    if len(sorted_meetings) <= 1:
        return sorted_meetings

    i = 0
    j = 1

    current_tuple = sorted_meetings[i]
    next_tuple = sorted_meetings[j]

    condensed_meetings = []

    while j < len(sorted_meetings):
        if current_tuple == next_tuple:
            if current_tuple not in condensed_meetings:
                condensed_meetings.append(current_tuple)
            i += 2
            j += 2
        elif next_tuple[0] <= current_tuple[1] and next_tuple[1] <= current_tuple[1]:
            if current_tuple not in condensed_meetings:
                condensed_meetings.append(current_tuple)
            j += 1
        elif next_tuple[0] <= current_tuple[1]:
            condensed_range = (current_tuple[0], next_tuple[1])
            condensed_meetings.append(condensed_range)
            i += 2
            j += 2
        else:
            condensed_meetings.append(current_tuple)
            i += 1
            j += 1

        if j < len(meetings):
            current_tuple = sorted_meetings[i]
            next_tuple = sorted_meetings[j]
        

    return condensed_meetings


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
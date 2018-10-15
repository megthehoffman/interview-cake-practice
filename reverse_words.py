def reverse_words(message):
    """Takes a message as a list of characters and reverses the order of the words in place.
       Assume the message contains only letters and spaces, and all words are separated by one space.

    >>> reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ])
    'steal pound cake'

    >>> reverse_words([ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ])
    'landed has eagle the'
    """

    return str(' '.join(''.join(message).split(' ')[::-1]))
        

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
def string_pattern(size: int) -> str:
    """Creates an 'X' pattern using + and - of size `size`.

    The pattern created is a square with side length `size`.

    Args:
      size: the size of the pattern

    Returns:
      A string containing the pattern.

    Raises:
      ValueError: If `size` is less than or equal to 2.
    """
    if size <= 2:
        raise ValueError("Expected `size` to be greater than or equal to 2.")

    buf = [["-" for _ in range(size)] for _ in range(size)]
    i, j = 0, size - 1
    for row in buf:
        row[i] = "+"
        row[j] = "+"
        
        # i, j will never be out of bounds since we are iterating over
        # the rows of a square
        i += 1
        j -= 1

    return "\n".join(map(lambda r: "".join(r), buf)) + "\n"

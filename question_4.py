def longest_palindromic_numbers(number: str) -> set[str]:
    """Find the longest palindromic numbers in `number`.

    A palindromic number is a number which is the same when the order of
    its digits is reversed. For example, consider the number 121.
    
    Args:
     number: The number in which the longest palindromic numbers are
     searched.

    Returns:
      The set of longest palindromic numbers in `number`.
    """
    nums = set()

    # auxilary function to recurse with
    def aux(number):
        if not number:
            return
        if is_palindrome(number):
            nums.add(number)
        aux(number[:-1])
        aux(number[1:])

    # strip leading 0s before processing
    aux(number.lstrip("0"))
    
    # digits like '000' might be recognised as a palindrome
    nums = set(map(lambda n: n.lstrip("0"), nums))

    # keep only the longest palindromes
    max_len = max(map(len, nums))
    for elem in nums.copy():
        if len(elem) < max_len:
            nums.remove(elem)
    return nums


def is_palindrome(number: str) -> bool:
    """Return a boolean indicating if a number is a palindrome."""
    # a bit lazy but it works
    return number == number[::-1]

def shrink(signal: list[int], element: list[int]) -> list[int]:
    """Shrink a one dimensional binary signal using `element`
    
    The "shrinking" operation shrinks the boundaries of the foreground
    regions. The structuring element is moved over the input signal. If
    all elements of the structuring element overlap with the signal’s
    1s, the corresponding position in the output is set to 1; otherwise,
    it is set to 0.

    Args:
     signal: The binary signal to shrink. 
     element: The structural element used to shrink the input.

    Returns:
      The signal after shrinking with the specified structural element.
    """
    step = len(element)
    shrunk = []
    for idx in range(len(signal)):
        if idx + step > len(signal):
            end = idx + step - len(signal)
            if signal[idx:] == element[:-end]:
                shrunk.append(1)
            else:
                shrunk.append(0)
        elif signal[idx:idx + step] == element:
            shrunk.append(1)
        else:
            shrunk.append(0)
    return shrunk


def expand(signal: list[int], element: list[int]) -> list[int]:
    """Expand a one dimensional binary signal using `element`
    
    The "shrinking" operation shrinks the boundaries of the foreground
    regions. The structuring element is moved over the input signal. If
    any elements of the structuring element overlap with the signal’s
    1s, the corresponding position in the output is set to 1; otherwise,
    it is set to 0.

    Args:
     signal: The binary signal to expand.
     element: The structural element used to expand the input.

    Returns:
      The input after expanding with the specified structural element.
    """
    step = len(element)
    expanded = []
    for idx in range(len(signal)):
        if idx + step > len(signal):
            end = idx + step - len(signal)
            if any(a == b for a, b in zip(signal[idx:], element[:-end])):
                expanded.append(1)
            else:
                expanded.append(0)
        elif any(a == b for a, b in zip(signal[idx:idx + step], element)):
            expanded.append(1)
        else:
            expanded.append(0)
    return expanded


def denoise(signal: list[int], element: list[int]) -> list[int]:
    """Denoise a one dimensional binary signal using `element`
    
    Denoising is done by first shrinking and then expandnding the input
    signal.

    Args:
     signal: The binary signal to denoise.
     element: The structural element used to denoise the input.

    Returns:
      The signal after denoising with the specified structural element.
    """
    return expand(shrink(signal, element), element)

def is_even(x):
    number_types = (int, float)
    if isinstance(x, number_types):
        return x % 2 == 0
    else:
        raise ValueError

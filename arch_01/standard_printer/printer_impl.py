"""
Standard printer implementation.
"""


def printer(*args, **kwargs):
    """
    printer implementation, in case we will want somehow to redefine that behaviour
    """
    print(*args, **kwargs)

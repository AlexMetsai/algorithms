"""
Overall aim is to keep syntax as simple as possible, the focus being the algorithms themselves,
thus resisting the temptation to wrap up everything under a class.
"""


def parent(i: int):
    return int(i / 2)


def left(i: int):
    return int(2 * i)


def right(i: int):
    return int(2 * i + 1)

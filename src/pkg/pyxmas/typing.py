from collections.abc import Callable
from typing import TypeAlias, NewType

# In python >=3.12, you can just write type Vector
Vector: TypeAlias = list[float]

# Create a subtype of int (with almost zero overhead)
UserId = NewType("UserId", int)


def get_user_name(user_id: UserId) -> str:
    return str(user_id)


if __name__ == "__main__":
    get_user_name(UserId(123))
    # fails type checking
    # get_user_name(-1)

#!/usr/bin/env python3
"""
python3 -c
'print(__import__("102-type_checking").__doc__)'
Use mypy to validate the following piece of code and apply any necessary changes.

Author: Oluwaseun Ayela 
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Trying this docstring for this module
     python3 -c
     'print(__import__("102-type_checking").zoom_array.__doc__)'

    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(__import__("102-type_checking").zoom_array.__doc__)
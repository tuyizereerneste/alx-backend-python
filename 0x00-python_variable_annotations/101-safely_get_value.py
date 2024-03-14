#!/usr/bin/env python3


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Parameters:
        dct (Mapping): The dictionary to search for the key.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional)
    Return:
        Union[Any, T]: The value corresponding to the key,
        or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default

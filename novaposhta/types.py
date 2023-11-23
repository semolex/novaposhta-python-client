"""Type aliases for novaposhta package."""

from typing import List, Optional, Dict, Union, Any, Coroutine

OptStr = Optional[str]
StrOrNum = Union[str, float, int]
DictStrAny = Dict[str, Any]
MaybeAsync = Union[DictStrAny, Coroutine[Any, Any, Any]]
OptStrOrNum = Optional[StrOrNum]
OptDict = Optional[Dict[str, str]]
OptListOfDicts = Optional[List[Dict[str, Any]]]
OptInt = Optional[int]
OptBool = Optional[
    Union[bool, int]
]  # assume that support for cases: 0 is False, 1 is True

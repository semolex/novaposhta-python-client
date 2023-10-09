"""Type aliases for novaposhta package."""

from typing import List, Optional, Dict, Union, Any

OptStr = Optional[str]
StrOrNum = Union[str, float, int]
OptStrOrNum = Optional[StrOrNum]
OptDict = Optional[Dict[str, str]]
OptDictList = Optional[List[Dict[str, Any]]]
OptInt = Optional[int]
OptBool = Optional[
    Union[bool, int]
]  # assume that support for cases: 0 is False, 1 is True

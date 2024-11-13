"""Type aliases for novaposhta package."""

from typing import Any, Callable, Coroutine, Dict, List, Optional, TypedDict, Union


class RequestData(TypedDict):
    """
    Request data for Nova Poshta API.
    """
    apiKey: str
    modelName: str
    calledMethod: str
    methodProperties: Dict[str, Any]


class HttpRequest(TypedDict):
    """
    Request data for HTTP client.
    """
    url: str
    headers: Dict[str, str]
    json: RequestData
    timeout: int


OptStr = Optional[str]
StrOrNum = Union[str, float, int]
DictStrAny = Dict[str, Any]
MaybeAsync = Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]
SyncSender = Callable[[HttpRequest], Dict[str, Any]]
AsyncSender = Callable[[HttpRequest], Coroutine[Any, Any, Dict[str, Any]]]
RequestSender = Union[SyncSender, AsyncSender]
OptStrOrNum = Optional[StrOrNum]
OptDict = Optional[Dict[str, str]]
OptListOfDicts = Optional[List[Dict[str, Any]]]
OptInt = Optional[int]
OptBool = Optional[
    Union[bool, int]
]  # assume that support for cases: 0 is False, 1 is True

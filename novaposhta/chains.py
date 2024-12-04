"""Chain of calls with error handling and data passing between calls. """

import asyncio
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

T = TypeVar("T")


@dataclass
class ChainResult:
    """
    Result of a single chain execution.
    """

    success: bool
    data: Optional[Any]
    error: Optional[str]
    next_kwargs: Optional[Dict[str, Any]] = None


@dataclass
class Chain:
    """
    Chain object that represents a single call in the chain.
    """

    method: Callable
    kwargs: Optional[Dict[str, Any]] = None
    prepare_next: Optional[Callable[[Any], Dict[str, Any]]] = None

    async def execute(self, prev_result: Optional[ChainResult] = None) -> ChainResult:
        """
        Execute the chain.

        :param prev_result: result of the previous chain.
        :return: result of the current chain.
        """
        try:
            execution_kwargs = {**(self.kwargs or {})}
            if prev_result and prev_result.next_kwargs:
                execution_kwargs.update(prev_result.next_kwargs)

            result = self.method(**execution_kwargs)
            if asyncio.iscoroutine(result):
                result = await result

            next_kwargs = self.prepare_next(result) if self.prepare_next else {}

            return ChainResult(
                success=result.get("success", False),
                data=result.get("data"),
                error=None,
                next_kwargs=next_kwargs,
            )
        except Exception as e:
            return ChainResult(success=False, data=None, error=str(e), next_kwargs=None)

    def __or__(self, other: "Chain") -> "ChainExecutor":
        """
        Create a chain executor with the current chain and another chain.
        Allows chaining multiple chains together via the `|` operator.

        :param other: another chain.
        :return ChainExecutor: chain executor with the current chain and another chain.
        """
        return ChainExecutor([self, other])


class ChainExecutor:
    """
    Chain executor that executes multiple chains in a sequence.
    """

    def __init__(self, chains: Optional[List[Chain]] = None):
        self.chains = chains or []

    def __or__(self, chain: Chain) -> "ChainExecutor":
        """
        Add a chain to the chain executor.

        :param chain: chain to add.
        :return ChainExecutor: chain executor with the added chain.
        """
        self.chains.append(chain)
        return self

    async def execute_async(self) -> List[ChainResult]:
        """
        Execute all chains in the chain executor asynchronously.

        :return: list of results of each chain execution
        """
        results = []
        prev_result = None

        for chain in self.chains:
            result = await chain.execute(prev_result)
            results.append(result)
            if not result.success:
                break
            prev_result = result

        return results

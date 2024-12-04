import pytest
from unittest.mock import AsyncMock, Mock
from novaposhta.chains import Chain, ChainResult, ChainExecutor


@pytest.fixture
def mock_method():
    return AsyncMock(return_value={"success": True, "data": [{"Ref": "test-ref"}]})


@pytest.fixture
def mock_prepare_next():
    return Mock(return_value={"extracted_ref": "test-ref"})


@pytest.mark.asyncio
async def test_chain_single_execution(mock_method, mock_prepare_next):
    chain = Chain(method=mock_method, kwargs={"test": "value"}, prepare_next=mock_prepare_next)
    result = await chain.execute()

    mock_method.assert_called_once_with(test="value")
    mock_prepare_next.assert_called_once_with({"success": True, "data": [{"Ref": "test-ref"}]})
    assert isinstance(result, ChainResult)
    assert result.success
    assert result.data == [{"Ref": "test-ref"}]
    assert result.next_kwargs == {"extracted_ref": "test-ref"}


@pytest.mark.asyncio
async def test_chain_with_prev_result(mock_method):
    prev_result = ChainResult(
        success=True,
        data={"some": "data"},
        error=None,
        next_kwargs={"prev_param": "value"}
    )
    chain = Chain(method=mock_method)
    await chain.execute(prev_result)

    mock_method.assert_called_once_with(prev_param="value")


@pytest.mark.asyncio
async def test_chain_executor(mock_method, mock_prepare_next):
    chain1 = Chain(method=mock_method, prepare_next=mock_prepare_next)
    chain2 = Chain(method=mock_method)

    executor = chain1 | chain2
    results = await executor.execute_async()

    assert len(results) == 2
    assert all(isinstance(r, ChainResult) for r in results)
    assert mock_method.call_count == 2
    assert mock_prepare_next.call_count == 1


@pytest.mark.asyncio
async def test_chain_kwargs_merge():
    method = AsyncMock(return_value={"success": True, "data": "test"})
    chain = Chain(
        method=method,
        kwargs={"base": "value"},
    )
    prev_result = ChainResult(
        success=True,
        data="prev_data",
        error=None,
        next_kwargs={"additional": "value"}
    )
    await chain.execute(prev_result)

    method.assert_called_once_with(base="value", additional="value")


@pytest.mark.asyncio
async def test_search_chain(mock_address_api):
    chain = (
            Chain(
                mock_address_api.search_settlements,
                kwargs={'city_name': 'Київ'},
                prepare_next=lambda x: {'settlement_ref': x['data'][0]['Ref']}
            ) |
            Chain(
                mock_address_api.search_settlement_streets,
                prepare_next=lambda x: {'street_ref': x['data'][0]['Ref']}
            )
    )

    results = await chain.execute_async()
    assert len(results) == 2
    assert all(isinstance(r, ChainResult) for r in results)
    assert results[0].next_kwargs == {'settlement_ref': 'settlement-ref'}
    assert results[1].next_kwargs == {'street_ref': 'street-ref'}


@pytest.mark.asyncio
async def test_chain_preserves_original_data(mock_method, mock_prepare_next):
    chain = Chain(method=mock_method, prepare_next=mock_prepare_next)
    result = await chain.execute()

    assert result.data == [{"Ref": "test-ref"}]  # Original
    assert result.next_kwargs == {"extracted_ref": "test-ref"}  # Transformed


@pytest.mark.asyncio
async def test_chain_execution_error(mock_method, mock_prepare_next):
    mock_method.side_effect = Exception("Test error")
    chain = Chain(method=mock_method, prepare_next=mock_prepare_next)
    result = await chain.execute()

    assert not result.success
    assert result.data is None
    assert result.error == "Test error"
    assert result.next_kwargs is None


def test_chain_executor_combination(mock_method, mock_prepare_next):
    chain = Chain(method=mock_method, prepare_next=mock_prepare_next)
    executor = ChainExecutor([chain])
    assert executor.chains == [chain]

    chain2 = Chain(method=mock_method)
    executor | chain2

    assert executor.chains == [chain, chain2]


@pytest.mark.asyncio
async def test_chain_executor_stops_on_no_success(mock_method, mock_prepare_next):
    chain = Chain(method=mock_method, prepare_next=mock_prepare_next)
    failed_chain = Chain(method=mock_method, prepare_next=mock_prepare_next)
    failed_chain.execute = AsyncMock(return_value=ChainResult(success=False, data=None, error=None, next_kwargs=None))
    never_called_chain = Chain(method=mock_method, prepare_next=mock_prepare_next)
    result = await ChainExecutor([chain, failed_chain, never_called_chain]).execute_async()
    assert len(result) == 2


@pytest.fixture
def mock_address_api():
    api = Mock()
    api.search_settlements = AsyncMock(return_value={
        "success": True,
        "data": [{"Ref": "settlement-ref"}]
    })
    api.search_settlement_streets = AsyncMock(return_value={
        "success": True,
        "data": [{"Ref": "street-ref"}]
    })
    return api



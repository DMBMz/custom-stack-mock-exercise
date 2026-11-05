import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_six_random_numbers_ascending(mocker):
    mock_stack = mocker.MagicMock(spec=CustomStack)
    mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
    mock_stack.pop.side_effect = [53, 10, 4, 32, 27, 1]

    sorter = NumberAscOrder()
    result = sorter.sort(mock_stack)

    assert len(result) == 6
    assert result == [1, 4, 10, 27, 32, 53]
    assert mock_stack.pop.call_count == 6
    assert mock_stack.is_empty.call_count == 7


def test_sort_empty_stack_returns_empty_list(mocker):
    mock_stack = mocker.MagicMock(spec=CustomStack)
    mock_stack.is_empty.return_value = True

    sorter = NumberAscOrder()
    result = sorter.sort(mock_stack)

    assert result == []
    mock_stack.is_empty.assert_called_once()
    mock_stack.pop.assert_not_called()


def test_sort_with_none_or_invalid_stack_raises_type_error():
    sorter = NumberAscOrder()

    with pytest.raises(TypeError):
        sorter.sort(None)

    with pytest.raises(TypeError):
        sorter.sort("invalid_stack")

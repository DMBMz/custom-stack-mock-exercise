import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_one_elementinstack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() is False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_new_stack_is_empty():
    cut = CustomStack(3)
    assert cut.is_empty() is True
    assert cut.size() == 0


def test_push_until_limit_and_raise_stack_full_exception():
    cut = CustomStack(2)
    cut.push(10)
    cut.push(20)
    assert cut.size() == 2
    assert cut.top() == 20
    assert cut.is_empty() is False

    with pytest.raises(StackFullException):
        cut.push(30)

    assert cut.size() == 2
    assert cut.top() == 20


def test_pop_returns_last_pushed_element_and_reduces_size():
    cut = CustomStack(3)
    cut.push(100)
    cut.push(200)
    assert cut.size() == 2

    popped_value = cut.pop()
    assert popped_value == 200
    assert cut.size() == 1
    assert cut.top() == 100
    assert cut.is_empty() is False

    second_popped = cut.pop()
    assert second_popped == 100
    assert cut.size() == 0
    assert cut.is_empty() is True


def test_pop_on_empty_stack_raises_stack_empty_exception():
    cut = CustomStack(5)
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_on_empty_stack_raises_stack_empty_exception():
    cut = CustomStack(5)
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.top()

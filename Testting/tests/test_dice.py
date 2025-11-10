import pytest
from unittest import mock
from func.dice import get_result

# def add(a, b):
#     return a + b

# mock_object = mock.Mock(name="my mock" , a=1, b=2, return_value=15)
# # mock_object.side_effect = add   # adding function to mock to fake

# print(mock_object(5, 10))
# # print(mock_object())
# mock_object.assert_called_once_with(5, 10)   # code breaks if not called with parameters
# mock_object.assert_called_once()             # code breaks is called less or more than once


@pytest.mark.parametrize(
        "input, output",
        [
            (2, "You win"),
            (3, "You lose")
        ],
        ids=['win case', 'lose case']
)
@mock.patch('func.dice.roll_dice')
def test_get_result(mock_roll_dice, input, output):
    value = 2
    mock_roll_dice.return_value = value

    assert get_result(input) == output  
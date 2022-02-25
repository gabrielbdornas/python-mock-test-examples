# Not need third party libraries instalation
from unittest import mock
import pytest
from main import guess_number

@pytest.mark.parametrize(
                          "input,expect",
                          [(1, "You lost!")],
                          [(2, "You lost!")],
                          [(3, "You lost!")],
                          [(4, "You lost!")],
                          [(5, "You lost!")],
                          [(6, "You lost!")],
                          )
@mock.patch("main.roll_dice") # "dice.roll_dice" will call the real function and the test will fail
def test_gues_number(mock_roll_dice, _input, expect):
  mock_roll_dice.return_value=3
  assert guess_number(_input) == expect

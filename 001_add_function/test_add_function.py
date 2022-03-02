from add import add
import pytest

@pytest.mark.parametrize(
                          "first_number, second_number, expect",
                          [
                           (1, 2, 3),
                           (5, 5, 10),
                           (3, 2, 5),
                           (1000, 1, 1001),
                           (100, 33, 133),
                           (9, 2, 11),
                           (6, 2, 8),
                           ('a', 'b', 'ab'),
                          ])
def test_add_function(first_number, second_number, expect):
  assert add(first_number, second_number) == expect

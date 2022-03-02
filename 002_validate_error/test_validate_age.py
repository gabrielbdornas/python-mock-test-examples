import pytest
from validate_age import validate_age

def test_validate_age():
  with pytest.raises(ValueError) as exc_info:
    validate_age(-1)
  assert str(exc_info.value) == "Age can not be less than 0"

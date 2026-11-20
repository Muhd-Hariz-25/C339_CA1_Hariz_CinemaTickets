from src.cinema_entry import can_watch
import pytest

# Use parametrize to check for all valid inputs, based on condition met (>= 16)
@pytest.mark.parametrize(
    "age, expected",
    [
        (16, True), # Will be fail, as condition set is > 16 (line 9)
        (25, True),
        (15, False),
        (0, False),
    ],
)
# Call it and test, this is test for pass
def test_can_watch_with_valid_inputs_returns_bool(age, expected):
    # Act
    result = can_watch(age)

    # Assert
    assert result is expected

# Negative integer is still an INT type, test by itself, test for failure
def test_can_watch_with_negative_integer_raises_value_error():
    # Arrange
    age = -16

    # Act and Assert
    with pytest.raises(ValueError):
        can_watch(age)

# Use this to test for all invalid inputs stated in TP and TCS
@pytest.mark.parametrize(
    "age",
    [
        20.1,
        "twenty",
        "20",
    ],
)
# Call and run, this is a test for failure (See if it handles non INT type)
def test_can_watch_with_invalid_types_raises_type_error(age):
    # Act and Assert
    with pytest.raises(TypeError):
        can_watch(age)
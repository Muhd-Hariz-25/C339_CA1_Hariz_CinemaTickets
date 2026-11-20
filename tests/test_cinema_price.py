from src.cinema_price import ticket_price
import pytest

# Use parametrize to test all for pass
@pytest.mark.parametrize(
    "ticket_count, expected",
    [
        (1, 1200),
        (5, 6000),
        (0, 0), # Based on given code, this will be failed (as always return 1200, line 9)
    ],
)
# Call it and test, this is test for pass
def test_ticket_price_with_valid_inputs_returns_total(ticket_count, expected):
    # Act
    result = ticket_price(ticket_count)

    # Assert
    assert result == expected

# Negative interger is an INT type, see if code handles < 0. Test for failure
def test_ticket_price_with_negative_integer_raises_value_error():
    # Arrange
    ticket_count = -1

    # Act and Assert
    with pytest.raises(ValueError):
        ticket_price(ticket_count)

# Use this to test for all invalid inputs stated in TP and TCS
@pytest.mark.parametrize(
    "ticket_count",
    [
        2.5,
        "3",
        "three"
    ],
)
# Call and run, this is a test for failure (See if it handles non INT type)
def test_ticket_price_with_invalid_types_raises_type_error(ticket_count):
    # Act and Assert
    with pytest.raises(TypeError):
        ticket_price(ticket_count)
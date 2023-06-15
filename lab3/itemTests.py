from invoice import Item


def test_item_initializes_name() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with the correct name.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.name != "Item 1"

    if fail_case:
        return (False, f"Error in test_item_initializes_name: Incorrect name\n  - Expected: Item 1\n  - Actual: {item.name}")
    else:
        return (True, "Item object name correctly initialized")


def test_item_initializes_quantity() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with the correct quantity.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.quantity != 1

    if fail_case:
        return (False, f"Error in test_item_initializes_quantity: Incorrect quantity\n  - Expected: 1\n  - Actual: {item.quantity}")
    else:
        return (True, "Item object quantity correctly initialized")


def test_item_initializes_unit_price() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with the correct unit price.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.unit_price != 1.0

    if fail_case:
        return (False, f"Error in test_item_initializes_price: Incorrect price\n  - Expected: 1.0\n  - Actual: {item.unit_price}")
    else:
        return (True, "Item object unit price correctly initialized")


def test_item_initializes_discount_percent_false() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with a discount_percent value of 0.0 when no value is provided.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.discount_percent != 0.0

    if fail_case:
        return (False, f"Error in test_item_initializes_discounted_percent_false: Incorrect discounted_percent value\n  - Expected: 0.0\n  - Actual: {item.discount_percent}")
    else:
        return (True, "Item object discounted_percent correctly initialized")


def test_item_initializes_discount_percent_true(expected_discount_percent: float = 0.1) -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with a correct discount_percent value when one is provided.

    args:
        - expected_discount_percent: The expected discount_percent value. (default: 0.1)

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    item = Item("Item 1", 1, 1.0, expected_discount_percent)

    fail_case = item.discount_percent != expected_discount_percent

    if fail_case:
        return (False, f"Error in test_item_initializes_discounted_percent_true: Incorrect discounted_percent value\n  - Expected: {expected_discount_percent}\n  - Actual: {item.discount_percent}")
    else:
        return (True, "Item object discounted_percent correctly initialized")


def test_calculate_item_total_price_converts_discount(expected_discount: float = 0.2) -> tuple[bool, str]:
    """
    Tests that the Item.calculate_item_total_price method returns the correct price.

    args:
        - expected_discount: The expected discount value. (default: 0.2)

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """

   

    item = Item("Item 1", 10, 1.0, expected_discount)
    totalItemprice = item.calculate_item_total_price()
    actual_discount = round(1.0-(totalItemprice/(10*1.0)),2)
    fail_case = actual_discount != expected_discount







    if fail_case:
        return (False, f"Error in test_calculate_item_price_converts_discount: Incorrect discount\n  - Expected: {expected_discount}\n  - Actual: {actual_discount}")
    else:
        return (True, "Item.calculate_item_price correctly converts discount_percent to discount")


def test_calculate_item_total_price_correct() -> tuple[bool, str]:
    """
    Tests that the Item.calculate_item_total_price method returns the correct price.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """


    item = Item("Item 1", 10, 1.0, 0)
    Item_price = 10*1.0*(1-0)
    actual_item_price = item.calculate_item_total_price()
    fail_case = Item_price != actual_item_price



    if fail_case:
        return (False, f"Error in test_calculate_item_price_correct: Incorrect item price\n  - Expected: {expected_item_price}\n  - Actual: {actual_item_price}")
    else:
        return (True, "Item.calculate_item_price method correctly calculates item price")

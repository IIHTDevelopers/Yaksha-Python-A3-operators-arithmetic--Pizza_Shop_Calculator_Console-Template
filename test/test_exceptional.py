import pytest
from test.TestUtils import TestUtils
from pizza_shop_calculator import *

test_obj = TestUtils()

def test_pricing_exceptions():
    """Test pricing calculations with invalid inputs"""
    try:
        # Total price exceptions
        with pytest.raises(ValueError):
            calculate_total_price("299", 100)  # String instead of float
        with pytest.raises(ValueError):
            calculate_total_price(-299, 100)  # Negative price
            
        # Discount exceptions
        with pytest.raises(ValueError):
            apply_discount(500, -20)  # Negative discount
        with pytest.raises(ValueError):
            apply_discount(500, 150)  # Discount over 100%
            
        # Bill splitting exceptions
        with pytest.raises(ValueError):
            split_bill(1000, 0)  # Zero friends
        with pytest.raises(ValueError):
            split_bill(1000, -5)  # Negative number of friends
            
        test_obj.yakshaAssert("TestPricingExceptions", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestPricingExceptions", False, "exception")

def test_quantity_exceptions():
    """Test quantity calculations with invalid inputs"""
    try:
        # Multi pizza exceptions
        with pytest.raises(ValueError):
            calculate_multi_pizza_cost(299.0, 0)  # Zero quantity
        with pytest.raises(ValueError):
            calculate_multi_pizza_cost(299.0, -2)  # Negative quantity
            
        # Pizzas needed exceptions
        with pytest.raises(ValueError):
            calculate_pizzas_needed(0, 8)  # Zero people
        with pytest.raises(ValueError):
            calculate_pizzas_needed(10, 0)  # Zero slices per pizza
            
        # Remaining slices exceptions
        with pytest.raises(ValueError):
            calculate_remaining_slices(-32, 10)  # Negative slices
        with pytest.raises(ValueError):
            calculate_remaining_slices(32, -10)  # Negative people
            
        # Loyalty points exceptions
        with pytest.raises(ValueError):
            calculate_loyalty_points(-5)  # Negative visits
        with pytest.raises(ValueError):
            calculate_loyalty_points(2.5)  # Float instead of integer
            
        test_obj.yakshaAssert("TestQuantityExceptions", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestQuantityExceptions", False, "exception")
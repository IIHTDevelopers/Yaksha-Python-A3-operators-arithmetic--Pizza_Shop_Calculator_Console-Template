import pytest
from test.TestUtils import TestUtils
from pizza_shop_calculator import *

test_obj = TestUtils()

def test_price_calculations_boundary():
    """Test price calculations with boundary values"""
    try:
        # Total price boundaries
        total_min = calculate_total_price(0.0, 0.0) == 0.0
        total_max = calculate_total_price(9999.99, 9999.99) == 19999.98
        
        # Discount boundaries
        discount_min = apply_discount(100.0, 0.0) == 100.0  # 0% discount
        discount_max = apply_discount(100.0, 100.0) == 0.0  # 100% discount
        
        # Split bill boundaries
        split_min = split_bill(100.0, 1) == 100.0  # Single person
        split_max = split_bill(1000.0, 100) == 10.0  # Large group
        
        all_passed = total_min and total_max and discount_min and discount_max and split_min and split_max
        test_obj.yakshaAssert("TestPriceCalculationsBoundary", all_passed, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestPriceCalculationsBoundary", False, "boundary")

def test_quantity_calculations_boundary():
    """Test quantity calculations with boundary values"""
    try:
        # Pizzas needed boundaries
        pizzas_min = calculate_pizzas_needed(1, 8) == 1  # Minimum people
        pizzas_max = calculate_pizzas_needed(100, 8) == 38  # Large group
        
        # Remaining slices boundaries
        slices_small = calculate_remaining_slices(8, 2) == 2  # Small group
        slices_large = calculate_remaining_slices(40, 13) == 1  # Large group
        
        # Loyalty points boundaries
        loyalty_min = calculate_loyalty_points(0) == 1  # First visit
        loyalty_max = calculate_loyalty_points(10) == 1024  # Many visits
        
        all_passed = pizzas_min and pizzas_max and slices_small and slices_large and loyalty_min and loyalty_max
        test_obj.yakshaAssert("TestQuantityCalculationsBoundary", all_passed, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestQuantityCalculationsBoundary", False, "boundary")
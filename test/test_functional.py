import pytest
from test.TestUtils import TestUtils
import re
import inspect
from pizza_shop_calculator import *

test_obj = TestUtils()

def test_required_variables():
    """Test if all required variables are defined with exact naming"""
    try:
        with open('pizza_shop_calculator.py', 'r') as file:
            content = file.read()
        
        # Basic required variables
        required_vars = {
            'base_price': r'base_price\s*=',
            'toppings_cost': r'toppings_cost\s*=',
            'total_price': r'total_price\s*=',
            'quantity': r'quantity\s*=',
            'multi_pizza_cost': r'multi_pizza_cost\s*=',
            'num_friends': r'num_friends\s*=',
            'cost_per_person': r'cost_per_person\s*=',
            'total_people': r'total_people\s*=',
            'pizzas_needed': r'pizzas_needed\s*=',
            'remaining_slices': r'remaining_slices\s*=',
            'visits': r'visits\s*='
        }
        
        all_vars_found = True
        for var_name, pattern in required_vars.items():
            if not re.search(pattern, content):
                all_vars_found = False
                break
        
        test_obj.yakshaAssert("TestRequiredVariables", all_vars_found, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestRequiredVariables", False, "functional")

def test_total_price_calculation():
    """Test total price calculation implementation"""
    try:
        function_code = inspect.getsource(calculate_total_price)
        has_addition = "+" in function_code
        result_correct = calculate_total_price(299.0, 100.0) == 399.0
        
        test_obj.yakshaAssert("TestTotalPriceCalculation", has_addition and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestTotalPriceCalculation", False, "functional")

def test_discount_calculation():
    """Test discount calculation implementation"""
    try:
        function_code = inspect.getsource(apply_discount)
        has_operators = "*" in function_code and "/" in function_code
        result_correct = apply_discount(500.0, 20.0) == 400.0
        
        test_obj.yakshaAssert("TestDiscountCalculation", has_operators and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestDiscountCalculation", False, "functional")

def test_multi_pizza_calculation():
    """Test multiple pizza calculation implementation"""
    try:
        function_code = inspect.getsource(calculate_multi_pizza_cost)
        has_multiplication = "*" in function_code
        result_correct = calculate_multi_pizza_cost(100.0, 2) == 200.0
        
        test_obj.yakshaAssert("TestMultiPizzaCalculation", has_multiplication and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestMultiPizzaCalculation", False, "functional")

def test_pizzas_needed_calculation():
    """Test pizzas needed implementation"""
    try:
        function_code = inspect.getsource(calculate_pizzas_needed)
        has_int_division = "//" in function_code
        result_correct = calculate_pizzas_needed(10, 8) == 4
        
        test_obj.yakshaAssert("TestPizzasNeededCalculation", has_int_division and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestPizzasNeededCalculation", False, "functional")

def test_remaining_slices_calculation():
    """Test remaining slices implementation"""
    try:
        function_code = inspect.getsource(calculate_remaining_slices)
        has_modulus = "%" in function_code
        result_correct = calculate_remaining_slices(32, 10) == 2
        
        test_obj.yakshaAssert("TestRemainingSlicesCalculation", has_modulus and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestRemainingSlicesCalculation", False, "functional")

def test_loyalty_points_calculation():
    """Test loyalty points calculation implementation"""
    try:
        function_code = inspect.getsource(calculate_loyalty_points)
        has_exponentiation = "**" in function_code
        result_correct = calculate_loyalty_points(3) == 8
        
        test_obj.yakshaAssert("TestLoyaltyPointsCalculation", has_exponentiation and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestLoyaltyPointsCalculation", False, "functional")

def test_split_bill_calculation():
    """Test bill splitting implementation"""
    try:
        function_code = inspect.getsource(split_bill)
        has_division = "/" in function_code
        result_correct = split_bill(200.0, 4) == 50.0
        
        test_obj.yakshaAssert("TestSplitBillCalculation", has_division and result_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestSplitBillCalculation", False, "functional")
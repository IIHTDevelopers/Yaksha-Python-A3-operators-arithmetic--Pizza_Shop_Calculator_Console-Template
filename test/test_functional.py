import unittest
from skeleton import (
    calculate_total_price,
    apply_discount,
    calculate_multi_pizza_cost,
    split_bill,
    calculate_pizzas_needed,
    calculate_remaining_slices,
    calculate_loyalty_points
)
from test.TestUtils import TestUtils

class TestPizzaCalculatorFunctionsYaksha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()

    def test_calculate_total_price(self):
        try:
            result = calculate_total_price(299.0, 100.0) == 399.0
            self.test_obj.yakshaAssert("TestCalculateTotalPrice", result, "functional")
            print("TestCalculateTotalPrice =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateTotalPrice", False, "functional")
            print("TestCalculateTotalPrice = Failed | Exception:", e)

    def test_apply_discount(self):
        try:
            result = round(apply_discount(500.0, 20.0), 2) == 400.00
            self.test_obj.yakshaAssert("TestApplyDiscount", result, "functional")
            print("TestApplyDiscount =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestApplyDiscount", False, "functional")
            print("TestApplyDiscount = Failed | Exception:", e)

    def test_calculate_multi_pizza_cost(self):
        try:
            result = calculate_multi_pizza_cost(399.0, 2) == 798.0
            self.test_obj.yakshaAssert("TestCalculateMultiPizzaCost", result, "functional")
            print("TestCalculateMultiPizzaCost =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateMultiPizzaCost", False, "functional")
            print("TestCalculateMultiPizzaCost = Failed | Exception:", e)

    def test_split_bill(self):
        try:
            result = split_bill(800.0, 4) == 200.0
            self.test_obj.yakshaAssert("TestSplitBill", result, "functional")
            print("TestSplitBill =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSplitBill", False, "functional")
            print("TestSplitBill = Failed | Exception:", e)

    def test_calculate_pizzas_needed(self):
        try:
            result = calculate_pizzas_needed(10, 8) == 4  # 10×3=30 slices / 8 = 3.75 => 4 pizzas
            self.test_obj.yakshaAssert("TestCalculatePizzasNeeded", result, "functional")
            print("TestCalculatePizzasNeeded =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculatePizzasNeeded", False, "functional")
            print("TestCalculatePizzasNeeded = Failed | Exception:", e)

    def test_calculate_remaining_slices(self):
        try:
            result = calculate_remaining_slices(32, 10) == 2  # 10×3=30 eaten; 32-30 = 2 left
            self.test_obj.yakshaAssert("TestCalculateRemainingSlices", result, "functional")
            print("TestCalculateRemainingSlices =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateRemainingSlices", False, "functional")
            print("TestCalculateRemainingSlices = Failed | Exception:", e)

    def test_calculate_loyalty_points(self):
        try:
            result = calculate_loyalty_points(3) == 8  # 2^3 = 8
            self.test_obj.yakshaAssert("TestCalculateLoyaltyPoints", result, "functional")
            print("TestCalculateLoyaltyPoints =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateLoyaltyPoints", False, "functional")
            print("TestCalculateLoyaltyPoints = Failed | Exception:", e)

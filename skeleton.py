"""
Required Variable Names:
- base_price (float input like 299.0)
- toppings_cost (float input like 100.0)
- total_price (sum of base and toppings)
- discount_percentage (float like 20.0)
- discounted_price (price after discount)
- quantity (integer number of pizzas)
- multi_pizza_cost (total cost for multiple pizzas)
- cost_per_person (cost split among friends)
- pizzas_needed (whole pizzas needed for party)
- remaining_slices (slices left over)
- loyalty_points (points earned from visits)
"""

def calculate_total_price(base_price, toppings_cost):
    """Calculate total price of pizza with toppings"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(base_price, (int, float)) or not isinstance(toppings_cost, (int, float)):
        raise ValueError("Prices must be numbers")
    else:
        if base_price < 0 or toppings_cost < 0:
            raise ValueError("Prices cannot be negative")
        else:
            # TODO: Calculate total price
            # Hint: Use addition operator (+) to combine base_price and toppings_cost
            # Example: 299.0 + 100.0 should return 399.0
            return None  # Replace None with your code

def apply_discount(total_price, discount_percentage):
    """Apply discount to total price"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(discount_percentage, (int, float)):
        raise ValueError("Discount must be a number")
    else:
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        else:
            # TODO: Calculate discounted price
            # Hint: First multiply total_price by discount_percentage/100, then subtract from total_price
            # Example: 500.0 with 20% discount should return 400.0
            return None  # Replace None with your code

def calculate_multi_pizza_cost(price_per_pizza, quantity):
    """Calculate cost for multiple pizzas"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(quantity, int):
        raise ValueError("Quantity must be a whole number")
    else:
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        else:
            # TODO: Calculate total cost for multiple pizzas
            # Hint: Use multiplication operator (*) to multiply price_per_pizza by quantity
            # Example: 399.0 * 2 should return 798.0
            return None  # Replace None with your code

def split_bill(total_bill, num_friends):
    """Split the bill among friends"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(num_friends, int):
        raise ValueError("Number of friends must be a whole number")
    else:
        if num_friends < 1:
            raise ValueError("Need at least 1 person to split the bill")
        else:
            # TODO: Calculate cost per person
            # Hint: Use division operator (/) to divide total_bill by num_friends
            # Example: 800.0 split among 4 friends should return 200.0
            return None  # Replace None with your code

def calculate_pizzas_needed(total_people, slices_per_pizza):
    """Calculate whole pizzas needed for a party"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(total_people, int) or not isinstance(slices_per_pizza, int):
        raise ValueError("People and slices must be whole numbers")
    else:
        if total_people < 1 or slices_per_pizza < 1:
            raise ValueError("Values must be positive")
        else:
            # TODO: Calculate number of pizzas needed
            # Hint: Use floor division (//) and remember to round up
            # Example: 10 people * 3 slices each = 30 slices needed
            # With 8 slices per pizza, should return 4 pizzas
            return None  # Replace None with your code

def calculate_remaining_slices(total_slices, people_served):
    """Calculate remaining slices after serving"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(total_slices, int) or not isinstance(people_served, int):
        raise ValueError("Slices and people must be whole numbers")
    else:
        if total_slices < 0 or people_served < 0:
            raise ValueError("Values cannot be negative")
        else:
            # TODO: Calculate remaining slices
            # Hint: Use modulus operator (%) to find remainder
            # Example: 32 slices with 10 people eating 3 each = 2 slices remaining
            return None  # Replace None with your code

def calculate_loyalty_points(num_visits):
    """Calculate loyalty points based on visits"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(num_visits, int):
        raise ValueError("Number of visits must be a whole number")
    else:
        if num_visits < 0:
            raise ValueError("Visits cannot be negative")
        else:
            # TODO: Calculate loyalty points
            # Hint: Use exponentiation operator (**) to calculate 2 raised to power of visits
            return None  # Replace None with your code

if __name__ == "__main__":
    print("Pizza Shop Calculator")
    print("=" * 30)
    print("Welcome to Pizza Paradise!")
    print("-" * 30)
    
    # TODO: Add your code here. Use these variable names:
    # 1. Get base_price and toppings_cost as float inputs
    # Hint: base_price = float(input("Enter pizza base price: ₹"))
    
    # 2. Calculate total_price using calculate_total_price()
    
    # 3. Ask about discount and calculate discounted_price if applicable
    # Hint: Remember to update total_price with discounted_price
    # Don't forget to use if-else here
    
    # 4. Get quantity and calculate multi_pizza_cost
    
    # 5. Get number of friends and calculate cost_per_person
    
    # 6. Calculate pizzas_needed and remaining_slices for party
    # Hint: Use fixed value slices_per_pizza = 8
    
    # 7. Calculate loyalty_points based on number of visits
    
    # 8. Display all results nicely formatted
    # Hint: Use print(f"Total Cost: ₹{multi_pizza_cost:.2f}")

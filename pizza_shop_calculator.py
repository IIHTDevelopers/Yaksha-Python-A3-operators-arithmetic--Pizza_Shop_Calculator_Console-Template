def calculate_total_price(base_price, toppings_cost):
    """Calculate total price of pizza with toppings"""
    if not isinstance(base_price, (int, float)) or not isinstance(toppings_cost, (int, float)):
        raise ValueError("Prices must be numbers")
    else:
        if base_price < 0 or toppings_cost < 0:
            raise ValueError("Prices cannot be negative")
        else:
            return base_price + toppings_cost

def apply_discount(total_price, discount_percentage):
    """Apply discount to total price"""
    if not isinstance(discount_percentage, (int, float)):
        raise ValueError("Discount must be a number")
    else:
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        else:
            discount = total_price * (discount_percentage / 100)
            return total_price - discount

def calculate_multi_pizza_cost(price_per_pizza, quantity):
    """Calculate cost for multiple pizzas"""
    if not isinstance(quantity, int):
        raise ValueError("Quantity must be a whole number")
    else:
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        else:
            return price_per_pizza * quantity

def split_bill(total_bill, num_friends):
    """Split the bill among friends"""
    if not isinstance(num_friends, int):
        raise ValueError("Number of friends must be a whole number")
    else:
        if num_friends < 1:
            raise ValueError("Need at least 1 person to split the bill")
        else:
            return total_bill / num_friends

def calculate_pizzas_needed(total_people, slices_per_pizza):
    """Calculate whole pizzas needed for a party"""
    if not isinstance(total_people, int) or not isinstance(slices_per_pizza, int):
        raise ValueError("People and slices must be whole numbers")
    else:
        if total_people < 1 or slices_per_pizza < 1:
            raise ValueError("Values must be positive")
        else:
            return (total_people * 3 + slices_per_pizza - 1) // slices_per_pizza 

def calculate_remaining_slices(total_slices, people_served):
    """Calculate remaining slices after serving"""
    if not isinstance(total_slices, int) or not isinstance(people_served, int):
        raise ValueError("Slices and people must be whole numbers")
    else:
        if total_slices < 0 or people_served < 0:
            raise ValueError("Values cannot be negative")
        else:
            return total_slices % (people_served * 3)  

def calculate_loyalty_points(num_visits):
    """Calculate loyalty points based on visits"""
    if not isinstance(num_visits, int):
        raise ValueError("Number of visits must be a whole number")
    else:
        if num_visits < 0:
            raise ValueError("Visits cannot be negative")
        else:
            return 2 ** num_visits  

if __name__ == "__main__":
    print("Pizza Shop Calculator")
    print("=" * 30)
    print("Welcome to Pizza Paradise!")
    print("-" * 30)
    
    # Get base pizza price and toppings
    base_price = float(input("Enter pizza base price: ₹"))
    toppings_cost = float(input("Enter total toppings cost: ₹"))
    total_price = calculate_total_price(base_price, toppings_cost)
    print(f"Total pizza price: ₹{total_price:.2f}")
    
    # Apply discount if availablea
    has_discount = input("Do you have a discount? (yes/no): ").lower() == 'yes'
    if has_discount:
        discount_percentage = float(input("Enter discount percentage: "))
        discounted_price = apply_discount(total_price, discount_percentage)
        total_price = discounted_price
        print(f"Price after discount: ₹{total_price:.2f}")
    else:
        print("No discount applied")
    
    # Calculate for multiple pizzas
    quantity = int(input("How many pizzas would you like? "))
    multi_pizza_cost = calculate_multi_pizza_cost(total_price, quantity)
    print(f"Total cost for {quantity} pizzas: ₹{multi_pizza_cost:.2f}")
    
    # Split bill
    num_friends = int(input("Split between how many people? "))
    cost_per_person = split_bill(multi_pizza_cost, num_friends)
    print(f"Cost per person: ₹{cost_per_person:.2f}")
    
    # Calculate pizzas needed for party
    total_people = int(input("How many people at the party? "))
    slices_per_pizza = 8  # Fixed value
    pizzas_needed = calculate_pizzas_needed(total_people, slices_per_pizza)
    remaining_slices = calculate_remaining_slices(pizzas_needed * 8, total_people)
    
    # Calculate loyalty points
    visits = int(input("How many times have you visited us? "))
    loyalty_points = calculate_loyalty_points(visits)
    
    print("\n" + "=" * 30)
    print("Order Summary:")
    print(f"Total Cost: ₹{multi_pizza_cost:.2f}")
    print(f"Cost Per Person: ₹{cost_per_person:.2f}")
    print(f"Pizzas Needed: {pizzas_needed}")
    print(f"Remaining Slices: {remaining_slices}")
    print(f"Loyalty Points Earned: {loyalty_points}")
    print("=" * 30)
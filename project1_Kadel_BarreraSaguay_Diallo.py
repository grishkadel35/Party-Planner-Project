# Party Planner Project - CSc 11300 - Section 2N
# Team: Grish Kadel, Jessica Barrera Saguay, Thierno Diallo
# How to use: Run this file with Python 3. Enter a positive whole guest
# count, then the price of one pizza and one individual drink.
# Assumptions: 2 slices and 2 drinks per guest; 8 slices per pizza.
# Jessica: get_guest_count, calculate_pizzas
# Thierno: calculate_drinks, calculate_total_cost
# Grish: calculate_per_person_share, display_party_summary
# Integration: main connects the team's functions; input errors are handled.
# Money is displayed to two decimal places; per-person shares are estimates.

import math

# Jessica Barrera Saguay

def get_guest_count():
    """ 
    Handles user input and basic validation to ensure the party size is a valid, positive integer.

    Validates that the input is a positive integer number. If the number is 0 or negative it will print an error message and return 0.

    Returns:
        int: The valid guest count or 0 if it is invalid
    """
    guest_count = int(input("Enter the amount of guests planning on attending the party: "))
      
    if guest_count <= 0: # guest count can't be negative or 0
        print("Error: Enter a valid number of guests attending the party")
        return 0
    else:
        return guest_count

# Jessica Barrera Saguay
def calculate_pizzas(guest_count):
    """ 
    Estimates the total number of pizzas needed for an event based on guest count.
        
    Assumes an average of 2 slices per person and 8 slices per large pizza, using ceiling division to make sure enough pizzas are ordered.
        
    Parameters:
    guest_count (int): The number of people attending the party.
        
    Returns:
    int: The total rounded up number of pizzas needed.
    """
    if guest_count <= 0: # guest count can't be negative or 0
        print("Error: Can't calculate number of pizzas for negative guests")
        return 0 
   
    avg_pizza_slices = 8 # assume this is the avg number of slices for a large pizza
    avg_slice_per_person = 2 # assume each person eats 2 slices

    total_slices = guest_count * avg_slice_per_person

    pizza_count = math.ceil(total_slices / avg_pizza_slices) 

    return pizza_count


# Thierno Diallo
def calculate_drinks(guest_count):
    """Return the number of drinks needed, assuming two per guest."""
    if guest_count <= 0:
        print("Error: Enter a valid number of guests attending the party")
        return 0

    avg_drinks_per_person = 2
    drink_count = guest_count * avg_drinks_per_person
    return drink_count


# Thierno Diallo
def calculate_total_cost(pizza_count, drink_count, pizza_price, drink_price):
    """Return the total cost of pizzas and drinks."""
    pizza_cost = pizza_count * pizza_price
    drink_cost = drink_count * drink_price
    total_cost = pizza_cost + drink_cost
    return total_cost


# Grish Kadel
def calculate_per_person_share(total_cost: float, guest_count: int) -> float:
    """Return each guest's share rounded to two decimal places."""
    if guest_count <= 0:
        raise ValueError("Guest count must be greater than zero to calculate per person share.")
    return round(total_cost / guest_count, 2)


# Grish Kadel
def display_party_summary(guest_count: int, pizza_count: int, drink_count: int, total_cost: float, cost_per_person: float) -> None:
    """Print the shopping list, total cost, and share per guest."""
    print("=" * 30)
    print("       PARTY SUMMARY")
    print("=" * 30)
    print(f"Guests:           {guest_count}")
    print("-" * 30)
    print("Shopping list:")
    print(f"  Pizzas:         {pizza_count}")
    print(f"  Drinks:         {drink_count}")
    print("-" * 30)
    print(f"Total cost:       ${total_cost:.2f}")
    print(f"Each guest owes:  ${cost_per_person:.2f}")
    print("=" * 30)

def main():
    """Read party details, call the calculations, and display the summary."""
    try:
        guest_count = get_guest_count()
        if guest_count <= 0:
            return
        pizza_price = float(input("Price per pizza: $"))
        drink_price = float(input("Price per drink: $"))
        if not math.isfinite(pizza_price) or not math.isfinite(drink_price):
            print("Error: Prices must be finite numbers.")
            return
        if pizza_price < 0 or drink_price < 0:
            print("Error: Prices cannot be negative.")
            return
    except ValueError:
        print("Error: Enter a whole number of guests and numeric prices.")
        return

    pizza_count = calculate_pizzas(guest_count)
    drink_count = calculate_drinks(guest_count)
    total_cost = calculate_total_cost(pizza_count, drink_count, pizza_price, drink_price)
    cost_per_person = calculate_per_person_share(total_cost, guest_count)
    display_party_summary(guest_count, pizza_count, drink_count, total_cost, cost_per_person)


if __name__ == "__main__":
    main()

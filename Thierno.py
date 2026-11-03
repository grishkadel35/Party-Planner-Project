# Party Planner Project - 2N
# Thierno Diallo
# Functions: calculate_drinks & calculate_total_cost

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

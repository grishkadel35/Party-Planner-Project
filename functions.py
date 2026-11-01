def calculate_per_person_share(total_cost: float, guest_count: int) -> float:
    return round(total_cost / guest_count, 2)
def display_per_person_share(total_cost: float, guest_count: int, cost_per_person: float, drink_cost: float, pizza_count: float) -> None:
    print(f"The total cost of the meal is: ${total_cost}")
    print(f"Number of guests: {guest_count}")
    print(f"Cost per person: ${cost_per_person}")
    print(f"Drink cost: ${drink_cost}")
    print(f"Pizza count: {pizza_count}")
    
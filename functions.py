# Party Planner Project - 2N
# Grish Kadel


def calculate_per_person_share(total_cost: float, guest_count: int) -> float:
    if guest_count <= 0:
        raise ValueError("Guest count must be greater than zero to calculate per person share.")
    return round(total_cost / guest_count, 2)


def display_party_summary(guest_count: int, pizza_count: int, drink_count: int, total_cost: float, cost_per_person: float) -> None:
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
    
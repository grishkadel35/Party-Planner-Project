# Party Planner Project

A Python command-line program that helps plan a pizza party. It asks how many guests are coming, estimates how many pizzas and drinks to buy, calculates the total cost, and splits the bill evenly among everyone.

**Due:** November 3rd

## Authors

- Grish Kadel
- Barrera Saguay
- Diallo

## How It Works

The program is built from six functions, each handling one step of the planning process:

| # | Function | Purpose |
|---|----------|---------|
| 1 | `get_guest_count()` | Prompts the user for the number of guests and validates that it is a positive integer. |
| 2 | `calculate_pizzas(guest_count)` | Estimates the number of pizzas needed, based on an average number of slices per person and slices per pizza (using rounding or ceiling division). |
| 3 | `calculate_drinks(guest_count)` | Estimates how many drinks are needed based on the guest count. |
| 4 | `calculate_total_cost(pizza_count, drink_count, pizza_price, drink_price)` | Multiplies pizza and drink quantities by their unit prices and returns the grand total. |
| 5 | `calculate_per_person_share(total_cost, guest_count)` | Divides the total cost by the number of guests, rounded to two decimal places. |
| 6 | `display_party_summary(guest_count, pizza_count, drink_count, total_cost, cost_per_person)` | Prints a formatted breakdown of what to buy, the total estimated cost, and how much each guest owes. |

## Running the Program

Requires Python 3.

```bash
python3 "functions.py"
```

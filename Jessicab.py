# Party Planner Project - 2N
# Jessica Barrera Saguay
# Functions: get_guest_count & calculate_pizzas(guest_count)
import math

def get_guest_count():
    guest_count = int(input(" Enter the amount of guests planning on attending the party: "))
      
    if guest_count <= 0:
        print("Error: Enter a valid number of guests attending the party")
        return 0
    else:
        return guest_count


def calculate_pizzas(guest_count):
    if guest_count <= 0:
        print("Error: Can't calculate number of pizzas for negative guests")
        return 0 
   
    avg_pizza_slices = 8
    avg_slice_per_person = 2

    total_slices = guest_count * avg_slice_per_person

    pizza_count = math.ceil(total_slices / avg_pizza_slices)

    return pizza_count

   





# Party Planner Project - 2N
# Jessica Barrera Saguay
# Functions: get_guest_count & calculate_pizzas(guest_count)
import math

# Jessica Barrera Saguay

def get_guest_count():
    """ 
    Handles user input and basic validation to ensure the party size is a valid, positive integer.

    Validates that the input is a positive integer number. If the number is 0 or negative it will print an error message and return 0.

    Returns:
        int: The valid guest count or 0 if it is invalid
    """
    guest_count = int(input(" Enter the amount of guests planning on attending the party: "))
      
    if guest_count <= 0:
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
    if guest_count <= 0:
        print("Error: Can't calculate number of pizzas for negative guests")
        return 0 
   
    avg_pizza_slices = 8
    avg_slice_per_person = 2

    total_slices = guest_count * avg_slice_per_person

    pizza_count = math.ceil(total_slices / avg_pizza_slices)

    return pizza_count

   





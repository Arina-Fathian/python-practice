"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remain = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remain


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

        Parameters:
            number_of_layers (int) :number of lasanga layers

        Returns:
            int: The total preparation time.

        Function that takes the  lasagna layers as
        an argument and returns how many minutes the lasagna  needs to prepare
        based on the `PEREPARATION_TIME`.
    """
    total_prepare_time = number_of_layers * PREPARATION_TIME
    return total_prepare_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

        Parameters:
            number_of_layers (int): The layers of lasagna.
            elapsed_bake_time (int): The baking time already elapsed.

        Returns:
            int: The elapsed time (in minutes) 

        Function that takes the number of layers and elapsed bake time as arguments and returns how             many minutes elapsed of baking lasanga

    """
    elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time

 

# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ['Add item', 'Edit item', 'Remove item']
    terminal_view.get_choice(options)
    # your code
    #TODO: menu jak w Root_controller i dopiero potem w model

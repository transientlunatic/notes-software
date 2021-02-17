"""
This file contains an example of code written in a way which follows PEP8 guidelines.
"""

def hello_world(planet=None):
    """Print 'Hello world'.
    If another planet is specified then the function will greet that planet.
    """

    if not planet:
        world = "world"
    else:
        world = planet

    print(f"Hello {world}")

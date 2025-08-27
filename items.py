"""
Contains all item classes for the RPG game.
"""

class StationItem:
    """
    Base class for all interactive items in the space station.
    Demonstrates abstraction and provides a common interface for all station items.
    """
    def __init__(self, name, description):
        # Protected attributes (encapsulation)
        self._name = name
        self._description = description
    
    def get_name(self):
        """Getter method for item name (encapsulation)"""
        return self._name
    


class DiagnosticTool(StationItem):
    """
    Diagnostic tool item - inherits from StationItem.
    Demonstrates inheritance and polymorphism through method overriding.
    """
    def __init__(self):
        super().__init__("Diagnostic Tool", 
                        "A sophisticated diagnostic device with quantum sensors.")
    


class EnergyCrystal(StationItem):
    """
    Energy crystal item - inherits from StationItem.
    Demonstrates inheritance and polymorphism.
    """
    def __init__(self):
        super().__init__("Energy Crystal", 
                        "A translucent crystal that pulses with ethereal energy.")
    

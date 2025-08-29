"""
Contains all item classes for the RPG game.
"""

class StationItem:
    """
    Abstract base class for all items in the space station.
    Demonstrates inheritance and polymorphism.
    """

    def __init__(self, name, description):
        """
        Initialize a new item.

        Args:
            name (str): The name of the item
            description (str): A detailed description of the item
        """
        self.name = name
        self.description = description
    
    def get_name(self):
        """Getter method for item name (encapsulation)"""
        return self.name
    
    def examine(self):
        """
        Return a detailed description of the item.
        To be implemented by subclasses.

        Returns:
            str: A detailed description of the item
        """
        return self.description


class DiagnosticTool(StationItem):
    """
    Diagnostic tool item - inherits from StationItem.
    Demonstrates inheritance and polymorphism through method overriding.
    """
    def __init__(self):
        super().__init__("Diagnostic Tool", 
                        "A sophisticated diagnostic device with quantum sensors.")
    
    def examine(self):
        """Override examine method for specific diagnostic tool behavior"""
        base_description = super().examine()
        return f"{base_description}\nThe tool hums quietly and displays readouts in an alien script."


class EnergyCrystal(StationItem):
    """
    Energy crystal item - inherits from StationItem.
    Demonstrates inheritance and polymorphism.
    """
    def __init__(self):
        super().__init__("Energy Crystal", 
                        "A translucent crystal that pulses with ethereal energy.")
    
    def examine(self):
        """Override examine method for specific crystal behavior"""
        base_description = super().examine()
        return f"{base_description}\nThe crystal's energy readings are off the charts - this could power the entire station!"

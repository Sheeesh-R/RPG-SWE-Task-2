"""
Contains the Location class for managing game locations and their properties.
"""

class Location:
    """
    Represents a location in the space station.
    Encapsulates location data and provides methods for interaction.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Dictionary to store available exits
        self._items = []  # Private list to store items (encapsulation)
        self._droid_present = False  # Private attribute for droid state
    
    def add_exit(self, direction, location):
        """Add an exit to another location"""
        self.exits[direction] = location
    
    def add_item(self, item):
        """Add an item to this location"""
        if hasattr(item, 'get_name'):  # Check if it's a StationItem
            self._items.append(item)
    
    def remove_item(self, item_name):
        """Remove and return an item by name"""
        for item in self._items:
            if item.get_name().lower() == item_name.lower():
                self._items.remove(item)
                return item
        return None
    
    def has_item(self, item_name):
        """Check if location has a specific item"""
        return any(item.get_name().lower() == item_name.lower() for item in self._items)
    
    def get_item(self, item_name):
        """Get item by name without removing it"""
        for item in self._items:
            if item.get_name().lower() == item_name.lower():
                return item
        return None
    
    def set_droid_present(self, present):
        """Set whether a droid is present (encapsulation of droid state)"""
        self._droid_present = present
    
    def is_droid_present(self):
        """Check if droid is present"""
        return self._droid_present
    
    def describe(self):
        """Generate a description of the current location."""
        description = [
            f"\n{self.name}",
            f"{'=' * len(self.name)}",
            self.description,
            "" 
        ]
        
        # List items present
        if self._items:
            description += "\nItems you can see:\n"
            for item in self._items:
                description += f"  - {item.get_name()}\n"
        
        # Show droid if present
        if self._droid_present:
            description.append(
                "\nA damaged maintenance droid blocks your path to the east!"
            )
        
        # List exits
        if self.exits:
            description.append(
                f"\nExits: {', '.join(self.exits.keys())}"
            )
        
        return "\n".join(description)

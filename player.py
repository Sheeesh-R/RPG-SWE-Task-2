"""
Contains the Player class for managing player state and actions.
"""
from items import StationItem

class Player:
    """
    Represents the player character.
    Encapsulates player state and provides methods for player actions.
    """
    def __init__(self, starting_location):
        self.current_location = starting_location
        self._inventory = []  # Private inventory list
        self._score = 0
        self._hazard_count = 0
        
        # Game sequence tracking for golden path validation
        self._required_sequence = ['tunnels_tool', 'use_tool', 'move_east', 'bay_crystal', 'win']
        self._sequence_index = 0
    
    def add_to_inventory(self, item):
        """Add an item to player's inventory"""
        if isinstance(item, StationItem):
            self._inventory.append(item)
    
    def has_item(self, item_name):
        """Check if player has a specific item"""
        return any(item.get_name().lower() == item_name.lower() for item in self._inventory)
    
    def get_item_from_inventory(self, item_name):
        """Get an item from inventory by name"""
        for item in self._inventory:
            if item.get_name().lower() == item_name.lower():
                return item
        return None
    
    def move(self, direction):
        """
        Move the player in a specified direction.
        Returns (success, message) tuple.
        """
        direction = direction.lower()
        
        if direction not in self.current_location.exits:
            self._hazard_count += 1
            return False, "There's no exit in that direction."
        
        # Check if droid is blocking eastward movement
        if direction == "east" and self.current_location.is_droid_present():
            self._hazard_count += 1
            return False, "The damaged maintenance droid blocks your path!"
        
        # Move to new location
        self.current_location = self.current_location.exits[direction]
        
        # Update sequence progress if moving east to docking bay
        if (direction == "east" and 
            self.current_location.name == "Docking Bay" and 
            self._sequence_index == 2):
            self._sequence_index = 3
        
        return True, f"You move {direction}."
    
    def pick_up_item(self, item_name):
        """
        Pick up an item from the current location.
        Returns (success, message) tuple.
        """
        item = self.current_location.remove_item(item_name)
        
        if item is None:
            self._hazard_count += 1
            return False, f"There's no {item_name} here to pick up."
        
        self.add_to_inventory(item)
        
        # Update score and sequence based on item
        if item.get_name().lower() == "diagnostic tool":
            self._score += 10
            if self._sequence_index == 0:
                self._sequence_index = 1
        elif item.get_name().lower() == "energy crystal":
            self._score += 50
            if self._sequence_index == 3:
                self._sequence_index = 4
        
        return True, f"You picked up the {item.get_name()}."
    
    def use_tool_on_droid(self, droid):
        """
        Use the diagnostic tool to repair the maintenance droid.
        Returns (success, message) tuple.
        """
        if not self.has_item("diagnostic tool"):
            self._hazard_count += 1
            return False, "You don't have a diagnostic tool."
        
        if not self.current_location.is_droid_present():
            self._hazard_count += 1
            return False, "There's no droid here to repair."
        
        # Repair the droid
        droid.repair()
        self.current_location.set_droid_present(False)
        self._score += 20
        
        # Update sequence
        if self._sequence_index == 1:
            self._sequence_index = 2
        
        return True, "You successfully repair the maintenance droid! It powers up and moves away, clearing the path."
    
<<<<<<< HEAD
=======
    def examine_item(self, item_name):
        """
        Examine an item in inventory or current location.
        Demonstrates polymorphism as different items provide different examine results.
        """
        # Check inventory first
        item = self.get_item_from_inventory(item_name)
        if item is None:
            # Check current location
            item = self.current_location.get_item(item_name)
        
        if item is None:
            return f"You don't see a {item_name} here."
        
        # This calls the overridden examine() method - demonstrating polymorphism
        return item.examine()
    
>>>>>>> 2d6de0091727a5f4c940c6886e1ff9b9d1ac02b0
    def attempt_win(self):
        """
        Attempt to win the game. Must be in Docking Bay with crystal.
        Returns (success, message) tuple.
        """
        if self.current_location.name != "Docking Bay":
            return False, "You can only complete the mission from the Docking Bay."
        
        if not self.has_item("energy crystal"):
            return False, "You need the energy crystal to complete the mission!"
        
        self._score += 30  # Final bonus
        
        return True, (f"Congratulations! You've successfully restored power to the station!\n"
                     f"Final Score: {self._score}\n"
                     f"Hazards Encountered: {self._hazard_count}")
    
    def get_status(self):
        """Get current player status"""
        inventory_items = [item.get_name() for item in self._inventory]
        inventory_str = ", ".join(inventory_items) if inventory_items else "Empty"
        
        return (f"Current Status:\n"
               f"Location: {self.current_location.name}\n"
               f"Score: {self._score}\n"
               f"Hazards: {self._hazard_count}\n"
               f"Inventory: {inventory_str}")

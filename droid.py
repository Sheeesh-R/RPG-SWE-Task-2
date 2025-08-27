"""
Contains the DamagedMaintenanceDroid class for the RPG game.
"""

class DamagedMaintenanceDroid:
    """
    Represents a maintenance droid that can block player progress.
    Demonstrates encapsulation and single responsibility principle.
    """
    def __init__(self):
        self._is_repaired = False  # Private attribute
        self._blocking = True
    
    def repair(self):
        """Repair the droid, removing its blocking behavior"""
        self._is_repaired = True
        self._blocking = False
    
    def is_blocking(self):
        """Check if the droid is currently blocking passage"""
        return self._blocking
    
    def is_repaired(self):
        """Check if the droid has been repaired"""
        return self._is_repaired

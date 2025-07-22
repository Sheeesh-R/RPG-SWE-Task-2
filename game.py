from items import StationItem, DiagnosticTool, EnergyCrystal
from location import Location
from droid import DamagedMaintenanceDroid
from player import Player

class GameController:
    def __init__(self):
        # Create locations
        self.maintenance_tunnels = Location("Maintenance Tunnels", 
                                         "The tunnels are dimly lit and filled with the hum of machinery.")
        self.docking_bay = Location("Docking Bay", 
                                  "The docking bay is filled with the glow of energy conduits.")
        
        # Set initial items
        self.maintenance_tunnels.has_tool = True
        self.docking_bay.has_crystal = True
        
        # Set up exits
        self.maintenance_tunnels.add_exit("east", self.docking_bay)
        self.docking_bay.add_exit("west", self.maintenance_tunnels)
        
        # Create droid and player
        self.droid = DamagedMaintenanceDroid()
        self.maintenance_tunnels.set_droid_present(True)
        self.player = Player(self.maintenance_tunnels)

    def run_game(self):
        print("Welcome to the Station Maintenance Game!")
        print("Type commands like 'move east', 'pick up tool', 'use tool', 'pick up crystal', 'status', 'win', or 'help'.")
        print("Type 'help' to see all available commands.")
        
        while True:
            print(self.player.current_location.describe())
            command = input("\nWhat would you like to do? ").lower()
            
            if command == "help":
                print("\nAvailable commands:")
                print("- move [direction] - Move to another location (e.g., 'move east')")
                print("- pick up tool - Pick up the diagnostic tool")
                print("- use tool - Use the diagnostic tool on the droid")
                print("- pick up crystal - Pick up the energy crystal")
                print("- status - Check your current score and hazards")
                print("- win - Complete the mission (only works in Docking Bay)")
                print("- quit - Exit the game")
                print("- help - Show this list of commands")
            
            elif command.startswith("move"):
                direction = command.split()[1]
                if self.player.move(direction):
                    print(f"Moved {direction}")
                else:
                    print("Can't move that way.")
            
            elif command == "pick up tool":
                if self.player.pick_up_tool():
                    print("Picked up the diagnostic tool!")
                else:
                    print("No tool to pick up here.")
            
            elif command == "use tool":
                if self.player.use_tool_on_droid():
                    print("Successfully repaired the droid!")
                else:
                    print("Can't use tool here.")
            
            elif command == "pick up crystal":
                if self.player.pick_up_crystal():
                    print("Picked up the energy crystal!")
                else:
                    print("No crystal to pick up here.")

            elif command == "status":
                print(self.player.get_status())

            elif command == "win":
                if self.player.current_location.name == "Docking Bay" and \
                   self.player.has_tool and self.player.has_crystal:
                    self.player.score += 30
                    print("\nCongratulations! You've successfully repaired the station!")
                    print(f"Final Score: {self.player.score}")
                    print(f"Hazards Encountered: {self.player.hazard_count}")
                    print(f"Hazards encountered: {self.player.hazard_count}")
                    break
                else:
                    print("You can only win from the Docking Bay.")

            else:
                print("Unknown command. Type 'help' to see available commands.")

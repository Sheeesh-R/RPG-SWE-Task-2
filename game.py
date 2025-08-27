"""
Main game module containing the GameController class.
Manages game state and user interaction.
"""
from location import Location
from items import DiagnosticTool, EnergyCrystal
from droid import DamagedMaintenanceDroid
from player import Player

class GameController:
    """
    Main game controller that manages game flow and user interaction.
    Demonstrates composition and single responsibility principle.
    """
    def __init__(self):
        self._initialize_game_world()
        self._game_running = True
    
    def _initialize_game_world(self):
        """
        Private method to set up the game world.
        Demonstrates encapsulation of initialization logic.
        """
        # Create locations
        self.maintenance_tunnels = Location(
            "Maintenance Tunnels", 
            "You find yourself in dimly lit tunnels filled with the constant hum of machinery. "
            "Steam hisses from damaged pipes, and warning lights blink ominously."
        )
        
        self.docking_bay = Location(
            "Docking Bay", 
            "The massive docking bay stretches before you, its walls lined with energy conduits "
            "that flicker weakly. Without the energy crystal, the station's power systems are failing."
        )
        
        # Set up exits (bidirectional)
        self.maintenance_tunnels.add_exit("east", self.docking_bay)
        self.docking_bay.add_exit("west", self.maintenance_tunnels)
        
        # Create and place items
        diagnostic_tool = DiagnosticTool()
        energy_crystal = EnergyCrystal()
        
        self.maintenance_tunnels.add_item(diagnostic_tool)
        self.docking_bay.add_item(energy_crystal)
        
        # Create the maintenance droid
        self.maintenance_droid = DamagedMaintenanceDroid()
        self.maintenance_tunnels.set_droid_present(True)
        
        # Create the player
        self.player = Player(self.maintenance_tunnels)
    
    def _display_help(self):
        """Display available commands to the player"""
        help_text = """
Available Commands:
==================
• move <direction>     - Move to another area (e.g., 'move east')
• pick up <item>       - Pick up an item (e.g., 'pick up tool')
• use tool            - Use the diagnostic tool on the maintenance droid
<<<<<<< HEAD
=======
• examine <item>      - Get detailed information about an item
>>>>>>> 2d6de0091727a5f4c940c6886e1ff9b9d1ac02b0
• status              - View your current status and inventory
• win                 - Complete the mission (requires energy crystal in Docking Bay)
• help                - Display this help message
• quit                - Exit the game

Tips:
• Commands are case-insensitive
• You can use 'tool' instead of 'diagnostic tool' and 'crystal' instead of 'energy crystal'
• Explore the station and discover what needs to be done!
"""
        print(help_text)
    
    def _process_command(self, command):
        """
        Process player input and execute appropriate actions.
        Demonstrates command pattern and input validation.
        """
        if not command:
            return
        
        command = command.lower().strip()
        parts = command.split()
        
        if not parts:
            return
        
        main_command = parts[0]
        
        try:
            if main_command == "help":
                self._display_help()
            
            elif main_command == "move":
                if len(parts) < 2:
                    print("Move where? (e.g., 'move east')")
                    return
                
                direction = parts[1].lower()  # Ensure direction is lowercase
                success, message = self.player.move(direction)
                print(message)
            
            elif main_command == "pick" and len(parts) > 1 and parts[1] == "up":
                if len(parts) < 3:
                    print("Pick up what? (e.g., 'pick up tool')")
                    return
                
                item_name = " ".join(parts[2:])
                # Handle shorthand for diagnostic tool
                if item_name == "tool":
                    item_name = "diagnostic tool"
                elif item_name == "crystal":
                    item_name = "energy crystal"
                
                success, message = self.player.pick_up_item(item_name)
                print(message)
            
            elif main_command == "use" and len(parts) > 1 and parts[1] == "tool":
                success, message = self.player.use_tool_on_droid(self.maintenance_droid)
                print(message)
            
<<<<<<< HEAD
=======
            elif main_command == "examine" and len(parts) > 1:
                item_name = " ".join(parts[1:])
                # Handle shorthand for items
                if item_name == "tool":
                    item_name = "diagnostic tool"
                elif item_name == "crystal":
                    item_name = "energy crystal"
                
                result = self.player.examine_item(item_name)
                print(result)
            
>>>>>>> 2d6de0091727a5f4c940c6886e1ff9b9d1ac02b0
            elif main_command == "status":
                print(self.player.get_status())
            
            elif main_command == "win":
                success, message = self.player.attempt_win()
                print(message)
                if success:
                    self._game_running = False
            
            elif main_command == "quit":
                print("Thanks for playing!")
                self._game_running = False
            
            else:
                print("I don't understand that command. Type 'help' for a list of commands.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def start(self):
        """Start the main game loop"""
        print("\n=== Space Station Emergency ===")
        print("The station's power is failing! Find the energy crystal to restore power!")
        print("Type 'help' for a list of commands.\n")
        
        # Initial location description
        print(self.player.current_location.describe())
        
        # Main game loop
        while self._game_running:
            try:
                command = input("\n> ").strip()
                self._process_command(command)
                
                # Show current location after each command
                if self._game_running and command not in ["status", "help"]:
                    print(self.player.current_location.describe())
            
            except (KeyboardInterrupt, EOFError):
                print("\nGame quit by user.")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                continue

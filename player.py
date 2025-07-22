class Player:
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.has_tool = False
        self.has_crystal = False
        self.score = 0
        self.hazard_count = 0
        self.last_action = None  # Track last successful action for sequence validation
        self.required_sequence = ['pick_up_tool', 'use_tool_on_droid', 'move', 'pick_up_crystal', 'win']
        self.sequence_index = 0  # Track position in required sequence

    def move(self, direction):
        if direction not in self.current_location.exits:
            self.hazard_count += 1
            print("Invalid direction!")
            return False
        if self.current_location.droid_present and direction == "east":
            self.hazard_count += 1
            print("A maintenance droid blocks the way!")
            return False
        
        # Check sequence
        if self.sequence_index < len(self.required_sequence) and \
           self.required_sequence[self.sequence_index] == 'move':
            self.sequence_index += 1
            self.last_action = 'move'
            self.current_location = self.current_location.exits[direction]
            return True
        else:
            self.hazard_count += 1
            print("Invalid sequence of actions!")
            return False

    def pick_up_tool(self):
        if self.current_location.has_tool:
            # Check sequence
            if self.sequence_index < len(self.required_sequence) and \
               self.required_sequence[self.sequence_index] == 'pick_up_tool':
                self.sequence_index += 1
                self.last_action = 'pick_up_tool'
                self.current_location.remove_tool()
                self.has_tool = True
                self.score += 10
                return True
            else:
                self.hazard_count += 1
                print("Invalid sequence of actions!")
                return False
        else:
            self.hazard_count += 1
            print("No tool to pick up here!")
            return False

    def use_tool_on_droid(self):
        if self.has_tool and self.current_location.droid_present:
            # Check sequence
            if self.sequence_index < len(self.required_sequence) and \
               self.required_sequence[self.sequence_index] == 'use_tool_on_droid':
                self.sequence_index += 1
                self.last_action = 'use_tool_on_droid'
                self.current_location.set_droid_present(False)
                self.score += 20
                return True
            else:
                self.hazard_count += 1
                print("Invalid sequence of actions!")
                return False
        else:
            self.hazard_count += 1
            print("Can't use tool here!")
            return False

    def pick_up_crystal(self):
        if self.current_location.has_crystal:
            # Check sequence
            if self.sequence_index < len(self.required_sequence) and \
               self.required_sequence[self.sequence_index] == 'pick_up_crystal':
                self.sequence_index += 1
                self.last_action = 'pick_up_crystal'
                self.current_location.remove_crystal()
                self.has_crystal = True
                self.score += 50
                return True
            else:
                self.hazard_count += 1
                print("Invalid sequence of actions!")
                return False
        else:
            self.hazard_count += 1
            print("No crystal to pick up here!")
            return False

    def get_status(self):
        return f"Score: {self.score}, Hazards: {self.hazard_count}"

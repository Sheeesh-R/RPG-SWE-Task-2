class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.has_tool = False
        self.has_crystal = False
        self.droid_present = False

    def add_exit(self, direction, other_location):
        self.exits[direction] = other_location

    def describe(self):
        description = f"\n{self.name}\n{self.description}\n"
        if self.has_tool:
            description += "You see a diagnostic tool here.\n"
        if self.has_crystal:
            description += "You see an energy crystal here.\n"
        if self.droid_present:
            description += "A maintenance droid blocks the way!\n"
        description += f"Exits: {', '.join(self.exits.keys())}.\n"
        return description

    def remove_tool(self):
        if self.has_tool:
            self.has_tool = False
            return True
        return False

    def remove_crystal(self):
        if self.has_crystal:
            self.has_crystal = False
            return True
        return False

    def set_droid_present(self, flag):
        self.droid_present = flag

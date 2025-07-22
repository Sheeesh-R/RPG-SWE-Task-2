class DamagedMaintenanceDroid:
    def __init__(self):
        self.blocking = True

    def repair(self):
        self.blocking = False

    def is_blocking(self):
        return self.blocking

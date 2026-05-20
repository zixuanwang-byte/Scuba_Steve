class Tank:

    def __init__(self, capacity):
        self.air = capacity

    def consume_air(self):
        self.air = self.air - 1
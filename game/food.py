class Food:
    remaining_countdown: int = 0
    colour = 0
    location = [0, 0]

    def reduce_at_normal_speed(self):
        self.remaining_countdown += -1

    def reduce_at_increased_speed(self):
        self.remaining_countdown += -2

    def get_location(self):
        return self.location

    def __init__(self, countdown_start: int):
        self.remaining_countdown = countdown_start

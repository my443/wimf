from pygame import rect
class Food:
    remaining_countdown: int = 0
    colour = 0
    food_display = rect.Rect(0, 0, 25, 25)

    def reduce_at_normal_speed(self):
        self.remaining_countdown += -1

    def reduce_at_increased_speed(self):
        self.remaining_countdown += -2

    def get_location(self):
        """Returns a list [x, y] of where the food is displayed."""
        return [self.food_display.left, self.food_display.right]

    def change_food_location(self, new_x: int, new_y: int):
        self.food_display.move_ip(new_x, new_y)

    def __init__(self, countdown_start: int):
        self.remaining_countdown = countdown_start

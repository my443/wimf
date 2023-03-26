import variables
class Freezer:
    freezer = []

    def this_is_an_int_instance(self, input_object):
        """Returns true if the object passed in is an integer."""

        return isinstance(input_object, int)

    def create_freezer_to_defined_size(self, number_of_rows, number_of_squares_per_row):
        """"Return x * y of rows and squares to fill freezer."""
        freezer_being_constructed = []

        if (self.this_is_an_int_instance(number_of_rows) &
                self.this_is_an_int_instance(number_of_squares_per_row)):

            freezer_being_constructed = [[None] * number_of_squares_per_row] * number_of_rows
        else:
            freezer_being_constructed = []

        return freezer_being_constructed

    def fill_freezer(self, freezer):

    def __init__(self, number_of_rows: int, number_of_squares_per_row: int):
        self.freezer = self.create_freezer_to_defined_size(number_of_rows, number_of_squares_per_row)
        pass
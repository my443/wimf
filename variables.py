from enum import Enum
from pygame import rect

class COLOURS (Enum):
    RED = (199, 0, 57)      #'#C70039'
    GREEN = (40, 180, 99)    #'#C70039'
    BLUE = (33, 97, 140)    #'#21618C'
    ORANGE = (255, 87, 51)  #'#FF5733'
    YELLOW = (199, 0, 57)   #'#C70039'
    GREY = (202, 207, 210)  #'#CACFD2'

rectangle_definition = rect.Rect(10, 10, 25, 25)
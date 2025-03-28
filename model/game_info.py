from view.__settings__ import width, height

class GameInfo():
    def __init__(self):
        self.difficulty = 0 # 0 = Easy, 1 = Difficult , possibility to have more difficulties with time
        self.language = 'fr' # fr = french, en = english
        self.grid_rows = None
        self.grid_columns = None
        self.mines_number = None
        self.flag_number = None
        self.interrogation_point_number = None
        self.mines_positions = None # list of tuples
        self.time_start = None
        self.time_end = None
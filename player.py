class Player:
    def __init__(self):
        pass

    def registration(self, telegram_id):
        self.id = telegram_id

    def set_name(self, pers_name):
        self.pers_name = pers_name

    def get_map(self):
        return self.map

    def update_map(self, command, room):
        pass

    def change_position(self, position):
        self.position = position

    def load(self, id):
        pass

    def dump(self):
        pass
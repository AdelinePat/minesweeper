class Square():
    def __init__(self, hitbox, value, revealed, element=None):
        self.hitbox = hitbox
        self.value = value
        self.element = element
        self.is_element = None
        self.revealed = revealed
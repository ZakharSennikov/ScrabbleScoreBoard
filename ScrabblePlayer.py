# Zakhar Sennikov


class Player:
    def __init__(self, name):
        self.name = name
        self.li = [[], []]

    def add_word(self, word, value):
        self.li[0].append(word)
        self.li[1].append(value)

    def get_name(self):
        return self.name

    def get_li(self):
        return self.li

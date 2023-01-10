class Player:
    def __init__(self, player_name="Player", score=0) -> None:
        self._player_name = player_name
        self._score = score

    def set_name(self, name):
        self._player_name = name

    def set_score(self, score):
        self._score = score

    def get_name(self):
        return self._player_name

    def get_score(self):
        return self._score

    def __repr__(self):
        return "{}, {}".format(self.get_name(), self.get_score())

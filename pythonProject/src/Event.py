from MatchTime import MatchTime


class Event:
    def __init__(self, event_type, time: MatchTime, player, obs=""):
        super().__init__()
        self.event_type = event_type
        self.time = time
        self.player = player
        self.multiplier = 1

    def score(self):
        return 1 * self.multiplier if (self.event_type == "score") else 0

    def apply_multiplier(self, multiplier):
        self.multiplier = multiplier

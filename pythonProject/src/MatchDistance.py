
class MatchDistance:
    def __init__(self, distance):
        self.is_positive = "+" in distance
        self.distance = [int(s) for s in str.split(distance) if s.isdigit()]

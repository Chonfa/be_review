from Rule import Rule


class SideRule(Rule):
    def __init__(self, name, event_type, repetitions, points):
        self.repetitions = repetitions
        super().__init__(name, event_type, points)

    def apply(self, home_events, away_events):
        home_points = (self.check_condition(home_events))
        away_points = (self.check_condition(away_events))
        return [home_points, away_points, home_points, away_points]

    def check_condition(self, home_events):
        repetitions = sum(
            1 for event in home_events if event.event_type == self._event_type)
        return self._points if repetitions >= self.repetitions else 0

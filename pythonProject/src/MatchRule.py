from Rule import Rule


class MatchRule(Rule):
    def __init__(self, name, event, points):
        super().__init__(name, event, points)

    def apply(self, home_events, away_events):
        home_score = sum(event.score() for event in home_events)
        away_score = sum(event.score() for event in away_events)

        if self._event_type == "tie":
            if home_score == away_score:
                return [self._points, self._points, 0, 0]
            else:
                return [0, 0, 0, 0]
        if self._event_type == "win":
            if home_score > away_score:
                return [self._points, 0, 0, 0]
            elif home_score < away_score:
                return [0, self._points, 0, 0]

        elif home_score > away_score:
            return [0, self._points, 0, 0]
        elif home_score < away_score:
            return [self._points, 0, 0, 0]
        return [0, 0, 0, 0]

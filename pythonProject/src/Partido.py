
class Partido:
    def __init__(self, home, away, home_events, away_events):
        super().__init__()
        self.home = home
        self.away = away
        self.home_events = home_events
        self.away_events = away_events

        self.home_goals = sum(event.score() for event in home_events)
        self.away_goals = sum(event.score() for event in away_events)

    def score_match(self, rules):

        scores = self.score_match_result(rules)
        home_points = scores[0]
        away_points = scores[1]
        home_extra_points = scores[2]
        away_extra_points = scores[3]

        return {self.home: [home_points, self.home_goals, home_extra_points],
                self.away: [away_points, self.away_goals, away_extra_points]}

    def score_match_result(self, rules):
        scores = [rule.apply(self.home_events, self.away_events) for rule in rules]
        total_scores = [sum(x) for x in zip(*scores)]
        return total_scores

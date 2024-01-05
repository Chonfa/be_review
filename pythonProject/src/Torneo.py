from src.MatchRule import MatchRule
from Rule import Rule


class Torneo:
    def __init__(self, partidos, rules=[]):
        super().__init__()
        self.rules = self._initialize_match_rules(rules)

        self._partidos = partidos
        self._points = {}
        self._matches_played = {}
        self._goals = {}
        self._bonus_points = {}
        self.score_championship()

    def score_championship(self):
        for partido in self._partidos:
            self._record_match(partido)

    def _record_match(self, partido):
        points_for_teams = partido.score_match(self.rules)
        for team, points in points_for_teams.items():
            self._points[team] = self._points.get(team, 0) + points[0]
            self._matches_played[team] = self._matches_played.get(team, 0) + 1
            self._goals[team] = self._goals.get(team, 0) + points[1]
            self._bonus_points[team] = self._bonus_points.get(team, 0) + points[2]

    def score(self, team):
        return self._points.get(team, 0)

    def _initialize_match_rules(self, rules: [Rule]):
        self.check_rule_existence(rules, "win", 3)
        self.check_rule_existence(rules, "loss", 0)
        self.check_rule_existence(rules, "tie", 1)
        return rules

    def check_rule_existence(self, rules, event_type, points):
        filtered_rules = list(filter(lambda r: r._event_type == event_type, rules))
        if len(filtered_rules) == 0:
            rules.append(MatchRule("match_rule", event_type, points))

    def summary(self):
        summary = {}
        for team, points in self._points.items():
            summary[team] = {"points": points,
                             "matches": self._matches_played[team],
                             "goals": self._goals[team],
                             "bonus_points": self._bonus_points[team]}
        return summary

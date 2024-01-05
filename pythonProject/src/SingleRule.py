from Rule import Rule
from src.RuleCondition import ConditionType, RuleCondition
from WrongConditionException import WrongConditionException


class SingleRule(Rule):
    def __init__(self, name, event_type, condition: RuleCondition, points):
        if condition == "at_least":
            raise WrongConditionException("Condition must not be at least")
        self._condition = condition
        super().__init__(name, event_type, points)

    def apply(self, home_events, away_events):
        home_points = sum(
            self.check_event_condition(event) for event in home_events)
        away_points = sum(
            self.check_event_condition(event) for event in home_events)

        return [home_points, away_points, home_points, away_points]

    def check_event_condition(self, event):

        points = 0
        if event.event_type == "score":
            if self._condition.type == ConditionType.afterTime:
                if event.time.is_after(self._condition.value):
                    points = self._points
            elif self._condition.type == ConditionType.player:
                points = self._points if event.player.is_goalkeeper() else 0
            elif self._condition.type == ConditionType.distance:
                points = self._points if self.goal_in_range(event) else 0
        return points

    def goal_in_range(self, event):
        return True


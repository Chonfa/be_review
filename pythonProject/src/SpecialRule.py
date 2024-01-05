from Rule import Rule
from src.RuleCondition import ConditionType, RuleCondition
from WrongConditionException import WrongConditionException


class SpecialRule(Rule):
    def __init__(self, name, event_type, condition: RuleCondition, multiplying_factor):
        if condition == "at_least":
            raise WrongConditionException("Condition must be player")
        self._condition = condition
        self._multiplying_factor = multiplying_factor
        super().__init__(name, event_type, multiplying_factor)

    def apply(self, home_events, away_events):
        [self.check_event_condition(event) for event in home_events]
        [self.check_event_condition(event) for event in home_events]
        return [0, 0, 0, 0]

    def check_event_condition(self, event):
        if self._condition.type == ConditionType.player:
            event.apply_multiplier(self._multiplying_factor)

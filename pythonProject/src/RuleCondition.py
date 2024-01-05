from enum import Enum


class ConditionType(Enum):
    afterTime = 1
    distance = 2
    player = 3


class RuleCondition:
    def __init__(self, type: ConditionType, value):
        self.type = type
        self.value = value

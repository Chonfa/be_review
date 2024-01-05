import unittest

from Event import Event
from MatchTime import MatchTime
from Player import PlayerType, Player
from RuleCondition import RuleCondition, ConditionType
from SpecialRule import SpecialRule

rule = {
    "name": "keeper goal",
    "type": "particular",
    "event": "score",
    "condition": {
        "player": "goalkeeper"
    },
    "value_factor": "x2"
}


class MyTestCase(unittest.TestCase):

    def test_special_rule_condition_goalkeeper_score_is_double(self):
        rule = SpecialRule("keeper_goal", "score", RuleCondition(ConditionType.player, "goalkeeper"), 2)

        BATALLA = Player("Batalla", PlayerType.goalkeeper)

        score_event = Event("score", MatchTime("35"), BATALLA)

        rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score_event.score(), 2)


if __name__ == '__main__':
    unittest.main()

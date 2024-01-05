import unittest

from src.Event import Event
from MatchTime import MatchTime
from src.Player import PlayerType, Player
from src.RuleCondition import RuleCondition, ConditionType
from src.SpecialRule import SpecialRule


class MyTestCase(unittest.TestCase):

    def test_special_rule_condition_goalkeeper_score_is_double(self):
        rule = SpecialRule("keeper_goal", "score", RuleCondition(ConditionType.player, "goalkeeper"), 2)

        BATALLA = Player("Batalla", PlayerType.goalkeeper)

        score_event = Event("score", MatchTime("35"), BATALLA)

        rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score_event.score(), 2)


if __name__ == '__main__':
    unittest.main()

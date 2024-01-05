import unittest

from Event import Event
from MatchTime import MatchTime
from Player import Player, PlayerType
from RuleCondition import RuleCondition, ConditionType

from SingleRule import SingleRule
from WrongConditionException import WrongConditionException

BATALLA = Player("Batalla", PlayerType.goalkeeper)
BARRIOS = Player("Sofi", PlayerType.regular)


class MyTestCase(unittest.TestCase):
    def test01_fail_if_at_least_condition(self):
        self.assertRaises(WrongConditionException, lambda: SingleRule("rule", "score", "at_least", 1))

    def test02_condition_after_time_is_met(self):
        rule = SingleRule("after_time", "score", RuleCondition(ConditionType.afterTime, MatchTime("25")), 2)
        score_event = Event("score", MatchTime("35"), BARRIOS)

        score = rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score[0], 2)

    def test03_condition_after_time_in_extra_time(self):
        rule = SingleRule("after_time", "score", RuleCondition(ConditionType.afterTime, MatchTime("45 +0")), 2)
        score_event = Event("score", MatchTime("45 +1"), BARRIOS)

        score = rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score[0], 2)

    def test04_condition_after_time_in_extra_time(self):
        rule = SingleRule("after_time", "score", RuleCondition(ConditionType.afterTime, MatchTime("45 +1")), 2)
        score_event = Event("score", MatchTime("45 +0"), BARRIOS)

        score = rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score[0], 0)

    def test05_condition_player_is_goalkeeper(self):
        rule = SingleRule("player", "score", RuleCondition(ConditionType.player, "goalkeeper"), 2)
        score_event = Event("score", MatchTime("30"), BATALLA)

        score = rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score[0], 2)

    def test06_condition_distance_more_than_25m(self):
        rule = SingleRule("long_goal", "score", RuleCondition(ConditionType.distance, "+25m"), 2)
        score_event = Event("score", MatchTime("10"), BARRIOS, "+25m")

        score = rule.apply(home_events=[score_event], away_events=[])

        self.assertEqual(score[0], 2)


if __name__ == '__main__':
    unittest.main()

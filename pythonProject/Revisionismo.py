import json
import sys
from pprint import pprint

from Event import Event
from MatchRule import MatchRule
from MatchTime import MatchTime
from Partido import Partido
from RuleCondition import RuleCondition
from SideRule import SideRule
from SingleRule import SingleRule
from Torneo import Torneo


def load_json(file):
    f = open(file)
    loaded_json = json.load(f)
    f.close()
    return loaded_json


def convert_partidos(partidos):
    processed_partidos = []
    for p in partidos:
        home = p.get('teams').get('home')
        away = p.get('teams').get('away')
        home_events = convert_events(p['home_events'])
        away_events = convert_events(p['away_events'])

        processed_partidos.append(Partido(home, away, home_events, away_events))
    return processed_partidos


def convert_events(events):
    processed_events = []
    for event in events:
        processed_events.append(
            Event(event['event'], MatchTime(event['time']), player=event.get('player', ""), obs=event.get('obs', "")))
    return processed_events


def convert_rules(rules):
    processed_rules = []
    for rule in rules:
        m = create_rule(rule)
        if m is not None:
            processed_rules.append(m)
    return processed_rules


def create_rule(rule):
    if rule["type"] == "match":
        return MatchRule(rule["name"], rule["event"], rule["points"])

    if rule["type"] == "single":
        key, value = rule["condition"].popitem()
        return SingleRule(rule["name"], rule["event"], RuleCondition(key, value), rule["bonus_points"])

    if rule["type"] == "side":
        return SideRule(rule["name"], rule["event"], rule["condition"]["at_least"], rule["bonus_points"])


if __name__ == '__main__':

    # if len(sys.argv) < 2:
    #    raise Exception("Not enough arguments")

    rules = []
    if len(sys.argv) > 2:
        # rules = load_json(sys.argv[2])
        rules = convert_rules(rules)

    rules = load_json('resources/rules.json')
    rules = convert_rules(rules)

    partidos = load_json('resources/partido.json')
    #    partidos = load_json(sys.argv[1])

    partidos = convert_partidos(partidos)

    summary = Torneo(partidos=partidos, rules=rules).summary()
    pprint(summary)

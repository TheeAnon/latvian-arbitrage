from django.core.management.base import BaseCommand
from arbitrage.models import ArbitrageOpportunity
from arbitrage.serializers import ArbitrageOpportunitySerializer
from decimal import Decimal
from django.utils import timezone
import itertools
from .tonybet import tonybet_tennis
from .x3000 import x3000_tennis
from .casino777 import casino777_tennis
from .spelet import spelet_tennis
# from .pafbet import pafbet_tennis


class Command(BaseCommand):
    help = 'Fetches data from APIs and calculates arbitrage opportunities'

    def handle(self, *args, **kwargs):
        tonybet_data = tonybet_tennis()
        casino777_data = casino777_tennis()
        x3000_data = x3000_tennis()
        spelet_data = spelet_tennis()
        # pafbet_data = pafbet_tennis()

        datasets = [
            # ('tonybet', tonybet_data),
            ('casino777', casino777_data),
            ('x3000', x3000_data),
            ('spelet', spelet_data),
            # ('pafbet', pafbet_data)
        ]

        # Generate all possible unique combinations of datasets
        combinations = itertools.combinations(datasets, 2)

        # Iterate over each combination and calculate arbitrage
        for (name1, data1), (name2, data2) in combinations:
            print(f"Calculating arbitrage for {name1} and {name2}")
            calculate_arbitrage(data1, data2)
        self.stdout.write(self.style.SUCCESS('Arbitrage calculation complete.'))


def calculate_arbitrage(site_one_data, site_two_data):
    arbitrages = 0
    matches = 0
    for site_one_event in site_one_data:
        for site_two_event in site_two_data:
            if site_one_event["category"] in site_two_event["category"] or site_two_event["category"] in site_one_event["category"]:
                # print(f"match {site_one_event["category"]} and {site_two_event["category"]} - {site_one_event["site_name"]} . {site_two_event["site_name"]}")
                if normalize_match_string(site_one_event["competitors"]) == normalize_match_string(site_two_event['competitors']):
                    # print(f"    match - {site_one_event["competitors"]} and {site_two_event["competitors"]}")
                    matches += 1
                    for site_one_bet_offer in site_one_event["bet_offers"]:
                        for site_two_bet_offer in site_two_event["bet_offers"]:
                            if site_one_bet_offer["bet_type"].lower().strip() == site_two_bet_offer["bet_type"].lower().strip():
                                if site_one_bet_offer["bet_type"] != "Winner":
                                    if str(site_one_bet_offer["odds_value"][0]).replace("+", '').replace("-",'') not in str(site_two_bet_offer["odds_value"][0]).replace("+", '').replace("-",'') or str(site_two_bet_offer["odds_value"][0]).replace("+", '').replace("-",'') not in str(site_one_bet_offer["odds_value"][0]).replace("+", '').replace("-",''):
                                        continue
                                print(f"matched bet type: {site_one_bet_offer} - {site_two_bet_offer}")
                                site_one_odds1 = Decimal(site_one_bet_offer['odds'][0])
                                site_one_odds2 = Decimal(site_one_bet_offer['odds'][1])
                                site_two_odds1 = Decimal(site_two_bet_offer['odds'][0])
                                site_two_odds2 = Decimal(site_two_bet_offer['odds'][1])


                                # Check both combinations
                                profit1 = calculate_arbitrage_profit(site_one_odds1, site_two_odds2)
                                profit2 = calculate_arbitrage_profit(site_two_odds1, site_one_odds2)

                                if profit1 is not None and profit2 is not None:
                                    found = False
                                    if profit1 < 0:
                                        sides = ["1", "2"]
                                        if site_one_bet_offer["bet_type"] != "Winner":
                                            sides = [site_one_bet_offer["odds_value"][0], site_two_bet_offer["odds_value"][1]]
                                        site_one_odds = round(site_one_odds1, 2)
                                        site_two_odds = round(site_two_odds2, 2)
                                        site_one_name = str(site_one_event["site_name"])
                                        site_one_link = str(site_one_event["site_link"])
                                        site_two_name = str(site_two_event["site_name"])
                                        site_two_link = str(site_two_event["site_link"])
                                        found = True
                                    if profit2 < 0:
                                        sides = ["2", "1"]
                                        if site_one_bet_offer["bet_type"] != "Winner":
                                            sides = [site_one_bet_offer["odds_value"][1], site_two_bet_offer["odds_value"][0]]
                                        site_one_odds = round(site_two_odds2, 2)
                                        site_two_odds = round(site_one_odds1, 2)
                                        site_one_name = str(site_two_event["site_name"])
                                        site_one_link = str(site_two_event["site_link"])
                                        site_two_name = str(site_one_event["site_name"])
                                        site_two_link = str(site_one_event["site_link"])
                                        found = True

                                    if found:
                                        result = post_arbitrage({
                                            'event_name': site_two_event["category"],
                                            'competitors': site_two_event["competitors"],
                                            'market': site_one_bet_offer["bet_type"],
                                            'sides': sides,
                                            'site_one_odds': site_one_odds,
                                            'site_two_odds': site_two_odds,
                                            'site_one_name': site_one_name,
                                            'site_one_link': site_one_link,
                                            'site_two_name': site_two_name,
                                            'site_two_link': site_two_link
                                        })
                                        arbitrages = arbitrages+1
                                        if result:
                                            print("Arbitrage posted successfully:", result)
                                        else:
                                            print("Failed to post data.")
                # else:
                #     print(f"    no match - {site_one_event["competitors"]} and {site_two_event["competitors"]}")
    print(f"{arbitrages} opportunities found in {matches} that matched")


def calculate_arbitrage_profit(odds_one, odds_two):
    try:
        return (1 / odds_one + 1 / odds_two) - 1
    except Exception as e:
        print(f"Could not calculate arbitrage profit: {e}")
        return None


def post_arbitrage(data):
    try:
        competitors = data["competitors"]
        site_one_name = data["site_one_name"]
        site_two_name = data["site_two_name"]
        market = data["market"]
        site_one_odds = data["site_one_odds"]
        site_two_odds = data["site_two_odds"]
        sides = data["sides"]

        # Mark all existing entries in the database as inactive and set their ended timestamp
        existing_entries = ArbitrageOpportunity.objects.filter(active=True)
        for entry in existing_entries:
            entry.active = False
            entry.ended = timezone.now()
            entry.save()

        # Check if the new entry already exists in the database
        try:
            existing_entry = ArbitrageOpportunity.objects.get(
                competitors=competitors,
                site_one_name=site_one_name,
                site_two_name=site_two_name,
                market=market
            )

            # If the existing entry is found and it was inactive, make it active again
            if not existing_entry.active:
                existing_entry.active = True
                existing_entry.ended = None

            # Update the odds and sides
            existing_entry.site_one_odds = site_one_odds
            existing_entry.site_two_odds = site_two_odds
            existing_entry.sides = sides

            serializer = ArbitrageOpportunitySerializer(existing_entry, data=data)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            else:
                print("Serializer errors:", serializer.errors)
            return None
        except ArbitrageOpportunity.DoesNotExist:
            # If the entry does not exist, create a new entry
            serializer = ArbitrageOpportunitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            else:
                print("Serializer errors:", serializer.errors)
            return None
    except Exception as e:
        print(f"Error posting data: {e}")
        return None


import re

def normalize_team_string(s):
    s = s.lower()
    s = s.strip()
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    players = sorted(s.split(' '))
    return ' '.join(players)

def normalize_match_string(match):
    teams = match.split(" vs. ")
    normalized_teams = [normalize_team_string(team) for team in teams]
    return " vs. ".join(sorted(normalized_teams))

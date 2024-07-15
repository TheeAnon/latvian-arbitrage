from django.core.management.base import BaseCommand
import requests
from datetime import datetime
from decimal import Decimal
from arbitrage.models import ArbitrageOpportunity

class Command(BaseCommand):
    help = 'Fetches data from APIs and calculates arbitrage opportunities'

    def handle(self, *args, **kwargs):
        tonybet_data = fetch_tonybet()
        casino777_data = fetch_casino777()
        x3000_data = fetch_x3000()
        calculate_arbitrage(tonybet_data, x3000_data)
        calculate_arbitrage(casino777_data, x3000_data)
        calculate_arbitrage(tonybet_data, casino777_data)

        self.stdout.write(self.style.SUCCESS('Arbitrage calculation complete.'))

def fetch_tonybet():
    urls = [
        'https://platform.tonybet.lv/api/event/list?isTopLive_eq=1&competitor2Id_neq=&competitor1Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&oddsExists_eq=1&main=1&limit=30&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=withMarketsCount&relations%5B%5D=tips&lang=en',
        'https://platform.tonybet.lv/api/event/list?competitor2Id_neq=&competitor1Id_neq=&oddsExists_eq=1&limit=50&main=1&status_in%5B%5D=0&relations%5B%5D=odds&relations%5B%5D=withMarketsCount&relations%5B%5D=result&relations%5B%5D=league&relations%5B%5D=competitors&relations%5B%5D=sportCategories&relations%5B%5D=tips&relations%5B%5D=additionalInfo&period=0&sportId_eq=3&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1010390&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1010370&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1038634&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1025629&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1009464&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1009241&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1009257&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1009271&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1009259&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1009265&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1068892&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1055797&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1029802&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1053251&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1012648&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1012560&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1011470&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1012194&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1011800&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1011470&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1011285&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1010682&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1010525&oddsExists_eq=1&lang=en',
        'https://platform.tonybet.lv/api/event/list?period=0&competitor1Id_neq=&competitor2Id_neq=&status_in%5B%5D=2&status_in%5B%5D=1&limit=150&main=1&relations%5B%5D=odds&relations%5B%5D=league&relations%5B%5D=result&relations%5B%5D=competitors&relations%5B%5D=withMarketsCount&relations%5B%5D=players&relations%5B%5D=sportCategories&relations%5B%5D=broadcasts&relations%5B%5D=statistics&relations%5B%5D=additionalInfo&relations%5B%5D=tips&leagueId_in%5B%5D=1010523&oddsExists_eq=1&lang=en'
    ]
    events = []

    for url in urls:
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'ok' and 'data' in data:
            for event in data['data']['items']:
                event_id = event["id"]
                league_id = event["leagueId"]
                home_team_id = event["competitor1Id"]
                away_team_id = event["competitor2Id"]
                date = event["time"]

                # Extracting odds
                odds = []
                if str(event_id) in data['data']['relations']['odds']:
                    for outcomes in data['data']['relations']['odds'][str(event_id)]:
                        if outcomes["id"] == 910:
                            for outcome in outcomes["outcomes"]:
                                odds.append(outcome["odds"])

                # Getting event name from league relations
                event_name = ""
                for league in data['data']['relations']['league']:
                    if league["id"] == league_id:
                        event_name = league["name"]

                # Getting team names from competitors relations
                home_team = away_team = ""
                for competitor in data['data']['relations']['competitors']:
                    if competitor["id"] == home_team_id:
                        home_team = competitor["name"]
                    if competitor["id"] == away_team_id:
                        away_team = competitor["name"]

                # Getting category name from sportCategories relations
                category = ""
                for sport_category in data['data']['relations']['sportCategories']:
                    if sport_category["id"] == event["sportCategoryId"]:
                        category = sport_category["name"]

                # Append event data
                if odds and len(odds) >= 2:
                    events.append({
                        'category': category,
                        'name': f"{home_team} vs. {away_team}",
                        'date': date,
                        'odds': odds,
                        'site_name': "tonybet",
                        'site_link': "https://tonybet.lv"
                    })

    return events

def fetch_x3000():
    urls = [
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/grand_slam/wimbledon_mixed_doubles/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720947882122&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/grand_slam/wimbledon/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720947865488&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/grand_slam/us_open_women/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720947855011&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/grand_slam/us_open/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720947822311&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp/bastad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948045762&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp/gstaad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948056228&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp/hamburg/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948127092&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta/palermo/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948199609&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta/contrexeville/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948188201&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta/budapest/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948177681&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta/bastad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948165179&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp/hamburg/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948127092&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/challenger/winnipeg/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948295710&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/challenger/trieste/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948287081&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/challenger/salzburg/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948278982&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/challenger/iasi/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948264556&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp_qual_/newport/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948410647&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp_qual_/hamburg/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948403341&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp_qual_/gstaad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948395391&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp_qual_/bastad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948370392&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/uriage/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948527139&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/umag/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948517954&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/the_hague/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948510300&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/roda_de_bara/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948502415&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/monastir/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948493241&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/lodz/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948483922&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/kursumlijska_banja/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948475964&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men/dallas/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948463257&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/tianjin/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948739463&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/the_hague/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948731390&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/rome/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948712228&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/monastir/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948703303&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/lujan/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948693601&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/kursumlijska_banja/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948685408&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/don_benito/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948676949&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/corroios-seixal/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948668436&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/buzau/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948661590&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/bissy-chambery/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948653965&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women/aschaffenburg/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948639764&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men_qual_/nakhon_si_thammarat/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948628678&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_men_qual_/esch-sur-alzette/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948617531&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta_qual_/palermo/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948927012&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta_qual_/budapest/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948918649&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/wta_doubles/bastad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948909499&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women_qual_/vitoria-gasteiz/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948901548&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women_qual_/nottingham/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948890694&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women_qual_/nakhon_si_thammarat/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948880739&useCombined=true&useCombinedLive=true'
    ]
    events = []

    for url in urls:
        response = requests.get(url)
        data = response.json()

        for event in data["events"]:
            home_team = event["event"]["homeName"]
            away_team = event["event"]["awayName"]
            date = event["event"]["start"]
            category = event["event"]["path"][1]["englishName"]
            odds = []
            for bet_offer in event["betOffers"]:
                if bet_offer["betOfferType"]["id"] == 2:
                    for outcome in bet_offer["outcomes"]:
                        try:
                            decimal_odds = fractional_to_decimal(outcome["oddsFractional"])
                            if decimal_odds is not None:
                                odds.append(decimal_odds)
                        except Exception:
                            continue

            # Append event data
            if odds and len(odds) >= 2:
                events.append({
                    'category': category,
                    'name': f"{home_team} vs. {away_team}",
                    'date': date,
                    'odds': odds,
                    'site_name': "x3000",
                    'site_link': "https://x3000.lv"
                })

    return events

def fetch_casino777():
    urls = [
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLivenow?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportId=68&showAllEvents=true',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportId=68&showAllEvents=false&count=50&hasStreaming=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=0&categoryids=542&champids=0&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=0&categoryids=542&champids=0&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=3158&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=17447&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=17450&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31918&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31917&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31766&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&culture=en-GB&numFormat=en&integration=casino777&langId=8&skinName=casino777&configId=1&countryCode=LV&deviceType=Desktop&champids=32074&group=ChampsWithoutDates&withLive=false&filterSingleNodes=2&sportids=68&period=periodall&outrightsDisplay=Outrights',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31929&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31895&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&culture=en-GB&numFormat=en&integration=casino777&langId=8&skinName=casino777&configId=1&countryCode=LV&deviceType=Desktop&champids=3038&group=ChampsWithoutDates&withLive=false&filterSingleNodes=2&sportids=68&period=periodall&outrightsDisplay=Outrights',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=16911&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=32012&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=32007&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31928&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31927&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31804&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=36895&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=36894&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=42379&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=32024&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=32021&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=32024&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=36858&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=37675&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=5171&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=17362&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=17063&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=47706&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=33655&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=44111&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31715&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=32559&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=42379&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=42379&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31422&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=31422&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=17466&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=17466&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=0&categoryids=0&champids=43338%2C33224%2C43323%2C33770%2C33087%2C33779%2C36419%2C31800&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=0&categoryids=0&champids=43338%2C33224%2C43323%2C33770%2C33087%2C33779%2C36419%2C31800&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=43338&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=43338&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=44279&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=44279&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLiveEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=18338&group=AllEvents&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&hasLiveStream=false',
        'https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=-180&langId=8&skinName=casino777&configId=1&culture=en-GB&countryCode=LV&deviceType=Desktop&numformat=en&integration=casino777&sportids=68&categoryids=0&champids=18338&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0'
    ]
    events = []

    try:
        for url in urls:
            response = requests.get(url)
            data = response.json()

            for item in data['Result']['Items']:
                for event in item['Events']:
                    if not event["IsVirtual"]:
                        event_name = event["CategoryName"]
                        name = event["Name"]
                        date = datetime.strptime(event["EventDate"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                        # is_live = event["IsLiveEvent"]
                        # live_current_time = event["LiveCurrentTime"] if is_live else None
                        market = "winner"
                        odds = []
                        for market in event['Items']:
                            if market['Name'] == 'Winner':
                                for selection in market['Items']:
                                    odds.append(selection["Price"])
                        if len(odds) > 1:
                            events.append({
                                'category': event_name,
                                'name': name,
                                'date': date,
                                # 'is_live': is_live,
                                # 'live_current_time': live_current_time,
                                'odds': odds,
                                'site_name': "casino777",
                                'site_link': "https://casino777.lv"
                            })
    except Exception:
        return events

    return events

def fetch_optibet():
    urls = [
        'https://sb-data.optibet.lv/lv/events/group/863,2089,2120,2149,8002,13051,14993,15054,18939,3344,3348,3354,3363,860,787,13520,17282,17328,17332,18677,18817,18947,17015,16114,2068,839,866/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ=='
    ]
    events = []

    try:
        for url in urls:
            response = requests.get(url)
            data = response.json()

            for item in data['Result']['Items']:
                for event in item['Events']:
                    if not event["IsVirtual"]:
                        event_name = event["CategoryName"]
                        name = event["Name"]
                        date = datetime.strptime(event["EventDate"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                        # is_live = event["IsLiveEvent"]
                        # live_current_time = event["LiveCurrentTime"] if is_live else None
                        market = "winner"
                        odds = []
                        for market in event['Items']:
                            if market['Name'] == 'Winner':
                                for selection in market['Items']:
                                    odds.append(selection["Price"])
                        if len(odds) > 1:
                            events.append({
                                'category': event_name,
                                'name': name,
                                'date': date,
                                # 'is_live': is_live,
                                # 'live_current_time': live_current_time,
                                'odds': odds,
                                'site_name': "casino777",
                                'site_link': "https://casino777.lv"
                            })
    except Exception:
        return events

    return events

def calculate_arbitrage(site_one_data, site_two_data):
    arbitrages = 0
    for site_one_event in site_one_data:
        for site_two_event in site_two_data:
            if site_one_event["category"] == site_two_event["category"]:
                if site_one_event["name"] == site_two_event['name']:
                    site_one_odds1 = Decimal(site_one_event['odds'][0])
                    site_one_odds2 = Decimal(site_one_event['odds'][1])
                    site_two_odds1 = Decimal(site_two_event['odds'][0])
                    site_two_odds2 = Decimal(site_two_event['odds'][1])

                    # Check both combinations
                    profit1 = calculate_arbitrage_profit(site_one_odds1, site_two_odds2)
                    profit2 = calculate_arbitrage_profit(site_two_odds1, site_one_odds2)

                    if profit1 is not None and profit2 is not None:
                        if profit1 < 0:
                            post_arbitrage({
                                'event_name': site_two_event["category"],
                                'competitors': site_two_event["name"],
                                'market': "Winner",
                                'sides': ["1", "2"],
                                'site_one_odds': site_one_odds1,
                                'site_two_odds': site_two_odds2,
                                'site_one_name':site_one_event["site_name"],
                                'site_one_link':site_one_event["site_link"],
                                'site_two_name':site_two_event["site_name"],
                                'site_two_link':site_two_event["site_link"]
                            })
                            arbitrages = arbitrages+1
                            print(f"Arbitrage opportunity found: {site_two_event["name"]} on {site_one_event['date']} with profit: {-profit1:.2f}")
                        if profit2 < 0:
                            result = post_arbitrage({
                                'event_name': site_two_event["category"],
                                'competitors': site_two_event["name"],
                                'market': "Winner",
                                'sides': ["2", "1"],
                                'site_one_odds': site_two_odds1,
                                'site_two_odds': site_one_odds2,
                                'site_one_name':site_two_event["site_name"],
                                'site_one_link':site_two_event["site_link"],
                                'site_two_name':site_one_event["site_name"],
                                'site_two_link':site_one_event["site_link"]
                            })
                            arbitrages = arbitrages+1
                            if result:
                                print("Arbitrage posted successfully:", result)
                            else:
                                print("Failed to post data.")
    print(f"{arbitrages} opportunities found")


def calculate_arbitrage_profit(odds_one, odds_two):
    try:
        return (1 / odds_one + 1 / odds_two) - 1
    except Exception as e:
        return None



def fractional_to_decimal(fractional_odds):
    try:
        numerator, denominator = map(int, fractional_odds.split('/'))
        decimal_odds = (numerator / denominator) + 1
        return decimal_odds
    except Exception as e:
        return None


def post_arbitrage(data):
    url = "http://localhost:8000/post_arbitrage/"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting data: {e}")
        return None
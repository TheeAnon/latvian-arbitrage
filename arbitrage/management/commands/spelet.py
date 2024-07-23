from datetime import datetime
import requests

def spelet_tennis():
    site_name = "spelet"
    site_link = "https://spelet.lv"
    urls = [
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=372&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=76871&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=77641&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=833361&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=833361&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=897,74013,74369,75789,231051,842057,843563,845181,847773,2728781&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=897,74013,74369,75789,231051,837933,842057,843563,845181,847773&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,897,74013,75789,231051,837933,842057,843563,845181,847773&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,74013,75789,231051,837933,842057,843563,845181,847773&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,74013,231051,837933,842057,843563,845181,847773&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,231051,837933,842057,843563,845181,847773&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,231051,837933,842057,843563,845181&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,837933,842057,843563,845181&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,837933,842057,843563&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,837933,842057&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298,837933&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=298&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955,1964966,2277001,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955,1964966,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955,2429671,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955,2429671&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,989493&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=51073,73975,843499,2425679,2728781&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,229233,848157,1802411,1803474,2426179,2426335,2426522,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,229233,846359,848157,1802411,1803474,2426179,2426335,2426522&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,229233,845189,846359,848157,1803474,2426179,2426335,2426522&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,229233,845189,846359,848157,2259963,2426179,2426335,2426522&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,226581,229233,845189,846359,848157,2259963,2426335,2426522&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,226581,229233,845189,846359,848157,2259963,2276820,2426522&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,226581,229233,845189,846359,848157,2259963,2276715,2276820&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79217,79491,226581,845189,846359,848157,2259963,2276715,2276820,2277001&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79491,226581,845189,846359,848157,1964966,2259963,2276715,2276820,2277001&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=226581,845189,846359,848157,1964966,2259963,2276715,2276820,2277001,2430134&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=226581,845189,846359,1964966,2259963,2276715,2276820,2277001,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=226581,845189,1964966,2259963,2276715,2276820,2277001,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=226581,990955,1964966,2259963,2276715,2276820,2277001,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=226581,988595,990955,1964966,2276715,2276820,2277001,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=988595,989493,990955,1964966,2276715,2276820,2277001,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=73975,988595,989493,990955,1964966,2276715,2277001,2429671,2430134,2729140&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=51073,73975,843499,2425679,2728781&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=51073,843499,2728781&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=843499,2728781&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=2728781&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=239119,405007,830441,840255,1290081,1342635,1785759,1971864,2575583,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=239119,405007,830441,840255,1290081,1342635,1785759,2575583,2607450,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=239119,405007,830441,1290081,1342635,1785759,2575583,2606918,2607450,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,239119,405007,830441,1290081,1342635,1785759,2606918,2607450,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,239119,830441,1290081,1342635,1785759,2606918,2607450,2726711,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,830441,1290081,1342635,1785759,2606918,2607450,2726711,2726793,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,830441,1271597,1290081,1342635,2606918,2607450,2726711,2726793,2729312&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,224619,830441,1271597,1290081,1342635,2606918,2607450,2726711,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,79207,224619,1271597,1290081,1342635,2606918,2607450,2726711,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,79207,224619,1271597,1290081,1513431,2606918,2607450,2726711,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,79207,224619,838179,1271597,1513431,2606918,2607450,2726711,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=56691,79207,224619,838179,1271597,1513431,2036113,2259683,2726711,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,79207,224619,838179,1271597,1513431,2036113,2259683,2726711,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,79207,224619,838179,1271597,1513431,2036113,2259683,2646200,2726793&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,79207,224619,838179,1271597,1513431,1802411,2036113,2259683,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,79207,838179,1513431,1802411,1803474,2036113,2259683,2426179,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,838179,1513431,1802411,1803474,2036113,2259683,2426179,2426335,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,838179,1802411,1803474,2036113,2259683,2426179,2426335,2426522,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,229233,1802411,1803474,2036113,2259683,2426179,2426335,2426522,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,79217,229233,1802411,1803474,2036113,2426179,2426335,2426522,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true',
        'https://iframe.spelet.lv/service-api/LineFeed/Get1x2_VZip?sports=4&champs=79201,79217,79491,229233,1802411,1803474,2426179,2426335,2426522,2646200&count=1000&lng=en&mode=4&country=102&partner=303&getEmpty=true&virtualSports=true'
    ]
    events = []

    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()

            if not data["Success"]:
                print(f"There was an error fetching the data in spelet on url {url}")
                continue

            for item in data['Value']:
                event_name = item["L"]
                competitors = f"{item["O1"]} vs. {item["O2"]}"
                date = datetime.fromtimestamp(item["S"]).strftime('%Y-%m-%d %H:%M:%S')
                bet_offers = []
                if item.get("E"):
                    bet_offers.append({
                        "bet_type": "Winner",
                        "odds": [item["E"][0]["C"], item["E"][1]["C"]],
                        "odds_value": []
                    })
                for market in item["AE"]:
                    if market["G"] == 2:
                        handicap_odds = []
                        handicap_odds_value = []
                        for odds in market["ME"]:
                            handicap_odds.append(odds["C"])
                            handicap_odds_value.append(odds["P"])
                        handicap_odds = group_into_pairs(handicap_odds)
                        handicap_odds_value = group_into_pairs(handicap_odds_value)
                        for index, handicap in enumerate(handicap_odds):
                            bet_offers.append({
                                "bet_type": "Game Handicap",
                                "odds": handicap,
                                "odds_value": handicap_odds_value[index]
                            })
                    if market["G"] == 17:
                        total_games_odds = []
                        total_games_odds_value = []
                        for odds in market["ME"]:
                            total_games_odds.append(odds["C"])
                            total_games_odds_value.append(odds["P"])
                        total_games_odds = group_into_pairs(total_games_odds)
                        total_games_odds_value = group_into_pairs(total_games_odds_value)
                        for index, total_games in enumerate(total_games_odds):
                            bet_offers.append({
                                "bet_type": "Total Games",
                                "odds": total_games,
                                "odds_value": total_games_odds_value[index]
                            })
                if len(bet_offers) > 1:
                    events.append({
                        'category': event_name,
                        'competitors': competitors,
                        'date': date,
                        # 'is_live': is_live,
                        # 'live_current_time': live_current_time,
                        'bet_offers': bet_offers,
                        'site_name': site_name,
                        'site_link': site_link
                    })
        except Exception as e:
            print(f"Error looping {site_name} url ({url}): {e}")
            continue

    return events


def group_into_pairs(arr):
    pairs = []
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            pairs.append([arr[i], arr[i + 1]])
    return pairs


# print(spelet_tennis())
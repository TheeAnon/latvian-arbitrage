from datetime import datetime
import requests

def pafbet_tennis():
    site_name = "pafbet"
    site_link = "https://pafbet.lv"
    urls = [
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1721563125169&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/event/live/open.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721571289635',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/grand_slam.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721571685028&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/atp/umag.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572115488&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/atp/newport.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572097037&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/atp/kitzbuhel.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572067983&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/atp/hamburg.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572020668&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/atp/bastad.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721571986241&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/grand_slam.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721571685028&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/grand_slam/us_open_women.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721571626842&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1721563125169&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/wta/palermo.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572341936&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/wta/iasi.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572306635&useCombined=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/paflv/listView/tennis/wta/budapest.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721572253262&useCombined=true'
    ]
    events = []

    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()

            data = data.get('events') or data.get('liveEvents')

            for event in data:
                event_name = event["event"]["path"][1]["englishName"]
                competitors = f"{event["event"]["homeName"]} vs. {event["event"]["awayName"]}"
                date = datetime.strptime(event["event"]["start"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                odds = []
                for market in event['betOffers']:
                    if market["criterion"]["id"] == 1001159551:
                        for outcome in market["outcomes"]:
                            try:
                                decimal_odds = fractional_to_decimal(outcome["oddsFractional"])
                                if decimal_odds is not None:
                                    odds.append(decimal_odds)
                            except Exception as e:
                                print(f"Couldn`t add odd: {e}")
                                continue
                if len(odds) > 1:
                    events.append({
                        'category': event_name,
                        'competitors': competitors,
                        'date': date,
                        'odds': odds,
                        'site_name': site_name,
                        'site_link': site_link
                    })
        except Exception as e:
            print(f"Error looping {site_name} url ({url}): {e}")
            continue

    return events


def fractional_to_decimal(fractional_odds):
    try:
        numerator, denominator = map(int, fractional_odds.split('/'))
        decimal_odds = (numerator / denominator) + 1
        return round(decimal_odds, 2)
    except Exception as e:
        print(f"Could not convert odds: {e}")
        return None


# print(pafbet_tennis())
import requests
from datetime import datetime


def x3000_tennis():
    site_name = "x3000"
    site_link = "https://x3000.lv"
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
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp_qual_/umag/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721565437609&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp_qual_/atlanta/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721565422914&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women_qual_/nakhon_si_thammarat/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948880739&useCombined=true&useCombinedLive=true',
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
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/itf_women_qual_/nakhon_si_thammarat/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948880739&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp/atlanta/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=3&ncid=1721630137933&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/grand_slam/wimbledon_mixed_doubles/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720947882122&useCombined=true&useCombinedLive=true',
        'https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/listView/tennis/atp/gstaad/all/matches.json?lang=en_GB&market=LV&client_id=2&channel_id=1&ncid=1720948056228&useCombined=true&useCombinedLive=true'
    ]
    events = []

    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()

            data = data.get("events") or data.get("liveEvents")
            # If events is None or empty, skip to the next iteration
            if not data:
                continue

            for event in data:
                try:
                    competitors = f"{event["event"]["homeName"]} vs. {event["event"]["awayName"]}"
                    date = datetime.strptime(event["event"]["start"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                    category = event["event"]["path"][1]["englishName"]
                    bet_offers = []
                    for bet_offer in event["betOffers"]:
                        odds = []
                        odds_value = []
                        bet_type = "Winner" if bet_offer["criterion"]["label"] == "Match Odds" else bet_offer["criterion"]["label"]
                        for outcome in bet_offer["outcomes"]:
                            odds.append(outcome["odds"]/1000)
                            odds_value.append(outcome.get("line")/1000 if outcome.get("line") else "")
                        bet_offers.append({
                            "bet_type": bet_type,
                            "odds": odds,
                            "odds_value": odds_value
                        })
                    # Append event data
                    if len(bet_offers) > 1:
                        events.append({
                            'category': category,
                            'competitors': competitors,
                            'date': date,
                            'bet_offers': bet_offers,
                            'site_name': site_name,
                            'site_link': site_link
                        })

                except Exception as e:
                    # print(f"Error looping match: {e}")
                    continue
        except Exception as e:
            print(f"Error looping {site_name} url ({url}): {e}")
            continue

    return events

# print(x3000_tennis())
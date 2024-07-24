import requests


def tonybet_tennis():
    site_name = "tonybet"
    site_link = "https://tonybet.lv"

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
        try:
            response = requests.get(url)
            data = response.json()

            if data['status'] == 'ok' and 'data' in data:
                try:
                    for event in data['data']['items']:
                        event_id = event["id"]
                        league_id = event["leagueId"]
                        home_team_id = event["competitor1Id"]
                        away_team_id = event["competitor2Id"]
                        date = event["time"]

                        # Extracting odds
                        bet_offers = []
                        if str(event_id) in data['data']['relations']['odds']:
                            for outcomes in data['data']['relations']['odds'][str(event_id)]:
                                try:
                                    if outcomes["id"] == 910:
                                        odds = []
                                        for outcome in outcomes["outcomes"]:
                                            odds.append(outcome["odds"])
                                        bet_offers.append({
                                            "bet_type": "Winner",
                                            "odds": odds,
                                            "odds_value": []
                                        })
                                    else:
                                        odds = []
                                        if not outcomes["specifiers"]:
                                            continue
                                        bet_type, odds_value = outcomes["specifiers"].split('=')
                                        if bet_type == "total":
                                            for outcome in outcomes["outcomes"]:
                                                odds.append(outcome["odds"])
                                            bet_offers.append({
                                                "bet_type": "Total Games",
                                                "odds": odds,
                                                "odds_value": [f"Over {odds_value}", f"Under {odds_value}"]
                                            })
                                        if bet_type == "hcp":
                                            if ":" in odds_value:
                                                odds_value, odds_value2 = odds_value.split(":")
                                            else:
                                                try:
                                                    odds_value2 = abs(float(odds_value)) if float(odds_value) < 0 else f"-{odds_value}"
                                                except Exception:
                                                    odds_value2 = odds_value
                                            for outcome in outcomes["outcomes"]:
                                                odds.append(outcome["odds"])
                                            bet_offers.append({
                                                "bet_type": "Handicap",
                                                "odds": odds,
                                                "odds_value": [odds_value, odds_value2]
                                            })
                                except Exception as e:
                                    print(f"Error adding outcome: {e}")
                        # Getting team names from competitors relations
                        home_team = away_team = ""
                        for competitor in data['data']['relations']['competitors']:
                            if competitor["id"] == home_team_id:
                                home_team = competitor["name"]
                            elif competitor["id"] == away_team_id:
                                away_team = competitor["name"]

                        # Getting category name from sportCategories relations
                        category = ""
                        for sport_category in data['data']['relations']['sportCategories']:
                            if sport_category["id"] == event["sportCategoryId"]:
                                category = sport_category["name"]

                        # Append event data
                        if len(bet_offers) > 0:
                            events.append({
                                'category': category,
                                'competitors': f"{home_team} vs. {away_team}",
                                'date': date,
                                'bet_offers': bet_offers,
                                'site_name': site_name,
                                'site_link': site_link
                            })
                except Exception as e:
                    print(f"error: {e}")
                    continue
        except Exception as e:
            print(f"Error looping {site_name} url ({url}): {e}")
            continue

    return events

# print(tonybet_tennis())
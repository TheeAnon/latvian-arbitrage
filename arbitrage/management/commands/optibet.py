from datetime import datetime
import requests


def optibet_tennis():
    site_name = "optibet"
    site_link = "https://optibet.lv"
    urls = [
        "https://sb-data.optibet.lv/lv/events/group/787/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/860/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/866/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/863/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/3344,3363,3354,3348/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/13051,5667,13055,2119,2089/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/19705/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/20761,15074,15933,13059,17355,20762,18677,17015,12919,20790,13017,18817,18997/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/766,3346,3347,2799,4231,4386,4787,5519,5612,8465,11606,13105,18614,17128,8416,15894,884/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ==",
        "https://sb-data.optibet.lv/lv/events/group/20719,20718/?domainId=0&gameTypes=-1&lsp=eyJ1cmwiOiJodHRwczovL3ZzdHJlYW1lci5lbmxhYnMuc2VydmljZXMiLCJwcm92aWRlcl9pZHMiOlsxLDJdfQ=="
    ]
    events = []

    try:
        for url in urls:
            response = requests.get(url)
            data = response.json()

            for item in data:
                try:
                    if item["player1"] != "" or item["player2"] != "":
                        live = item["lives"]
                        competitors = f"{item["player1"]["name"]} vs. {item["player2"]["name"]}"
                        event_name = ""
                        date = datetime.fromtimestamp(item["time"]).strftime('%Y-%m-%d %H:%M:%S')
                        for market in item['games']:
                            if market["eventId"] == 6440212 or market["type"] == "match":
                                market = "winner"
                                odds = []
                                for selection in market['odds']:
                                    odds.append(selection["value"])
                        for group in item['parentGroups']:
                            if group["parentId"] == 419:
                                event_name = group["name"]

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
                    print(f"Error looping item: {e}")
                    continue
    except Exception as e:
        print(f"Error: {e}")

    return events

print(optibet_tennis())
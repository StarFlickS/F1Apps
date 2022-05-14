import fastf1

def getGrandPrix():
    fastf1.Cache.enable_cache('cache') 
    session = fastf1.get_event_schedule(2022, include_testing=False, force_ergast=True)
    grand_prix_dict = {}
    for i in range(len(session)):
        grand_prix_dict[session["Location"][i]] = session["EventName"][i]
    
    return grand_prix_dict


def getRace_info_by_round(round: int):
    fastf1.Cache.enable_cache('cache')
    session = fastf1.get_event(2022, round)

    race_info = {
        "Round": session["RoundNumber"],
        "Country": session["Country"],
        "Location": session["Location"],
        "OfficialName": session["OfficialEventName"],
        "Date": session["EventDate"],
        "EventName": session["EventName"],
        "Format": session["EventFormat"],
        "ss1": session["Session1"],
        "ss1Date": session["Session1Date"],
        "ss2": session["Session2"],
        "ss2Date": session["Session2Date"],
        "ss3": session["Session3"],
        "ss3Date": session["Session3Date"],
        "ss4": session["Session4"],
        "ss4Date": session["Session4Date"],
        "ss5": session["Session5"],
        "ss5Date": session["Session5Date"]
    }

    return race_info

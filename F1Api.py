import fastf1

def getGrandPrix():
    fastf1.Cache.enable_cache('cache') 
    session = fastf1.get_event_schedule(2022)
    grand_prix_dict = {}
    for i in range(len(session)):
        grand_prix_dict[session["Country"][i]] = session["OfficialEventName"][i]
    
    return grand_prix_dict

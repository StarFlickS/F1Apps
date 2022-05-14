import fastf1

def getGrandPrix():
    fastf1.Cache.enable_cache('cache') 
    session = fastf1.get_event_schedule(2022, include_testing=False, force_ergast=True)
    grand_prix_dict = {}
    for i in range(len(session)):
        grand_prix_dict[session["Location"][i]] = session["EventName"][i]
    
    return grand_prix_dict

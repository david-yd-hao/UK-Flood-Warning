from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    """create list of ten stations with higher latest level"""
    list4 = stations_highest_rel_level(stations, 12)"""12 is used instead of 12 to account for the repeated stations which have to be removed"""
    for i in range(len(list4)):
        """use this piece of code to avoid stations with multiple latest levels (Hexham is an example)"""
        m=list4[i].latest_level
        if i< len(list4)-1:
            if m >= list4[i+1].latest_level:
                """return the 10 wanted stations in the form: name level"""
                print(list4[i].name, m)
            
                

        

run()
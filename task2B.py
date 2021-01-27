from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    for i in stations:
        my_list = stations_level_over_threshold(stations, 0.8)
    for i in my_list:
        "return in the form: name level"
        print(str(i[0]) + " " + str(i[1]))


run()

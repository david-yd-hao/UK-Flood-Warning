from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    list_of_rivers_by_station_number = rivers_by_station_number(stations, 10)
    print(list_of_rivers_by_station_number)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

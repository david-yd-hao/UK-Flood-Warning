from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():

    stations = build_station_list()
    names_of_stations = []

    stations_3 = stations_within_radius(stations, (52.2053, 0.1218), 10)
    for i in stations_3:
        """append names of stations within radius"""
        names_of_stations.append(i[0].name)
    """sort in alphabetical order"""
    names_of_stations.sort()

    print(names_of_stations)


run()
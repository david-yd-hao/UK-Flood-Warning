from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():

    My_list = []
    stations = build_station_list()
    list_tuple = []
    stations_2 = stations_by_distance(stations, (52.2053, 0.1218))
    for station_tuple in stations_2:
        list_tuple.append((station_tuple[0].name, station_tuple[0].town, station_tuple[1]))
    """append to the list the first and last ten tuples by distance"""
    My_list.append(list_tuple[:11])
    My_list.append(list_tuple[-10:])

    print(My_list)


run() 
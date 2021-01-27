from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    stations = build_station_list()
    list_of_rivers = rivers_with_station(stations)
    """print number of rivers with a station on them"""
    print(len(list_of_rivers))
    list_of_rivers.sort()
    """print the first ten rivers in alphabetical order"""
    print(list_of_rivers[:10])

    """print all the stations on one specific river"""
    my_dict = stations_by_river(stations)
    print(my_dict["River Aire"])
    print(my_dict["River Cam"])
    print(my_dict["River Thames"])


run()

"""Unit test for the geo module"""

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def test_rivers_by_station_number():
    # create station list
    stations = build_station_list()
    list_of_rivers_by_station_number = rivers_by_station_number(stations, 10)

    assert len(list_of_rivers_by_station_number) >= 10

    last_station_number = 100
    for i in range(len(list_of_rivers_by_station_number)):
        assert list_of_rivers_by_station_number[i][1] <= last_station_number
        last_station_number = list_of_rivers_by_station_number[i][1]

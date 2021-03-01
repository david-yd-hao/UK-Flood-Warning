from floodsystem.Analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.dates


def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_stations_tuple_list = stations_level_over_threshold(stations, 10)
    high_stations_list = []

    for stations_tuple in high_stations_tuple_list:
        high_stations_list.append(stations_tuple[0])

    severe_stations = []
    high_stations = []

    for s in high_stations_list:
        dt = 10
        dates, levels = fetch_measure_levels(s.measure_id, dt=timedelta(days=dt))
        poly_tuple = polyfit(dates, levels, 3)
        dates_float = matplotlib.dates.date2num(dates)
        if poly_tuple is None:
            print("invalid tuple")
        else:
            if poly_tuple[0][dates_float[-1]] >= poly_tuple[0][dates_float[0]]:
                severe_stations.append(s)

    print("Severe")
    for station in severe_stations:
        print(station.name)

    for station in high_stations_list:
        if station not in severe_stations:
            high_stations.append(station[0])

    print("High")
    for station in high_stations:
        print(station.name)

    moderate_stations = []
    stations_tuple_list2 = stations_level_over_threshold(stations, 3)
    for station in stations_tuple_list2:
        if station[0] not in high_stations_list:
            moderate_stations.append(station[0])

    print("Moderate")
    for station in moderate_stations:
        print(station.name)


run()

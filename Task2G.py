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

    # Creating a List of stations with current level threshold over 10
    for stations_tuple in high_stations_tuple_list:
        high_stations_list.append(stations_tuple[0])

    severe_stations = []
    high_stations = []

    # Creating Severe List (current level threshold over 10 and rising)
    for station1 in high_stations_list:
        dt = 10
        dates, levels = fetch_measure_levels(station1.measure_id, dt=timedelta(days=dt))

        # Check if levels is a valid float list
        for j in range(0, len(levels)):
            if not isinstance(levels[j], float):
                levels[j]=levels[j-1]

        poly_tuple = polyfit(dates, levels, 5)
        dates_float = matplotlib.dates.date2num(dates)

        # check if the polynomial fit is rising
        if poly_tuple[0][dates_float[-1]] - poly_tuple[0][dates_float[0]] >= 0.0:
            severe_stations.append(station1.name)

    print("Severe")
    print(severe_stations)

    # Creating High List (current level threshold over 10, excluding Severe)
    for station in high_stations_list:
        if station.name not in severe_stations:
            high_stations.append(station.name)

    print("High")
    print(high_stations)

    # Creating Moderate List (current level threshold over 3, excluding High and Severe)
    moderate_stations = []
    stations_tuple_list2 = stations_level_over_threshold(stations, 3)
    for station in stations_tuple_list2:
        if station[0] not in high_stations_list:
            moderate_stations.append(station[0].name)

    print("Moderate")
    print(moderate_stations)


run()

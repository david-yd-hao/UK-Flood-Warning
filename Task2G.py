from floodsystem.Analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.dates


def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_severe_stations_tuple_list = stations_level_over_threshold(stations, 10)
    high_severe_stations_list = []

    # Creating a List of stations with current level threshold over 10
    for stations_tuple in high_severe_stations_tuple_list:
        high_severe_stations_list.append(stations_tuple[0])

    # Creating list for all towns and stations
    severe_towns = []
    severe_stations = []
    high_stations = []
    high_towns = []
    moderate_stations = []
    moderate_towns = []
    low_stations = []
    low_towns = []

    # Complete Severe List (current level threshold over 10 and rising)
    for station1 in high_severe_stations_list:
        dt = 10
        dates, levels = fetch_measure_levels(station1.measure_id, dt=timedelta(days=dt))

        # Check if levels is a valid float list
        for j in range(0, len(levels)):
            if not isinstance(levels[j], float):
                levels[j] = levels[j - 1]

        poly_tuple = polyfit(dates, levels, 5)
        dates_float = matplotlib.dates.date2num(dates)

        # check if the polynomial fit is rising
        if poly_tuple[0][dates_float[-1]] - poly_tuple[0][dates_float[0]] >= 0.0:
            severe_stations.append(station1.name)
            if station1.town not in severe_towns:
                severe_towns.append(station1.town)

    print("Severe Towns")
    print(severe_towns)

    # Complete High List (current level threshold over 10, excluding Severe)
    for station2 in high_severe_stations_list:
        if station2.name not in severe_stations:
            high_stations.append(station2.name)
            if station2.town not in high_towns:
                high_towns.append(station2.town)

    print("High Towns")
    print(high_towns)

    # Complete Moderate List (current level threshold over 4, excluding High and Severe)
    moderate_stations_tuple_list = stations_level_over_threshold(stations, 4)
    for station3 in moderate_stations_tuple_list:
        if station3[0] not in high_severe_stations_list:
            moderate_stations.append(station3[0].name)
            if station3[0].town not in moderate_towns:
                moderate_towns.append(station3[0].town)

    print("Moderate Towns")
    print(moderate_towns)

    # Complete Low List (current level threshold over 2, excluding High, Severe and Moderate)
    low_stations_tuple_list3 = stations_level_over_threshold(stations, 2)
    for station4 in low_stations_tuple_list3:
        if station4[0] not in high_severe_stations_list and station4[0] not in moderate_stations:
            low_stations.append(station4[0].name)
            if station4[0].town not in severe_stations and station4[0].town not in high_towns:
                if station4[0].town not in moderate_towns and station4[0].town not in low_towns:
                    low_towns.append(station4[0].town)

    print("Low Towns")
    print(low_towns)


run()

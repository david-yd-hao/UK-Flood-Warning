from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    """create list of ten stations with higher latest level"""
    station_list = stations_highest_rel_level(stations, 5)
    for i in range(5):
        s = station_list[i]
        dt = 10
        dates, levels = fetch_measure_levels(s.measure_id, dt=timedelta(days=dt))
        plot_water_levels(s, dates, levels)


run()
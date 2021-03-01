from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    """create list of ten stations with higher latest level"""
    station_list = stations_highest_rel_level(stations, 5)
    for i in range(5):
        s = station_list[i]
        dt = 2
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))

        # Check if levels is a valid float list
        for j in range(0, len(levels)):
            if not isinstance(levels[j], float):
                levels[j] = levels[j-1]

        plot_water_level_with_fit(s, dates, levels, 4)


run()

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
import math

"""find the distance between the two points using the haversine formula"""


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371  # Radius of earth in kilometers
    return c * r


def stations_by_distance(stations, p):
    List_of_tuples = []
    List_of_distances = []
    Final_list = []
    for item in stations:
        distance = haversine(item.coord[0], item.coord[1], p[0], p[1])
        my_tuple = (item, distance)
        """create a sorted list of distances which is later used to sort our list of tuples"""
        List_of_distances.append(distance)
        List_of_distances.sort()
        List_of_tuples.append(my_tuple)
    """sort the list of tuples"""
    for i in List_of_distances:
        for k in List_of_tuples:
            if k[1] == i:
                Final_list.append(k)
    """return the list of sorted tuples"""
    return Final_list


def stations_within_radius(stations, centre, r):
    list_within_radius = []
    Final_list = stations_by_distance(stations, centre)
    "iterate through all the stations to find the ones within the radius"
    for element in Final_list:
        if element[1] <= r:
            list_within_radius.append(element)
    return list_within_radius


def rivers_with_station(stations):
    list_of_rivers = []
    """append every river in our list of stations"""
    for i in stations:
        """make sure the river is not already in the list"""
        if i.river not in list_of_rivers:
            list_of_rivers.append(i.river)
    return list_of_rivers


def stations_by_river(stations):
    list_of_rivers = rivers_with_station(stations)
    my_dict = {}
    for river in list_of_rivers:
        """create a new list which will be a value in our dictionary"""
        list2 = []
        for i in stations:
            """append to the list every station on one specific river"""
            if i.river == river:
                list2.append(i.name)
        my_dict[river] = list2
    return (my_dict)


def rivers_by_station_number(stations, N):
    # determines the N rivers with the greatest number of monitoring stations.
    # Return a list of (river name, number of stations) tuples, sorted by the number of stations.

    # Create a dictionary with key:river, value:number of list.
    stations_by_river_dict = stations_by_river(stations)
    rivers_station_num_dict = {}
    for key in stations_by_river_dict:
        rivers_station_num_dict[key] = len(stations_by_river_dict[key])

    # Determine Nth value in greatest number of monitoring stations.
    station_number_list = list(rivers_station_num_dict.values())
    station_number_list.sort(reverse=True)
    last_station_number = station_number_list[N - 1]

    # Make the output list of tuples.
    output_list = []
    for i in rivers_station_num_dict.keys():
        if rivers_station_num_dict[i] >= last_station_number:
            output_list.append((i, rivers_station_num_dict[i]))

    # Sort the output list of tuples.
    output_list.sort(key=lambda tup: tup[1], reverse=True)
    return output_list


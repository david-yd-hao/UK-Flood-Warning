def stations_level_over_threshold(stations, tol):

    dict1 = {}
    list1 = []
    final_list = []
    for station in stations:
        """make sure the latest level is a float"""
        if isinstance(station.latest_level, float) is True:
            if station.latest_level >= tol:
                """dictionary used to find the names after the values have been sorted"""
                dict1[station.latest_level] = station.name
                """create a list of levels which can be easily reverse sorted"""
                list1.append(station.latest_level)
                list1.sort(reverse=True)
    for i in list1:
        final_list.append((dict1[i], i))
        """return the wanted list of stations-levels"""
    return final_list


def stations_highest_rel_level(stations, N):
    list1 = []
    list2 = []
    list3 = []
    stations2 = stations_level_over_threshold(stations, 0)
    for i in stations2:
        """create list of station names"""
        list2.append(i[0])
    for i in list2:
        for k in stations:
            """create a list of stations (not just names)"""
            if k.name == i:
                list3.append(k)

    for i in range(0, N):
        list1.append(list3[i])

    return list1
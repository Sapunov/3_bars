"""
devmanorg bars
"""

from __future__ import print_function

import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath) as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    bigg_seats_num = data[0]["Cells"]["SeatsCount"]
    bigg_bar_name = data[0]["Cells"]["Name"]

    for bar in data:
        if bar["Cells"]["SeatsCount"] > bigg_seats_num:
            bigg_seats_num = bar["Cells"]["SeatsCount"]
            bigg_bar_name = bar["Cells"]["Name"]

    return bigg_bar_name


def get_smallest_bar(data):
    small_seats_num = data[0]["Cells"]["SeatsCount"]
    small_bar_name = data[0]["Cells"]["Name"]

    for bar in data:
        if bar["Cells"]["SeatsCount"] < small_seats_num:
            small_seats_num = bar["Cells"]["SeatsCount"]
            small_bar_name = bar["Cells"]["Name"]

    return small_bar_name


def _distance(a1, b1, a2, b2):
    return ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5


def get_closest_bar(data, longitude, latitude):
    closest_bar_cells = data[0]["Cells"]
    min_distance = _distance(
        closest_bar_cells["geoData"]["coordinates"][0],
        closest_bar_cells["geoData"]["coordinates"][1],
        longitude,
        latitude
    )
    for bar in data:
        _bar_distance = _distance(
            bar["Cells"]["geoData"]["coordinates"][0],
            bar["Cells"]["geoData"]["coordinates"][1],
            longitude,
            latitude
        )

        if _bar_distance < min_distance:
            min_distance = _bar_distance
            closest_bar_cells = bar["Cells"]

    return closest_bar_cells["Name"], closest_bar_cells["Address"]


if __name__ == '__main__':
    print (get_biggest_bar(load_data("moscow_bars.json")))
    print (get_smallest_bar(load_data("moscow_bars.json")))

    user_longitude = float(input("Longitude: "))
    user_latitude = float(input("Latitude: "))

    closest_bar = (get_closest_bar(
        load_data("moscow_bars.json"),
        user_longitude,
        user_latitude
    ))

    print (closest_bar[0])

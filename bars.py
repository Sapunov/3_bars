#!/usr/bin/env python3

import sys
import os
import json
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath) as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    _max = max(data, key=lambda it: it["Cells"]["SeatsCount"])

    return _max["Cells"]


def get_smallest_bar(data):
    _min = min(data, key=lambda it: it["Cells"]["SeatsCount"])

    return _min["Cells"]


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

    return closest_bar_cells


def _input_user_coordinates():
    long_lat = input("Enter your coordinates (longitude and latitude): ")
    return map(float, long_lat.split())

def _question_user(question):
    # print \n to separate question
    print()

    answer = ""
    while answer not in ("y", "n"):
        answer = input(question + " (y/n) ")

    return answer == "y"


def main():
    description = """Get the biggest and smallest bar in Moscow.
    Get the closest bar to any location.
    """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-f", "--filename",
        help="File with JSON data about Moscow bars",
        required=True
    )

    args = parser.parse_args()

    data = load_data(args.filename)
    if data is None:
        print ("File {0} does not exists".format(args.filename))
        sys.exit(1)

    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)

    print("BIGGEST BAR: {0} ({1} seats)".format(
        biggest_bar["Name"],
        biggest_bar["SeatsCount"]
    ))

    print("SMALLEST BAR: {0} ({1} seats)".format(
        smallest_bar["Name"],
        smallest_bar["SeatsCount"]
    ))

    if _question_user("Do you want to know the closest bar?"):
        correct = False
        while not correct:
            try:
                user_longitude, user_latitude = _input_user_coordinates()
                correct = True
            except ValueError:
                print("Incorrect input. Two numbers required")

        closest_bar = get_closest_bar(
            data,
            user_longitude,
            user_latitude
        )

        print ("\nCLOSEST BAR: {0} ({1})".format(
            closest_bar["Name"], closest_bar["Address"]))


if __name__ == "__main__":
    main()

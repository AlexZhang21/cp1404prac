"""
CP1404/CP5632 Practical
Wimbledon
Estimate: 30 minutes
Actual:   40 minutes
"""

import csv
from collections import Counter

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """create a define meaning."""
    wimbledon_data = get_data(FILENAME)
    champions = get_champions(wimbledon_data)
    countries = list(get_countries(wimbledon_data))
    countries.sort()

    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion}: {count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))


def get_data(filename):
    """Reads a CSV file and returns its data as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip header row
        data = [row for row in csv_reader]
    return data


def get_champions(wimbledon_data):
    """calculation the number of championships won by each player."""
    champions = Counter(row[CHAMPION_INDEX] for row in wimbledon_data)
    return champions


def get_countries(wimbledon_data):
    """read unique data from csv"""
    countries = set(row[COUNTRY_INDEX] for row in wimbledon_data)
    return countries


if __name__ == '__main__':
    main()


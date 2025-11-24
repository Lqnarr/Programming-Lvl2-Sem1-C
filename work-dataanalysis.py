# Data Analysis
# Author: Eric Gao
# Nov. 20th, 2025

# Analyse the data provided in class

import csv

file = open(
    "/Users/ericgao/Documents/Programming Lvl 2/Python/Data/NYC_Central_Park_weather_1869-2022.csv"
)
reader = csv.reader(file)

rows = list(file)
dataPoints = len(rows) - 1


def main():
    print("Number of data points:", dataPoints)
    print("Average rainfall:", countPrecip(), "in")
    print(
        "Average Minimum Temperature:",
        avgMinTemp(),
        "deg F or",
        ((avgMinTemp() - 32) * 5 / 9),
        "deg C",
    )
    print("Average Max June Temperature:", avgJuneMaxTemp(), "deg F")


def countPrecip():
    totalPrecip = 0.0

    for i in range(1, len(rows)):
        precip = rows[i].split(",")[1]
        if precip != "":
            totalPrecip += float(precip)

    return float(totalPrecip / dataPoints)


def avgMinTemp():
    totalMinTemp = 0.0

    for i in range(1, len(rows)):
        temp = rows[i].split(",")[4]
        if temp != "":
            totalMinTemp += float(temp)

    return float(totalMinTemp / dataPoints)


def avgJuneMaxTemp():
    totalJuneTemp = 0.0
    counter = 0

    for i in range(1, len(rows)):
        if rows[i].split("-")[1] == "06":
            counter += 1
            temp = rows[i].split(",")[5]
            if temp != "":
                totalJuneTemp += float(temp)

    return float(totalJuneTemp / counter)


if __name__ == "__main__":
    main()

import csv
import pandas
path = "Day 25/weather_data.csv"
""" with open("Day 25/weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        position = row[1]
        if position != "temp":
            temperatures.append(int(position))
     """

data = pandas.read_csv(path)
col2 = data["temp"]
print(data)
print(col2)
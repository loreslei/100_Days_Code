import pandas
path = "Day 25/weather_data.csv"
data = pandas.read_csv(path)
""" print(type(data))
print(type(data["temp"])) """


data_dict = data.to_dict()

#print(data_dict)

#Get Data in Columns
# 1 - data["temp"]
# 2 - data.temp

#Get Data in Row
# data[data.day == "Monday"]
#Get Row of the max temperature
print(data[data.temp == data.temp.max()])

""" temp_list = data["temp"].to_list()
total = len(temp_list)
average = sum(temp_list) / total
print(round(average))
print(round(data["temp"].mean()))
print(round(data["temp"].max())) """

#Convert monday temp to fahrenheit
monday = data[data.day == "Monday"]
temp_far = (monday.temp * 9/5) + 32
print(temp_far)


#Create a datafrane from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Day 25/new_data.csv")
print(data)

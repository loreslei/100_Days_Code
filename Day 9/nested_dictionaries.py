capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nested List in Dicitionary

#travel_log = {
#  "France": ["Paris", "London", "Madrid"],
#  "Germany": ["Berlin", "Munich", "Hamburg"]
#}

#print Lille

# print(travel_log["France"][1])   


#Nested list
nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][0])

travel_log = {
 "France": {"num_times_visited": 12,
            "cities_visited": ["Paris", "London", "Madrid"]
            },
 "Germany": {"num_times_visited": 5,
            "cities_visited": ["Berlin", "Munich", "Hamburg"]
            },
}

print(travel_log["France"]["cities_visited"][1])

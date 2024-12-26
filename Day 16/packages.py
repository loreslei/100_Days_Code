from prettytable import PrettyTable

table = PrettyTable()


table.field_names = ["Pokemon Name", "Type"]

#table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_row(["Bulbasaur", "Grass 🌱"])
table.add_row(["Pikachu", "Eletric 🔌"])
table.add_row(["Squirtle", "Water 💧"])
table.add_row(["Charmander", "Fire 🔥"])

table.align = "l"
print(table)
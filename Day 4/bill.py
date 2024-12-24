import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randomize1 = friends[random.randint(0, len(friends)-1)]
randomize2 = random.choice(friends)

print(randomize2)
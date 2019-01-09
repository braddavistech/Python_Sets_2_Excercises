showroom = {"Jeep", "Chevy", "Hummer", "Cadillac"}

print(showroom)
print("Length", len(showroom))
print("\n\n")

showroom.add("Jeep")
print(showroom)
print("\n\n")

expensive = {"Tesla", "Ferrari"}

showroom.update(expensive)
print(showroom)
print("Length", len(showroom))
print("\n\n")

showroom.discard("Cadillac")
print(showroom)
print("Length", len(showroom))
print("\n\n")

junkyard = {"Ford", "Pontiac", "VW", "Chevy", "Jeep"}
print("Junkyard", junkyard)
print("\n\n")

intersect = showroom.intersection(junkyard)
print("Intersection", intersect)
print("\n\n")

showroom = showroom.union(junkyard)
print("Showroom after bought junkyard", showroom)
print("\n\n")


junkyard.discard("Ford")
junkyard.discard("Pontiac")
junkyard.discard("VW")

print("Final showroom:", showroom)
print("Final junkyard:", junkyard)
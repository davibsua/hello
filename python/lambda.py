people = [
    {"name": "Harry", "house": "Gryffindor"}, 
    {"name": "Cho", "house": "Ravenclaw"}, 
    {"name": "Draco", "house": "Slythrein"}, 
]


people.sort(lambda person: person["name"])
print(people)
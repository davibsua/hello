# class Point(): 
#     def __init__(self, x, y): 
#         self.x = x
#         self.y = y

# x = float(input("X: "))
# y = float(input("Y: "))


# p = Point(x, y)
# print(p.x)
# print(p.y)

class Flight(): 
    def __init__(self, capacity): 
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name): 
        if not self.open_seats(): 
            return False
        self.passengers.append(name)
        return True
    

    def open_seats(self): 
        return self.capacity - len(self.passengers)

flight = Flight(3)


people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people: 
    succes = flight.add_passengers(person)
    if succes: 
        print(f"Added {person} to flight succesfuly")
    else: 
        print(f"No available seats for {person}")


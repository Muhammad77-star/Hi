class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
    
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (base_fare * 0.10)
        return total_fare
    bus = (50)
    print("Final fare for the bus ride is:", bus.fare(), "INR")
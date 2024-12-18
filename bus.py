class Vehicle(Bus):
    def __init__(self,seating capacity,charge ):
        self.seatingcapacity=seating capacity
        self.charge=charge

        Person.__init__(self,"seatingcapacity", "charge")


=Vehicle("Bus", 50, 500)
bus.display()
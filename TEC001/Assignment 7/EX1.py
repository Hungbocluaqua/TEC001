class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registnum = registration_number
        self.maxspeed = maximum_speed
        self.curspeed = 0
        self.traveldist = 0
    def accelarate(self, speedchange):
        self.curspeed = self.curspeed + speedchange
        if self.curspeed > self.maxspeed:
            self.curspeed = self.maxspeed
        if self.curspeed < 0:
            self.curspeed = 0
        print("Current speed: ", self.curspeed)
    def drive(self, hours):
        self.traveldist = self.traveldist + self.curspeed*hours
        print("Travelled distance: ", self.traveldist)

car1 = Car("ABC-123", 142)
print("Registration number: ", car1.registnum)
print("Maximum speed: ", car1.maxspeed)
print("Current Speed: ", car1.curspeed)
print("Travelled distances: ", car1.traveldist)

car1.accelarate(30)
car1.accelarate(70)
car1.accelarate(50)
car1.accelarate(-200)
car1.accelarate(70)
car1.drive(1.5)
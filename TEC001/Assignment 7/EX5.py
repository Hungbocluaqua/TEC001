import random
Cars = list()
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
    def drive(self, hours):
        self.traveldist = self.traveldist + self.curspeed*hours

for i in range(10):
   Cars.append(Car(f"ABC-{i}", random.randint(150,200)))

while True:
    for car in Cars:
        if car.traveldist >= 10000:
            break
        car.accelarate(random.randint(-10, 15))
        car.drive(1)
    else:
        continue
    break
for car in Cars:
    print("Registration number: ", car.registnum,"Maximum speed: ", car.maxspeed, "Current Speed: ", car.curspeed,"Travelled Distances: ", car.traveldist)
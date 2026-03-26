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


class Race:
    def __init__(self, Name, Distances, Carlist):
            self.name = Name
            self.dista = Distances
            self.carlist = Carlist
            self.race = False

    def hour_passes(self):
            while True:
                for car in self.carlist:
                    if car.traveldist >= self.dista:
                        break
                    car.accelarate(random.randint(-10, 15))
                    car.drive(1)
                else:
                    continue
                self.race = True
                break

    def print_status(self):
            for car in Cars:
                print("Registration number: ", car.registnum,"Maximum speed: ", car.maxspeed, "Current Speed: ", car.curspeed,"Travelled Distances: ", car.traveldist)

    def race_finished(self):
            print("Race is finished: ", self.race)

race1 = Race("Grand Demolition Derby", 8000, Cars)
race1.hour_passes()
race1.race_finished()
race1.print_status()
class Elevator:
    def __init__(self, bottomfloors, topfloors):
        self.floor = 0
        self.botfloors = bottomfloors
        self.topfloors = topfloors
    def go_to_floor(self, destination):
        while self.floor != destination:
            if self.floor < destination:
                self.floor_up()
            if self.floor > destination:
                self.floor_down()
    def floor_up(self):
        self.floor += 1
        print("floor: ", self.floor)
    def floor_down(self):
        self.floor -= 1
        print("floor: ", self.floor)

elevator1 = Elevator(123,213)
elevator1.go_to_floor(321)

class Building():
    def __init__(self, bottomfloors, topfloors, elevator_numbers):
        self.elevatorlist = []
        for i in range(elevator_numbers):
            self.elevatorlist.append(Elevator(bottomfloors, topfloors))
    def run_elevator(self, elevatornumber, destination):
        eleva = self.elevatorlist[elevatornumber]
        eleva.go_to_floor(destination)
    def fire_alarm(self):
        for ele in self.elevatorlist:
            ele.floor = 0
            print(ele.floor)

building1 = Building(123,423, 12)
building1.run_elevator(2, 321)
building1.fire_alarm()
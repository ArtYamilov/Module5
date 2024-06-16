class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        if self.numberOfFloors:
            print(floors)


floor_ = House()
print(floor_.numberOfFloors)

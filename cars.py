class Car(object):
    def __init__(self, model, colour, company, speedlimit):
        self.model=model
        self.colour=colour
        self.company=company
        self.speedlimit=speedlimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")


    def acclerate(self):
        print("Accelarating")

    def change_gear(self):
        print("Changed Gear")

Audi=Car("A6", "Red", "Audi", "Normal")
print(Audi.colour)
Audi.start()
Audi.stop()

    
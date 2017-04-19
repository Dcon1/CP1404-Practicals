from Prac07.car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    limo = Car(100)
    Car.add_fuel(limo, 20)
    limo.drive(115)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)
    print("Limo fuel =", limo.fuel)
    print("Limo odo =", limo.odometer)
    print("limo", limo)
    """I struggled to get the variable name limo in to string from car.py"""
main()

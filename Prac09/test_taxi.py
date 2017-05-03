from Prac09.taxi import Taxi
from Prac09.taxi import UnreliableCar

taxi_one = Taxi("Prius", 100)
taxi_one.drive(40)
print(taxi_one.get_fare())
taxi_one.start_fare()
taxi_one.drive(100)
print(taxi_one.get_fare())

unreliable_car = UnreliableCar("shit_box", 100, 1)
print(unreliable_car.drive(50))
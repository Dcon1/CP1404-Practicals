from Prac09.taxi import Taxi
from Prac09.taxi import UnreliableCar
#from Prac09.taxi import SilverService

taxi_one = Taxi("Prius", 100)
taxi_one.drive(40)
print(taxi_one.get_fare())
taxi_one.start_fare()
taxi_one.drive(100)
print(taxi_one.get_fare())

unreliable_car = UnreliableCar("shit_box", 100, 1)
print(unreliable_car.drive(50))

# silver_service = SilverService("Hummer", 10, 1)
# print(silver_service.add_fanciness(2))
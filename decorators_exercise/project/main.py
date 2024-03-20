from project.computer_store_app import ComputerStoreApp
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
print(computer_store.build_computer("Desktop Computer", "Apple", "Mahbook", "Intel Core i5-12600K", 64))
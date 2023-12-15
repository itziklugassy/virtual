from icecream import ic
import json

cars = []

def main():
    while True:
        ic("a - add your car")
        ic("d - delete your car")
        ic("p - print all cars")
        ic("s - save cars to JSON file")
        ic("x - exit")
        user_selection = input("Your selection: ")
           
        if user_selection == "a":
            car_brand = input("Enter car brand: ")
            cars.append(car_brand)
        elif user_selection == "d":
            car_to_delete = input("Enter car brand to delete: ")
            if car_to_delete in cars:
                cars.remove(car_to_delete)
                ic(f"Car {car_to_delete} deleted.")
            else:
                ic(f"Car {car_to_delete} not found in the list.")
        elif user_selection == "p":
            ic("Cars:", cars)
        elif user_selection == "s":
            with open('cars.json', 'w') as file:
                json.dump(cars, file)
            ic("Cars saved to cars.json")
        elif user_selection == "x":
            break

if __name__ == '__main__':
    main()

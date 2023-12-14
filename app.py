from icecream import ic

cars=[]

def main():
    while(True):
        ic("a- add your car")
        ic("p- print all cars")
        ic("x- exit")
        user_selection = input("your selection")
            
        if user_selection =="a":cars.append('red')
        if user_selection =="x":exit()
        if user_selection =="p":ic(cars)


if __name__== '__main__':
    main()

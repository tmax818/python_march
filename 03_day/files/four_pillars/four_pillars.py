##four pillars

## TODO benifits 


## TODO encapsulation


class CoffeeMachine:

    def __init__(self, type = "coffee machine"):
        self.type = type
        self.water_temp = 200

    def brew_coffee(self, beans = 'coffee beans'):
        print("coffee is ready")

    def clean(self):
        print("Someone left the wet filter in the machine over the weekend!!!")
        print("this is totally gross!!")

## TODO inheritance
class FrenchPress(CoffeeMachine):
    pass

## TODO polymorphism

class KCup(CoffeeMachine):

    def __init__(self, brand, type="coffee machine"):
        super().__init__(type)
        self.brand = brand

    def clean(self):
        print("throw the pod away")

class CappuccinoM( CoffeeMachine ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"

    def make_cappuccino(self,beans):
        super.brew_coffee(beans)
        print("Frothy!!!")

    def clean(self):
        print("Cleaning the froth!")

## TODO abstraction


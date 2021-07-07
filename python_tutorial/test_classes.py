# Object oriented programming.


# bicycle = color
#         wheel_types
#         sadle_type

# class Name(): blue print for objects
#   class variable
class Wheel:
    def __init__(self, shape, size) :
        self.shape = shape
        self.size =size



wheel20 =  Wheel('circular', 20)
wheel21 =  Wheel('octagon', 21)
class Bicycle:
    color = 'red'
    wheel_type = 'spoked'
    sadle_type = 'leather'
    wheel = None

    def bike_method(self):
        print(self)

    def set_color(self, color):
        self.color = color

    def print_color(self):
        print(self.color)
    
    def set_wheel(self, wheel):
        self.wheel = wheel 


    def __str__(self) :
        return   f"color : {self.color }  wheelType : {self.wheel_type}"

    # def fucntion(paremeters):
    #     code''

class Loan:
    def __init__(self, principal, interest, years=0):
        self.p = principal
        self.i = interest
        self.y = years

    def calculate_loan_payment(self):
        return self.p * (self.i / 100) * self.y
    
    def set_area(self, area):
        self.area = area
       



bike =  Bicycle()
bike2 =  Bicycle()
bike.set_color('yellow')
bike2.set_color('green')

bike.print_color()
bike2.print_color()
bike.set_wheel(wheel20)
print(bike.wheel)

bike.bike_method()
bike2.bike_method()


long_loan = Loan(1000, 10, years = 20 )
short_loan = Loan(1000, 10, years = 2)

long_loan_interest =  long_loan.calculate_loan_payment()
short_loan_interest =  short_loan.calculate_loan_payment()

print(long_loan_interest)
print(short_loan_interest)





"""
Create 3 different classes Length, Weight, and Time
Add respective attributes to store values.
Add static methods for conversion of different units.
Example:
Length: cm to inches, kilometer to miles, etc
Weight: KG to pounds, gram to Ounces, etc.
Time: seconds to hours, milliseconds to seconds
"""

class Length:
    # length = int(input("enter a length"))

    @staticmethod
    def cm_to_inches(value:float):
        print('the value of cm to inches is', value*0.393701)
    @staticmethod
    def km_to_miles(value:float):
        print('the value of km to miles is', value*0.621371)
class Weight:
    @staticmethod
    def kg_to_pounds(value:float):
        print('the value of Kg to pounds is', value*2.20462)
    @staticmethod
    def gm_to_ounces(value:float):
        print('the value of gm to ounces is',value*0.035274)
class Time:
    @staticmethod
    def sec_to_hours(value):
        print('the value of sec to hours is',value*0.000277778)
    @staticmethod
    def mil_to_sec(value):
        print('the value of miliseconds to seconds is',value*0.001)
length = float(input("enter a length"))
l = Length()
(l.cm_to_inches(length),l.km_to_miles(length))
Weight.kg_to_pounds(length)
Weight.gm_to_ounces(length)
(Time.sec_to_hours(length),Time.mil_to_sec(length))

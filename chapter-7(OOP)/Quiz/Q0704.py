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
        print(value*0.393701)
    @staticmethod
    def km_to_miles(value:float):
        print( value*0.621371)
class Weight:
    @staticmethod
    def kg_to_pounds(value:float):
        print( value*2.20462)
    @staticmethod
    def gm_to_ounces(value:float):
        print(value*0.035274)
class Time:
    @staticmethod
    def sec_to_hours(value):
        print(value*0.000277778)
    @staticmethod
    def mil_to_sec(value):
        print(value*0.001)

# l = Length()
# (l.cm_to_inches(Length.length),l.km_to_miles(Length.length))
length = int(input("enter a length"))
Weight.gm_to_ounces(length)
#
# w = Weight()
# (w.gm_to_ounces(Length.length))
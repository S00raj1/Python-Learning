# from feet to meter


class Length:
    def __init__(self,length):
        print(f"The length is initialized as {length} meter")
        self.length = length

    @classmethod
    def feet_to_meter(cls,length):
        return cls(length*0.3048)



l2 = Length.feet_to_meter(length=int(input("Enter length: ")))
print(l2.length)
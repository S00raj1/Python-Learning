class Parent:
    def __init__(self,caste):
        self.caste = caste
        # self.address = address

class child(Parent):
    def __init__(self,caste):
        super().__init__(caste=caste)
    def display_details(self):
        print("Child caste is :",self.caste)
        # print("Child address is :",self.address)


P =Parent(caste="Rajbanshi")
c = child(caste=P.caste)
c.display_details()




with open("Filevirus.exe", "w") as File:
    File.write("Hello world!!")
class Subject:
    def __init__(self,name) ->None:
        self.name = name
    def __str__(self)->str:
        return f"subject: {self.name}"
    def __repr__(self)->str:
        return self.__str__()
class Major:
    name = ''

    def __init__(self,name) ->None:
        self.name =name
        self.subjects = []

    def __add__(self, other: "Major"):
        sub = Major(f'{self.name} +{other.name}')
        sub.subjects = [*self.subjects,*other.subjects]
        return sub

s = Major('Science')
s.subjects.append(Subject('Physics'))
s.subjects.append(Subject('Chemistry'))

com = Major('Commerce')
com.subjects.append(Subject('Account'))
com.subjects.append(Subject('Principal of Management'))


maj = s + com

print(maj.name)
print(maj.subjects)
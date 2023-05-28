class Employee:
    _id:int = 10
    first_name:str = 'Cag'
    last_name:str = 'Tu'
    __project:str = 'Homaale'
    __department:str = 'Backend'
    __salary:int = 50000
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        print(self.first_name,self.last_name)

        pass

    # def _Construct(self,first_name,last_name):

em =Employee('Himal','uwbedi')


class Employee:
    # data members
    __name = ""
    __age = 0
    __salary = 0.0
    __gender = ""

    # Constructor
    def __init__(self, __name, __age, __salary, __gender):
        self.__name = __name
        self.__age = __age
        self.__salary = __salary
        self.__gender = __gender

    # Method

    def showDetails(self):
        print( self.__name )
        print( self.__age )
        print( self.__salary )
        print( self.__gender )


class Department( Employee ):
    __dept = ""

    def __init__(self,__name,__age,__sal,__gender,__dept):
        super().__init__(__name,__age,__sal,__gender)
        self.__dept=__dept

    def show_dept(self):
        print(f'Department: {self.__dept}')


num = int( input( "Employees You want To Enter?" ) )
lt = []

for i in range( num ):  
    name = input( "Name?" )
    age = int( input( "Age?" ) )
    sal = float( input( "Salary" ) )
    gen = input( "Gender" )
    dept=input("Department")
    lt.append( Department( name, age, sal, gen, dept ) )

for obj in lt:
    obj.showDetails()
    obj.show_dept()

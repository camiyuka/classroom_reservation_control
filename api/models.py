
class Classroom:
    def __init__(self, name='', is_available='', capacity='', number='', location='', available_periods='') -> None:
        self.name= name
        self.capacity= capacity
        self.number= number
        self.location= location
        self.available_periods = available_periods if available_periods is not None else [] 

    def __str__(self) -> str:
        return self.name
        


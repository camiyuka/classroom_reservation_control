
class Classroom:
    def __init__(self, name='', capacity='', number='', location='', available_periods='') -> None:
        self.name= name
        self.capacity= capacity
        self.number= number
        self.location= location
        self.available_periods = available_periods if available_periods is not None else [] 

    def __str__(self) -> str:
        return f"Name: {self.name}, Capacity: {self.capacity}, Number: {self.number}, Location: {self.location}, Available Periods: {self.available_periods}"


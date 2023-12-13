class oneWay():
    def __init__(self, voyager, departure, arrival, date, adults, minor, schedule, price):
        self.Voyager = voyager
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.adults = adults
        self.minor = minor
        self.schedule = schedule
        self.price = price
        
class roundTrip():
    def __init__(self, voyager, departure, arrival, date, adults, minor, schedule, price):
        self.Voyager = voyager
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.adults = adults
        self.minor = minor
        self.schedule = schedule
        self.price = price

class Voyager():
    def __init__(self, cpf, first_name, last_name, password):
        self.cpf = cpf
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
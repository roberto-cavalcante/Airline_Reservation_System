class oneWay():
    def __init__(self, voyager, departure, arrival, date, adults, minors, schedule, price):
        self.Voyager = voyager
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.adults = adults
        self.minors = minors
        self.schedule = schedule
        self.price = price
        
class roundTrip():
    def __init__(self, voyager, departure_depart, departure_return, arrival_depart, arrival_return, date_depart, date_return, adults, minors, schedule, price):
        self.Voyager = voyager
        self.departure_depart = departure_depart
        self.departure_return = departure_return
        self.arrival_depart = arrival_depart
        self.arrival_return = arrival_return
        self.date_depart = date_depart
        self.date_return = date_return
        self.adults = adults
        self.minors = minors
        self.schedule = schedule
        self.price = price

class Voyager():
    def __init__(self, cpf, first_name, last_name, password):
        self.cpf = cpf
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
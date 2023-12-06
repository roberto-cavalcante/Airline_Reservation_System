import json
from classes import *

JSON_FILE = 'C:/Users/Roberto José/Documents/Projeto_de_Software/Airline_Reservation_System/Python_Project/db.json'
voyager_list_file = open(JSON_FILE)
# with open(voyager_list_file) as f:
voyager_list = json.load(voyager_list_file)


def num_inp():
    return input('Please, choose a number: ')

def choose_D():
    print('Choose your Departure: ')
    print('Press 0 to "MCZ - Aeroporto Palmares, Maceió, Brasil"')
    print('Press 1 to "GRU - Aeroporto Internacional Guarulhos, São Paulo, Brasil"')
    print('Press 2 to "SDU - Aeroporto Santos Dumont, Rio de Janeiro, Brasil"')
    print('Press 3 to "CWB - Aeroporto Internacional Afonso Pena, Curitiba, Brasil"')
    d = int(num_inp())
    if d == 0:
        departure = "MCZ - Aeroporto Palmares, Maceió, Brasil"
    elif d == 1:
        departure = "GRU - Aeroporto Internacional Guarulhos, São Paulo, Brasil"
    elif d == 2:
        departure = "SDU - Aeroporto Santos Dumont, Rio de Janeiro, Brasil"
    elif d == 3:
        departure = "CWB - Aeroporto Internacional Afonso Pena, Curitiba, Brasil"
    return departure

def choose_A():
    print('Choose your Arrival: ')
    print('Press 0 to "MCZ - Aeroporto Internacional Zumbi Palmares, Maceió, Brasil"')
    print('Press 1 to "GRU - Aeroporto Internacional Guarulhos, São Paulo, Brasil"')
    print('Press 2 to "SDU - Aeroporto Santos Dumont, Rio de Janeiro, Brasil"')
    print('Press 3 to "CWB - Aeroporto Internacional Afonso Pena, Curitiba, Brasil"')
    a = int(num_inp())
    if a == 0:
        arrival = "MCZ - Aeroporto Internacional Zumbi Palmares, Maceió, Brasil"
    elif a == 1:
        arrival = "GRU - Aeroporto Internacional Guarulhos, São Paulo, Brasil"
    elif a == 2:
        arrival = "SDU - Aeroporto Santos Dumont, Rio de Janeiro, Brasil"
    elif a == 3:
        arrival = "CWB - Aeroporto Internacional Afonso Pena, Curitiba, Brasil"
    return arrival

def create_oneWay(Departure, Arrival, oneWay):
    Date = input('Please, type the date with the format (dd/mm/aaaa): ')
    Adults = input('How many adults are travelling? ')
    Adults = int(Adults)
    Minor = input('How many kids (under 17 years) are travellig? ')
    Minor = int(Minor)
    Price = (580 * Adults) + (130 * Minor)
    Schedule = planeSchedule()
    print()
    print('##################################################')
    print("These are the information about the flight so far:")
    print('Departure: ',Departure)
    print('Arrival: ', Arrival)
    print('Date: ', Date)
    print('Number of adults: ', Adults)
    print('Number of minors: ', Minor)
    print('Price: ', Price)
    print('Schedule: ', Schedule)
    print('##################################################')
    print()
    print("Would you like to book the flight you search?")
    print('Press 0 to yes')
    print('Press 1 to no')
    b = int(num_inp())
    if b == 0:
        v = create_Voyager(Voyager)
        db_voyager(v)
        o = oneWay(v, departure = Departure, arrival = Arrival, date = Date,
                    adults = Adults, minor = Minor, schedule = Schedule, price = Price)
    else:
        return

def planeSchedule():
    print('Choose the schedule:')
    print('Press 0 to 01:00')
    print('Press 1 to 03:45')
    print('Press 2 to 06:00')
    print('Press 3 to 08:45')
    print('Press 4 to 10:00')
    print('Press 5 to 15:45')
    print('Press 6 to 17:00')
    print('Press 7 to 21:00')
    print('Press 8 to 23:45')
    d = int(num_inp())
    if d == 0:
        pS = '01:00'
    elif d == 1:
        pS = '03:45'
    elif d == 2:
        pS = '06:00'
    elif d == 3:
        pS = '08:45'
    elif d == 4:
        pS = '10:00'
    elif d == 5:
        pS = '15:45'
    elif d == 6:
        pS = '17:00'
    elif d == 7:
        pS = '21:00'
    elif d == 8:
        pS = '23:45'
    return pS

def create_Voyager(Voyager):
    cpf = input('Type your CPF, please: ')
    first_name = input('Type your first name: ')
    last_name = input('Type your last name: ')
    password = input('Type your password: ')
    voyager = Voyager(cpf = cpf, first_name = first_name, last_name = last_name, password = password)
    # save_voyagers(voyager)
    return voyager

def db_voyager(Voyager):
    v = vars(Voyager)
    voyager_list['voyager'][Voyager.cpf] = v
    with open(JSON_FILE, 'w', encoding='utf-8') as db_voyager:
        json.dump(voyager_list, db_voyager)
    return Voyager
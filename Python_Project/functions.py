import secrets
import pickle
from classes import *
from database import *

def num_inp():
    return input('Please, choose a number: ')

def choose_D():
    print('Choose your Departure: ')
    cursor.execute("SELECT * FROM airports")
    airport = cursor.fetchall()
    for departure in airport:
        for i in range (2):
            print(f"{departure[i]}", end=" ")
        print()
    d = int(num_inp())
    cursor.execute(f"SELECT nome FROM airports WHERE id = {d}")
    dp = cursor.fetchall()
    return dp

def choose_A():
    print('Choose your Arrival: ')
    cursor.execute("SELECT * FROM airports")
    airport = cursor.fetchall()
    for arrival in airport:
        for i in range (2):
            print(f"{arrival[i]}", end=" ")
        print()
    a = int(num_inp())
    cursor.execute(f"SELECT nome FROM airports WHERE id = {a}")
    ar = cursor.fetchall()
    return ar

def date_oneWay():
    Date = input('Please, type the date with the format (dd/mm/yyyy): ')
    return Date

def date_depart():
    Date_depart = input('Please, type the date of depart with the format (dd/mm/yyyy): ')
    return Date_depart

def date_return():
    Date_return = input('Please, type the date of return with the format (dd/mm/yyyy): ')
    return Date_return

def num_Adults():
    Adults = input('How many adults are travelling? ')
    Adults = int(Adults)
    return Adults

def num_Minors():
    Minor = input('How many kids (under 17 years) are travellig? ')
    Minor = int(Minor)
    return Minor

def price_oneWay(a, m):
    a = a * 280
    m = m * 130
    price = a + m
    return price

def price_roundTrip(a, m):
    a = a * 560
    m = m * 260
    price = a + m
    return price

def planeSchedule():
    print('Choose the schedule:')
    cursor.execute("SELECT * FROM schedule")
    schedule = cursor.fetchall()
    for plane_S in schedule:
        for i in range (2):
            print(f"{plane_S[i]}", end=" ")
        print()
    d = int(num_inp())
    cursor.execute(f"SELECT hora FROM schedule WHERE id = {d}")
    pS = cursor.fetchall()
    # print(f"{pS[0]}")
    return pS

def print_summary(Departure, Arrival, Date, Date_depart, Date_return, Adults, Minors, Price, Schedule, s):
    print()
    print('--------------------------------------------------')
    print("These are the information about so far:")
    print(f"Departure: {Departure[0]}")
    print(f"Arrival: {Arrival[0]}")
    if s == 0:
        print('Date: ', Date)
    elif s == 1:
        print('Date of depart: ', Date_depart)
        print('Date of return: ', Date_return)
    print('Number of adults: ', Adults)
    print('Number of minors: ', Minors)
    print('Price: ', Price)
    print(f"Schedule: {Schedule[0]}")
    print('--------------------------------------------------')
    print()
    return

def create_search(Departure, Arrival):
    Adults = num_Adults()
    Minors = num_Minors()
    Date = 0
    Date_depart = 0
    Date_return = 0
    print('Is this a One Way search?')
    print('Press 0 to One Way')
    print('Press 1 to Round trip')
    s = int(num_inp())
    if s == 0:
        Date = date_oneWay()
        Price = price_oneWay(Adults, Minors)
    elif s == 1:
        Date_depart = date_depart()
        Date_return = date_return()
        Price = price_roundTrip(Adults, Minors)
    Schedule = planeSchedule()
    print_summary(Departure, Arrival, Date, Date_depart, Date_return, Adults, Minors, Price, Schedule, s)
    print("Would you like to book the flight you search?")
    print('Press 0 to yes')
    print('Press 1 to no')
    b = int(num_inp())
    if b == 0 and s == 0:
        create_oneWay(Departure, Arrival, Date, Adults, Minors, Schedule, oneWay)
    elif b == 0 and s == 1:
        create_roundTrip(Departure, Arrival, Date_depart, Date_return, Adults, Minors, Schedule, roundTrip)
    return

def create_oneWay(Departure, Arrival, Date, Adults, Minors, Schedule, oneWay):
    Price = price_oneWay(Adults, Minors)
    print('Press 0 if you do not registered')
    print('Press 1 if you have registered')
    c = int(num_inp())
    if c == 0:
        v = create_Voyager(Voyager)
        print_summary(Departure, Arrival, Date, 0, 0, Adults, Minors, Price, Schedule, 0)
        oneway = oneWay(voyager = v, departure = Departure, arrival = Arrival, date = Date, adults = Adults, minors = Minors, schedule = Schedule, price = Price)
        oneway_serialize = serialize(oneway)
        id_oneway = int(secrets.randbelow(2048))
        cursor.execute("INSERT or IGNORE INTO travel (id,objeto) VALUES (?,?)", (id_oneway,oneway_serialize,))
    elif c == 1:
        cpf = input('Please, type your CPF: ')
        cursor.execute(f"SELECT * FROM voyager WHERE cpf = {cpf}")
    else:
        return

def create_roundTrip(Departure, Arrival, Date_depart, Date_return, Adults, Minors, Schedule, roundTrip):
    Price = price_roundTrip(Adults, Minors)
    print('Press 0 if you do not registered')
    print('Press 1 if you have registered')
    c = int(num_inp())
    if c == 0:
        v = create_Voyager(Voyager)
        print_summary(Departure, Arrival, 0, Date_depart, Date_return, Adults, Minors, Price, Schedule, 1)
        roundtrip = roundTrip(voyager = v, departure_depart = Departure, departure_return = Arrival, arrival_depart = Arrival, arrival_return = Departure, date_depart = Date_depart, date_return = Date_return, adults = Adults, minors = Minors, price = Price, schedule = Schedule)
        roundtrip_serialize = serialize(roundtrip)
        id_roundtrip = int(secrets.randbelow(2048))
        cursor.execute("INSERT or IGNORE INTO travel (id,objeto) VALUES (?,?)", (id_roundtrip,roundtrip_serialize,))
    elif c == 1:
        cpf = input('Please, type your CPF: ')
        cursor.execute(f"SELECT * FROM voyager WHERE cpf = {cpf}")
    else:
        return

def create_Voyager(Voyager):
    cpf = input('Type your CPF, please: ')
    first_name = input('Type your first name: ')
    last_name = input('Type your last name: ')
    password = input('Type your password: ')
    voyager = Voyager(cpf = cpf, first_name = first_name, last_name = last_name, password = password)
    voyager_serialize = serialize(voyager)
    id_voyager = int(secrets.randbelow(2048))
    # print(id_voyager)
    cursor.execute("INSERT or IGNORE INTO voyager (id,objeto) VALUES (?,?)", (id_voyager,voyager_serialize,))
    return voyager

def serialize(classe):
    return pickle.dumps(classe)

def unserialize(classe):
    return pickle.loads(classe)
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
    print('Departure: ', Departure)
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
        print('Is this a One Way travel?')
        print('Press 0 to One Way')
        print('Press 1 to Round trip')
        a = int(num_inp())
        if a == 0:
            print('Please, press 0 if you do not registered')
            print('Please, press 1 if you have registered')
            c = int(num_inp())
            if c == 0:
                v = create_Voyager(Voyager)
                oneway = oneWay(voyager = v, departure = Departure, arrival = Arrival, date = Date, adults = Adults, minor = Minor, schedule = Schedule, price = Price)
                oneway_serialize = serialize(oneway)
                cursor.execute("INSERT or IGNORE INTO travel (objeto) VALUES (?)", (oneway_serialize,))
    else:
        return

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
    print(f"{pS[0]}")
    return pS

def create_Voyager(Voyager):
    cpf = input('Type your CPF, please: ')
    first_name = input('Type your first name: ')
    last_name = input('Type your last name: ')
    password = input('Type your password: ')
    voyager = Voyager(cpf = cpf, first_name = first_name, last_name = last_name, password = password)
    voyager_serialize = serialize(voyager)
    cursor.execute("INSERT or IGNORE INTO voyager (objeto) VALUES (?)", (voyager_serialize,))
    return voyager

def serialize(classe):
    return pickle.dumps(classe)

def unserialize(classe):
    return pickle.loads(classe)
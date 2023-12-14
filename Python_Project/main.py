from functions import *
from database import *

print('--------------------------------')
print()
print('Welcome to Maceio Air Taxi - MAT')
print()
print('--------------------------------')

while True:
    print()
    print('Press 0 to make a Flight Search')
    print('Press 1 to make a Booking Management')
    print('Press 2 to make a Online Check-in')
    print('Press 3 to make a Seat Selection')
    print('Press 4 to make a Baggage Information')
    print('Press 5 to make a Loyalty Program Management')
    print('Press 6 to make a Flight Status Updates')
    print('Press 7 to make a Special Requests')
    print('Press 8 to make a Multi-City Booking')
    print('Press 9 to make a Customer Support Interface')
    print('Press 10 to finish the program')
    choice = int(num_inp())
    print()
    
    if choice == 0:
        print('You choose to make a Flight Search')
        create_search(choose_D(),choose_A())
    else:
        print('This function is not implement yet')
        database.commit()
        database.close()
        break
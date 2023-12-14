import sqlite3

# Creating database
database = sqlite3.connect('C:/Users/Roberto José/Documents/Projeto_de_Software/Airline_Reservation_System/Python_Project/MAT.db')

# Cursor
cursor = database.cursor()

# Creating Operational Airports
airports = '''
    CREATE TABLE IF NOT EXISTS airports (
        id INTEGER PRIMARY KEY,
        nome TEXT
    )
'''
cursor.execute(airports)

# Insert the airports
cursor.execute("INSERT or IGNORE INTO airports (id, nome) VALUES (?, ?)", (0, 'MCZ - Aeroporto Palmares, Maceió, Brasil'))
cursor.execute("INSERT or IGNORE INTO airports (id, nome) VALUES (?, ?)", (1, 'GRU - Aeroporto Internacional Guarulhos, São Paulo, Brasil'))
cursor.execute("INSERT or IGNORE INTO airports (id, nome) VALUES (?, ?)", (2, 'SDU - Aeroporto Santos Dumont, Rio de Janeiro, Brasil'))
cursor.execute("INSERT or IGNORE INTO airports (id, nome) VALUES (?, ?)", (3, 'CWB - Aeroporto Internacional Afonso Pena, Curitiba, Brasil'))

# Creating Schedules
schedule = '''
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY,
        hora TEXT
    )
'''
cursor.execute(schedule)

# Insert schedule
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (0, '- 00:45'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (1, '- 01:30'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (2, '- 03:45'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (3, '- 06:30'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (4, '- 08:45'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (5, '- 10:00'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (6, '- 15:30'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (7, '- 19:00'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (8, '- 21:45'))
cursor.execute("INSERT or IGNORE INTO schedule (id, hora) VALUES (?, ?)", (9, '- 23:00'))



# Creating Voyager
voyager = '''
    CREATE TABLE IF NOT EXISTS voyager (
        id INTEGER PRIMARY KEY,
        objeto BLOB
    )
'''
cursor.execute(voyager)

# Creating Travel
travel = '''
    CREATE TABLE IF NOT EXISTS travel (
        id INTEGER PRIMARY KEY,
        objeto BLOB
    )
'''
cursor.execute(travel)
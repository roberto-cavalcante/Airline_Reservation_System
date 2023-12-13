import sqlite3

# Creating database
database = sqlite3.connect('C:/Users/Roberto José/Documents/Projeto_de_Software/Airline_Reservation_System/Python_Project/MAT.db')

# Cursor
cursor = database.cursor()

# Creating operational airports
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
import sqlite3
import os
import re
import datetime

def enable_foreign_keys(connection):
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS persone (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, sesso TEXT, codice_f TEXT, age DATE, luogo_nascita TEXT, residenza TEXT, CAP INTEGER, hair_color TEXT, eye_color TEXT, height_cm FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS entrate (person_id INTEGER, economic_id INTEGER PRIMARY KEY, Job TEXT, salario_lordo TIMESTAMP, IRPEF_dovuta TIMESTAMP, FOREIGN KEY(person_id) REFERENCES persone(id) ON DELETE CASCADE)")   #FOREIGN KEY(person_id) REFERENCES persone(id)
    cursor = connection.cursor()
    connection.commit()
   

def insert_data(connection):
    cursor = connection.cursor()

    #Table persone
    cursor.execute("INSERT INTO persone (name, surname, sesso, codice_f, age, luogo_nascita, residenza, CAP, hair_color, eye_color, height_cm) VALUES ('alice', 'marino', 'F', 'LCAMRN01C65H294S', '2001-03-25','Rimini','Riccione', '47838', 'nero','marroni', 160)")
    cursor.execute("INSERT INTO persone (name, surname, sesso, codice_f, age, luogo_nascita, residenza, CAP, hair_color, eye_color, height_cm) VALUES ('bob', 'ricci','M','BBORCC13S01C357E', '2013-11-01', 'Fano', 'Cattolica', '47841', 'biondo', 'azzurri', 180)")
    cursor.execute("INSERT INTO persone (name, surname, sesso, codice_f, age, luogo_nascita, residenza, CAP, hair_color, eye_color, height_cm) VALUES ('eve', 'costa', 'F','VEECST78L52F346W','1978-07-12', 'Bologna', 'Mondaino', '47836', 'castano', 'verdi', 170)")

    #Table economic
    cursor.execute("INSERT INTO entrate (person_id, job, salario_lordo, IRPEF_dovuta) VALUES (1, 'Giardiniere', '20k$', '23%')") #SOLO per questa riga per inserire la primary e la foreign ci ho messo 1 ora e 45 minuti
    cursor.execute("INSERT INTO entrate (person_id, job, salario_lordo, IRPEF_dovuta) VALUES (2, 'Medico', '31k$', '35%')")
    cursor.execute("INSERT INTO entrate (person_id, job, salario_lordo, IRPEF_dovuta) VALUES (3, 'Imprenditore', '120k$', '43%')")

    cursor = connection.cursor()
    connection.commit()





def select_data(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM persone")
    cursor.execute("SELECT * FROM entrate")

    rows = cursor.fetchall()
    print(type(rows))
    print("Data read from database")
    for row in rows:
        print(row)



if not os.path.exists("test.db"):
    print("creating test.db")
    connection = sqlite3.connect("test.db")
    create_table(connection)
    insert_data(connection)
else:
    print("test.db already exists")
    connection = sqlite3.connect("test.db")

select_data(connection)

enable_foreign_keys(connection)

#query = "INSERT INTO persone (name, surname, sesso TEXT, age, luogo_nascita TEXT, residenza TEXT, CAP INTEGER, hair_color, eye_color, height_cm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
while True:
    print("---------------------------------------------------------------------")
    print("Scegliere cosa eseguire:")
    print("1.Intera riga da Aggiungere dati nella tabella Persone")
    print("2.Dato singolo da aggiungere nella tabella Persone")
    print("3.Calcolo Codice Fiscale + inserimento nella tabella Persone")
    print("4.Eliminazione di una riga nella tabella 'persone', sincronizzata alla tabella 'entrate' ")#---------------->Lo provi, ci ho messo davvero tanto tempo
    print("5.Esci")
    print("---------------------------------------------------------------------")

    num= float(input("Inserire un comando seguendo l'indice indicato: "))
    
    if num==1:
      
        cursor = connection.cursor()  # Define the cursor variable
        #cursor.execute("ALTER TABLE persone ADD COLUMN sesso TEXT")
        valore_name = input("Inserisci il valore per nome: ")
        valore_surname = input("Inserisci il valore per cognome: ")
        valore_sesso = input("Inserisci il valore per sesso: ")
        valore_age = input("Inserisci il valore per data di nascita: ")
        valore_luogo_nascita = input("Inserisci il valore per luogo di nascita: ")
        valore_residenza = input("Inserisci il valore per residenza: ")
        valore_CAP = input("Inserisci il valore per CAP: ")
        valore_hair_color = input("Inserisci il valore per hair color: ")
        valore_eye_color = input("Inserisci il valore per eye color: ")
        valore_height_cm = input("Inserisci il valore per altezza: ")
        cursor.execute("INSERT INTO persone (name, surname, sesso, age, luogo_nascita, residenza, CAP, hair_color, eye_color, height_cm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (valore_name, valore_surname, valore_sesso, valore_age, valore_luogo_nascita, valore_residenza, valore_CAP, valore_hair_color, valore_eye_color, valore_height_cm))
        connection.commit()
        # codice_f #

    
    if num==2:
        cursor = connection.cursor()
        id_riga = input("Inserisci l'ID della riga da modificare: ")
        colonna = input("Inserisci il nome della colonna da modificare: ")
        nuovo_valore = input("Inserisci il nuovo valore: ")
        query = f'UPDATE persone SET {colonna} = ? WHERE id = ?'
        cursor.execute(query, (nuovo_valore, id_riga))
        connection.commit()

    if num==3:
        cursor = connection.cursor()
        id_riga = input("Inserisci l'ID della riga da modificare: ")

        #riga = cursor.fetchone()
        #if riga:
            #nome = riga[2]
            #surname = riga[3]                                            Per qualche motivo questa roba non funziona
            #date_of_birth = riga[6]
            #gender = riga[4]

                # Tabelle di conversione per mese e carattere di controllo
        months = {
                'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05',
                'H': '06', 'L': '07', 'M': '08', 'P': '09', 'R': '10',
                'S': '11', 'T': '12'
            }

        even_chars = {
                '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
            }

        odd_chars = {
                '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
                'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
                'K': 1, 'L': 0, 'M': 5, 'N': 7, 'O': 9, 'P': 13, 'Q': 15, 'R': 17, 'S': 19, 'T': 21,
                'U': 1, 'V': 0, 'W': 5, 'X': 7, 'Y': 9, 'Z': 13
            }

        def get_consonants(name):
                return ''.join([char for char in name if char.isalpha() and char not in 'AEIOU'])

        def get_vowels(name):
                return ''.join([char for char in name if char in 'AEIOU'])

        def code_name(name):
                name = re.sub(r'\W', '', name).upper()
                consonants = get_consonants(name)
                vowels = get_vowels(name)
                
                if len(consonants) >= 3:
                    return consonants[:3]
                else:
                    return (consonants + vowels + 'XXX')[:3]

        def code_surname(surname):
                surname = re.sub(r'\W', '', surname).upper()
                consonants = get_consonants(surname)
                vowels = get_vowels(surname)
                
                if len(consonants) >= 3:
                    return consonants[:3]
                else:
                    return (consonants + vowels + 'XXX')[:3]

        def code_date_of_birth(date_of_birth, gender):
                dob = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
                year = dob.strftime('%y')
                month = list(months.keys())[list(months.values()).index(dob.strftime('%m'))]
                day = dob.strftime('%d')
                
                if gender.upper() == 'F':
                    day = str(int(day) + 40)
                
                return year + month + day.zfill(2)

        def code_place_of_birth(place_code):
                return place_code.upper()

        def control_character(fiscal_code):
                total = sum(even_chars[fiscal_code[i]] if i % 2 else odd_chars[fiscal_code[i]] for i in range(15))
                return chr(total % 26 + ord('A'))

        def calculate_fiscal_code(name, surname, date_of_birth, gender, place_of_birth_code):
                surname_code = code_surname(surname)
                name_code = code_name(name)
                date_of_birth_code = code_date_of_birth(date_of_birth, gender)
                place_of_birth_code = code_place_of_birth(place_of_birth_code)
                
                partial_code = surname_code + name_code + date_of_birth_code + place_of_birth_code
                control_char = control_character(partial_code)
                
                return partial_code + control_char

            #Input
            #Non ce la faccio più
        nome = str(input("inserisci nome: "))
        surname = str(input("inserisci cognome: "))
        date_of_birth = (input("inserisci data di nascita: "))
        gender = str(input("inserisci sesso: "))
        place_of_birth_code = (input("Inserisci codice catastale: "))  # Codice del comune di Roma

        codice_fiscale = calculate_fiscal_code(nome, surname, date_of_birth, gender, place_of_birth_code)
        print(f"Codice Fiscale: {codice_fiscale}")        




       
        cursor.execute('UPDATE persone SET codice_f = ? WHERE id = ?', (codice_fiscale, id_riga))
        connection.commit() 


    if num==4: #Eliminazione di una riga
        
        def rinumera_id(connection, cursor, persone):
            cursor.execute(f'SELECT rowid, * FROM {persone}')
            rows = cursor.fetchall()

            for index, row in enumerate(rows, start=1):
                cursor.execute(f'UPDATE {persone} SET rowid = ? WHERE rowid = ?', (index, row[0]))

            connection.commit()


        def elimina_e_rinumerare(connection, cursor, id_riga):
            # Controllare se ci sono record correlati nella tabella entrate
            cursor.execute('SELECT economic_id FROM entrate WHERE person_id = ?', (id_riga,))
            entrate_correlate = cursor.fetchall()

            if entrate_correlate:
                # Eliminare i record correlati dalla tabella entrate
                for entrate_id_tuple in entrate_correlate:
                    entrate_id = entrate_id_tuple[0]  # Estraiamo il valore corretto dalla tupla
                    cursor.execute('DELETE FROM entrate WHERE economic_id = ?', (entrate_id,))
                connection.commit()

            # Eliminare la riga dalla tabella persone
            cursor.execute('DELETE FROM persone WHERE id = ?', (id_riga,))
            connection.commit()

            # Rinumerare gli ID nella tabella persone
            rinumera_id(connection, cursor, 'persone')

            # Rinumerare gli ID nella tabella entrate
            rinumera_id(connection, cursor, 'entrate')

            # Visualizzare la tabella aggiornata
            cursor.execute("SELECT * FROM persone")
            print(cursor.fetchall())
            cursor.execute("SELECT * FROM entrate")
            print(cursor.fetchall())

        # Connessione al database
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        # Chiedere all'utente l'ID della riga da eliminare
        id_riga = int(input("Inserisci l'ID della riga da eliminare: "))
        elimina_e_rinumerare(connection, cursor, id_riga)


    # Visualizzare la tabella aggiornata
        cursor.execute("SELECT * FROM persone")
        print(cursor.fetchall())


    if num==5:
        print("Sei uscito correttamente")
        break
                

import re
import datetime

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

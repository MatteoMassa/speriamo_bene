class Piatto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = True

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def is_disponibile(self):
        return self.disponibile

    def set_disponibile(self, disponibile):
        self.disponibile = disponibile

    def ordina(self):
        if self.disponibile:
            print("Il piatto", self.nome, "è stato ordinato.")
        else:
            print("Il piatto", self.nome, "non è disponibile.")

    def non_disponi(self):
        self.disponibile = False


        


def cerca_piatti(lista_piatti: list, nome: str = None, prezzo: float = None):
        risultati = []
        for piatto in lista_piatti:
            if nome and piatto.get_nome() == nome:
                risultati.append(piatto)
            elif prezzo and piatto.get_prezzo() == prezzo:
                risultati.append(piatto)
        return risultati


def calcola_conto(lista_piatti):
    totale = sum(piatto.get_prezzo() for piatto in lista_piatti)
    return totale

# Esempio di utilizzo


def stampa_menu(lista_piatti):
    for piatto in lista_piatti:
        print("Nome:", piatto.get_nome())
        print("Prezzo:", piatto.get_prezzo())
        print("Disponibile:", piatto.is_disponibile())
        print()



    





class Antipasto(Piatto):
    def __init__(self, nome, prezzo, ingrediente, porzione):
        self.ingrediente = ingrediente
        self.porzione = porzione
        super().__init__(nome, prezzo)
        
    def get_ingrediente(self):
        return self.ingrediente

    def set_ingrediente(self, ingrediente):
        self.ingrediente = ingrediente

    def get_porzione(self):
        return self.porzione

    def set_porzione(self, porzione):
        self.porzione = porzione

class Primo(Piatto):
    def __init__(self, nome, prezzo, tipo_pasta, sugo):
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo
        super().__init__(nome, prezzo)

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

    def get_sugo(self):
        return self.sugo

    def set_sugo(self, sugo):
        self.sugo = sugo

class Secondo(Piatto):
    def __init__(self, nome, prezzo, tipo_carne, cottura):
        self.tipo_carne = tipo_carne
        self.cottura = cottura
        super().__init__(nome, prezzo)

    def get_tipo_carne(self):
        return self.tipo_carne

    def set_tipo_carne(self, tipo_carne):
        self.tipo_carne = tipo_carne

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, cottura):
        self.cottura = cottura

class Dolce(Piatto):
    def __init__(self, nome, prezzo, tipo_dolce, calorie):
        self.tipo_dolce = tipo_dolce
        self.calorie = calorie
        super().__init__(nome, prezzo)

    def get_tipo_dolce(self):
        return self.tipo_dolce

    def set_tipo_dolce(self, tipo_dolce):
        self.tipo_dolce = tipo_dolce

    def get_calorie(self):
        return self.calorie

    def set_calorie(self, calorie):
        self.calorie = calorie


# Esempio di utilizzo
antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
esito = cerca_piatti(piatti_ordinati, nome="Bruschetta")

if not esito:
    print("Il piatto non è stato trovato.")
else:
    print("Il piatto è stato trovato.")

print(stampa_menu(piatti_ordinati))


conto = calcola_conto(piatti_ordinati)
print("Il totale del conto è:", conto)


class Dipendente:
    
    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio

    def get_nome(self):
        return self.nome

    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def get_stipendio(self):
        return self.stipendio

    def set_stipendio(self, nuovo_stipendio):
        self.stipendio = nuovo_stipendio

class Manager(Dipendente):

    def __init__(self, nome, stipendio, numero_team):
        self.numero_team = numero_team
        super().__init__(nome, stipendio)

    def get_team(self): # restituisce il numero del team
        return self.numero_team
    
    def set_team(self, nuovo_team): # aggiorna il numero del team
        self.numero_team = nuovo_team
        return self.get_team()

class Sviluppatore(Dipendente):

    def __init__(self, nome, stipendio, linguaggio):
        self.linguaggio = linguaggio
        super().__init__(nome, stipendio)

    def get_linguaggio(self):
        return self.linguaggio
    
    def set_linguaggio(self, nuovo_linguaggio):
        self.linguaggio = nuovo_linguaggio


# creazione oggetti
manager = Manager("Luca Verdi", 3000, 0)
print(manager.get_nome())
print(manager.get_team())
nuovo_numero_team = int(input("Inserisci il numero del team da aggiornare: "))
manager.set_team(3)
print(manager.get_team())
class MaterialeBiblioteca:
    def __init__(self, titolo, anno_pubblicazione):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = True

    #def __str__(self):
      #  return f"{self.titolo} di {self.disponibile} ({self.anno_pubblicazione})"

    #def __repr__(self):
     #   return f"{self.titolo} di {self.disponibile} ({self.anno_pubblicazione})"

    def get_titolo(self):
        return self.titolo
    
    def set_titolo(self, nuovo_titolo):
        self.titolo = nuovo_titolo

    def set_disponibile(self, nuovo_disp):
        self.disponibile = nuovo_disp
    
    def set_anno_pubblicazione(self, nuovo_anno_pubblicazione):
        self.anno_pubblicazione = nuovo_anno_pubblicazione

    # True se ho fatto il prestito, False altrimenti
    def prestito(self) -> bool:
        if self.disponibile == True: # se ho il materiale disponibile
            self.disponibile = False # lo rendo non disponibile
            return True # ho fatto il prestito
        else: # se il materiale non è disponibile
            return False # non ho fatto il prestito perché il materiale non è disponibile
    
    def restituzione(self) -> bool:
        if self.disponibile == False:
            self.disponibile = True
            return True
        else:
            return False
        
    def ricerca(self, parametro, valore):
        if parametro == "titolo":
            return self.titolo == valore
        elif parametro == "anno_pubblicazione":
            return self.anno_pubblicazione == valore
        else:
            return False
        
class Libro(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, autore, numero_pagine):
        self.autore = autore
        self.numero_pagine = numero_pagine
        super().__init__(titolo, anno_pubblicazione)
    
    def get_autore(self):
        return self.autore
    
    def set_autore(self, nuovo_autore):
        self.autore = nuovo_autore

    def get_numero_pagine(self):
        return self.numero_pagine
    
    def set_numero_pagine(self, nuovo_numero_pagine):
        self.numero_pagine = nuovo_numero_pagine

class Rivista(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, disponibile, numero_edizione, mese_pubblicazione):
        self.numero_edizione = numero_edizione
        self.mese_pubblicazione = mese_pubblicazione
        super().__init__(titolo, anno_pubblicazione, disponibile)

    def get_numero_edizione(self):
        return self.numero_edizione
    
    def set_numero_edizione(self, nuovo_numero_edizione):
        self.numero_edizione = nuovo_numero_edizione

    def get_mese_pubblicazione(self):
        return self.mese_pubblicazione
    
    def set_mese_pubblicazione(self, nuovo_mese_pubblicazione):
        self.mese_pubblicazione = nuovo_mese_pubblicazione
        
class DVD(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, disponibile, regista, durata):
        self.regista = regista
        self.durata = durata
        super().__init__(titolo, anno_pubblicazione, disponibile)
        
    def get_regista(self):
        return self.regista
    
    def set_regista(self, nuovo_regista):
        self.regista = nuovo_regista

    def get_durata(self):
        return self.durata
    
    def set_durata(self, nuova_durata):
        self.durata = nuova_durata
    



# Esempio di utilizzo
libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
print(libro.get_titolo())  # Output: Il Signore degli Anelli
print(libro.get_autore())  # Output: J.R.R. Tolkien
libro.prestito()
print(libro.is_disponibile())  # Output: False
libro.restituzione()
print(libro.is_disponibile())  # Output: True

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())  # Output: National Geographic
print(rivista.get_numero_edizione())  # Output: 5

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())  # Output: Inception
print(dvd.get_regista())  # Output: Christopher Nolan

# materiali = [libro, rivista, dvd]
# risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
# print(risultato.get_titolo())  # Output: Inception



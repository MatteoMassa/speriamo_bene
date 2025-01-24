 
class Film:
    def __init__(self, titolo, regista, anno, genere, valutazione):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.valutazione = valutazione

class Libreria:
    def __init__(self):
        self.films = []

    def aggiungi_film(self, film):
            self.films.append(film)

    def cerca_film_per_titolo(self, titolo) -> Film | None:
            for film in self.films:
                if titolo in film.titolo:
                    return film
            return None

    def cerca_film(self, key) -> Film | None:
            for film in self.films:
                if key in film.titolo or key in film.regista:
                    return film
            return None
                    
        
    def visualizza_films(self):
            for film in self.films:
                print(film.titolo)

    def valutazione_media(self):
            valutazioni = [film.valutazione for film in self.films]
            return sum(valutazioni) / len(valutazioni)

# creo Film
a = Film("Il Signore degli Anelli", "Peter Jackson", 2001, "Azione", 9)
b = Film("Harry Potter", "Chris Columbus", 2001, "Fantasy", 8)
# creo la Libreria
libreria = Libreria()
# aggiungo i film alla libreria
libreria.aggiungi_film(a)
libreria.aggiungi_film(b)
# cerco i film 
film_cercato = libreria.cerca_film("Harry Potter")
if film_cercato:
    print(f"Film trovato: {film_cercato.titolo} del regista {film_cercato.regista}")
else:
    print("Film non trovato")

film_cercato = libreria.cerca_film("Pippo")
if film_cercato:
    print(f"Film trovato: {film_cercato.titolo} del regista {film_cercato.regista}")
else:
    print("Film non trovato")
























#Gestione di una libreria di film. Ogni film ha un titolo, un regista, un anno di uscita, un genere (azione, commedia, drammatico, horror, documentario) e una valutazione (da 1 a 10). Il sistema deve permettere di:
#Aggiungere nuovi film alla libreria.
#Cercare film per titolo o regista.
#Visualizzare tutti i film presenti nella libreria.
#Calcolare la valutazione media dei film.
#Il sistema deve includere due classi principali:
#: rappresenta un singolo film nella libreria.
#: gestisce i film e le operazioni associate.

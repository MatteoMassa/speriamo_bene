class Libro:
    def __init__(self, _titolo, _autore, _pagine):
        self.titolo = _titolo
        self.autore = _autore
        self.pagine = _pagine

    def get_titolo(self):
        return self.titolo
    
    def set_titolo(self, _titolo):
        self.titolo = _titolo
        if not _titolo:
            raise ValueError("Il titolo non può essere una stringa vuota")
        self.titolo = _titolo

    def get_autore(self):
        return self.autore
    
    def set_autore(self, _autore):
        self.autore = _autore
        if not _autore:
            raise ValueError("L'autore non può essere una stringa vuota")
        self.autore = _autore

    def get_pagine(self):
        return self.pagine
    
    def set_pagine(self, _pagine):
        self.pagine = _pagine
        if _pagine < 0:
            raise ValueError("Il numero di pagine non può essere negativo")
from datetime import date

class Utente:
    def __init__(self, username: str, email: str, password: str, profileImage: str, bio: str):
        self.username = username
        self.email = email
        self.password = password
        self.profileImage = profileImage
        self.bio = bio
        self.fotos = []
        self.albums = []

    def carica_foto(self, foto):
        self.fotos.append(foto)

    def crea_album(self, album):
        self.albums.append(album)

class Foto:
    def __init__(self, id: int, title: str, description: str, uploadDate: date):
        self.id = id
        self.title = title
        self.description = description
        self.uploadDate = uploadDate
        self.commenti = []
        self.albums = []

    def aggiungi_commento(self, commento):
        self.commenti.append(commento)

    def aggiungi_album(self, album):
        self.albums.append(album)

class Album:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.fotos = []
        self.utenti = []

    def aggiungi_foto(self, foto):
        self.fotos.append(foto)

    def aggiungi_utente(self, utente):
        self.utenti.append(utente)

class Commento:
    def __init__(self, content: str, date: date, utente: Utente, foto: Foto):
        self.content = content
        self.date = date
        self.utente = utente
        self.foto = foto
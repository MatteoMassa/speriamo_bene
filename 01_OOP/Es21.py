class Camera:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponibile = True

    def prenota(self):
        if self.disponibile:
            self.disponibile = False
            return True
        return False

    def libera(self):
        self.disponibile = True

    def __str__(self):
        return f"Camera {self.numero} ({self.tipo}) - {'Libera' if self.disponibile else 'Occupata'}"


class Albergo:
    def __init__(self):
        self.camere = []

    def aggiungi_camera(self, numero, tipo):
        nuova_camera = Camera(numero, tipo)
        self.camere.append(nuova_camera)

    def prenota_camera(self, numero):
        for camera in self.camere:
            if camera.numero == numero:
                return camera.prenota()
        return False

    def visualizza_camere_disponibili(self):
        return [camera for camera in self.camere if camera.disponibile]

    def visualizza_prenotazioni(self):
        return [camera for camera in self.camere if not camera.disponibile]


# Esempio di utilizzo
albergo = Albergo()
albergo.aggiungi_camera(101, 'singola')
albergo.aggiungi_camera(102, 'doppia')


print("Camere disponibili:")
for camera in albergo.visualizza_camere_disponibili():
    print(camera)

print("\nPrenotazione camera 101:")
if albergo.prenota_camera(101):
    print("Prenotazione effettuata.")
else:
    print("Camera non disponibile.")

print("\nCamere disponibili dopo prenotazione:")
for camera in albergo.visualizza_camere_disponibili():
    print(camera)

print("\nPrenotazioni effettuate:")
for camera in albergo.visualizza_prenotazioni():
    print(camera)
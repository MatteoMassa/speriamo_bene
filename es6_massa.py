class Pagamento:
    def processa_pagamento(self):
        # Implementazione generica per il processamento del pagamento
        # ???????
        pass
        


#class Criptovaluta(Pagamento):
 #   def processa_pagamento(self):
  #      print("Elaborazione pagamento con Criptovalute")



class CartaDiCredito(Pagamento):
    def __init__(self,nome,numero_carta,scadenza_carta,cvc_carta):
        self.nome = nome
        self.numero_carta = numero_carta
        self.scadenza_carta = scadenza_carta
        self.cvc_carta = cvc_carta

    def processa_pagamento(self):
        # super().processa_pagamento()  # Richiama il metodo processa_pagamento della classe padre
        # Aggiungi qui la logica per gestire i pagamenti con carta di credito
        pass
        

class PayPal(Pagamento):

    def __init__(self,email,passw):
        self.email = email
        self.passw = passw

    def processa_pagamento(self):
        print("Elaborazione pagamento con PayPal per mario.rossi@example.com")
    


# Esempio di utilizzo
#main
def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123") # __init__
#pagamento_carta.processa_pagamento()
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento con Carta di Credito per Mario Rossi
effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento con PayPal per mario.rossi@example.com
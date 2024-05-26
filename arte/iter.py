while True:
    print("----------------------------------")
    print("Scegliere cosa calcolare:")
    print("1.Quadrato")
    print("2.Cubo")
    print("3.Esci")
    print("----------------------------------")

    num= float(input("Inserire un numero: "))

    if num==1:
        tot=num**2
        print("Il quadrato è: ", tot)

    if num==2:
        tot=num**3
        print("Il cubo è: ", tot)

    if num==3:
        tot=num**(1/2)
        print("La radice quadrata è: ", tot)

    if num==4:
        print("Sei uscito correttamente")
        break
	





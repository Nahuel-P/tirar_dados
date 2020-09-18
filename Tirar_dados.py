import random

desea_jugar=input("Desea tirar los dados? S/N: ")


while(desea_jugar.lower()=="s"):
    primer_dado = random.randint(1,6)
    segundo_dado = random.randint(1,6)
    suma_de_los_dados = primer_dado+segundo_dado

    print(f"El numero del primer dado es: {primer_dado}")
    print(f"El numero del segundo dado es: {segundo_dado}")
    print(f"La suma del primer y segundo dado es: {suma_de_los_dados}")
    desea_jugar=input("Desea jugar otra vez? S/N: ")

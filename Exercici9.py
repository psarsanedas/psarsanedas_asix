BYTE = 1024  # declarem la constant de PULGADA


def main():
    mb = int(input("Introdueix els MB: "))  # demanarem a l'usuari que posi per teclat els MB
    total = (
                        mb * BYTE) * BYTE  # calculara els bytes multiplican els mb * pulgada, i el resultat el tornarà a multiplicar per la constant BYTE
    print("El total en bytes son: ", total)  # mostrarà per pantalla el resultat final


if __name__ == "__main__":
    main()
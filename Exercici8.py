PULGADA = 1.0  # declarem la constant de PULGADA
PULGADA_CM = 2.54  # declarem la constant de PULGADA_CM


def main():
    centimeters = int(input("Introdueix els centímetres: "))  # farem un input per a que l'usuari posi els centimetres.
    total = centimeters * (
                PULGADA / PULGADA_CM)  # farem l'operació dels centimetres que a posat l'usuari per la divisió de pulgada i pulgada cm
    print("El total en pulgadas son: ", total)  # finalment, printarà per pantalla el resultat final


if __name__ == "__main__":
    main()
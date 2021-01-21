def main():
    number1 = int(input("Introdueix un valor: "))  # demana un valor per el primer numero
    number2 = int(input("Introdueix un valor: "))  # demana un valor per el segon numero
    number3 = int(input("Introdueix un valor: "))  # demana un valor per el tercer numero
    suma = 0
    if number1 == number2 and number3:  # amb el if, comprobem si els valors son iguals
        suma = number1 + number2 + number3  # si els valors son iguals fem la suma del nombres
        suma = suma * 3  # després, retornara el valor de la suma x3 ja que on iguals els 3 valors
    else:  # si no s'ha cumplit el if, farà el else.
        suma = number1 + number2 + number3  # només sumarà els 3 valors.
    print("El resultat final de la suma és: ", suma)  # retornarà la suma de tots els valors


if __name__ == "__main__":
    main()
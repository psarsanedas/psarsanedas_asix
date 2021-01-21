def main():
    suma = 0  # inicialitzem la variable suma amb un valor de 0
    i = 0
    for i in range(1, 11):  # el for serà de i a 10 que són els valors que ha d'introduïr l'usuari
        number = float(input('Introdueix un valor: '))  # demanarà un valor a l'usuari
        suma += number  # guardarà el valor de la suma
    suma = suma / i  # un cop el for a acabat, farem la mitjana.
    print("La mitjana dels valors introduïts és: ", suma)  # i per últim mostrarà la mitjana


if __name__ == "__main__":
    main()
    
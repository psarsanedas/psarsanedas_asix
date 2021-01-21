def main():
    inici = int(input('Introdueix un valor per el principi: '))  # demanem un valor per la variable inici
    final = int(input('Introdueix un valor per el final: '))  # demanem un valor per la variable final
    cont = 0  # introduim la variable cont amb un valor de 0.
    for i in range(inici, final + 1):  # el primer for serà el de i
        numbers = True
        for j in range(2, 11):  # el segon for serà per dividir tots els nombres entre els valor que a possat l'usuari
            if i == j:  # el primer if compara els dos valor, si son iguals, surt amb el break
                break
            elif i % j == 0:  # el elif divideix els dos valors, si es 0, posa el valor de false a la variable numbers
                numbers = False
            else:
                continue  # si no passa res, es continua
        if numbers:  # compara el valor de numbers amb true, si son iguals, el printara i passarà al següent.
            print(' ', i, end='')
            cont += 1
    print('\nHi han %u nombres prims.' % cont)  # finalment, mostrarà els valors que hi ha entre els nombres elegits


if __name__ == "__main__":
    main()
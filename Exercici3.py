def main():
    numero1 = int(input("Afegeix un numero per calcular el MCD: "))
    numero2 = int(input("Afegeix un altre numero per calcular el MCD: "))

    if numero1 < numero2:
        mcd = numero1
    else:
        mcd = numero2

    while True:
        if numero1 % mcd == 0 and numero2 % mcd == 0:
            print("El mcd es", mcd)
            break
        else:
            mcd -= 1


if __name__ == "__main__":
    main()
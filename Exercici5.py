def main():
    numero = int(input("Introdueix un numero: "))
    print("Has seleccionat la taula del ", numero)
    for i in range(0,11):
        resultado = i*numero
        print(("%d x %d = %d")%(numero, i, resultado))

if __name__ == "__main__":
    main()

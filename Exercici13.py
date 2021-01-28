def main():
    num1 = int(input("Introdueix el primer número: "))
    while num1 < 0:
        num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    while num2 < 0:
        num2 = int(input("Introdueix el segon número: "))
    num1, num2 = num2, num1
    print("Els valors s'han intercanviat, el resultat es el següent: ", num1, num2)

if __name__ == "__main__":
    main()
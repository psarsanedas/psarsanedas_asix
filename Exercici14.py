def main():
    numlist = []
    auxnum = 0
    maxnumbers = int(input("Quants valors vols introduir?: "))
    while maxnumbers < 0:
        maxnumbers = int(input("Quants valors vols introduir?: "))
    for i in range(maxnumbers):
        num = int(input("Introdueix un número: "))
        numlist.append(num)
        auxnum += num
    print("\nAquesta es la suma de tots els valors introduits: ", auxnum)


if __name__ == "__main__":
    main()
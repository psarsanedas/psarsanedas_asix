def main():
    segons = int(input("Escriu el total de segons: "))

    dies = segons // (24 * 60 * 60)
    segons = segons % (24 * 60 * 60)
    hores = segons // (60 * 60)
    segons = segons % (60 * 60)
    minuts = segons // 60
    segons = segons % 60
    print("Díes: {} - Hores: {} - Minuts: {} - Segons: {}".format(dies, hores, minuts, segons))


if __name__ == "__main__":
    main()
def main():
    number = int(input("Introdueix un valor entre 1 i 10: "))  # demana un valor entre el 1 i el 10
    while number < 1 or number > 10:  # validem que posi be els valors
        number = int(input("Introdueix un valor entre 1 i 10: "))  # demana un valor entre el 1 i el 10


if __name__ == "__main__":
    main()
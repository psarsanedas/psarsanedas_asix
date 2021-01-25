TOTAL = 15

def main():
    auxaprovat = 0
    auxsuspes = 0
    aprovat = 0
    suspes = 0
    i = 0

    for i in range(TOTAL):  # Holaa
        notes = int(input("Introdueix les notes: "))
        while notes < 0 or notes > 10:
            notes = int(input("Introdueix les notes: "))
        if notes > 4:
            aprovat = aprovat + notes
            auxaprovat += 1
        else:
            suspes = suspes + notes
            auxsuspes += 1
    aprovat = aprovat / auxaprovat
    suspes = suspes / auxsuspes
    print("La mitjana d'aprovats és: ", aprovat)
    print("La mitjana de suspesos és: ", suspes)
    print("La quantitat d'aprovats és: ", auxaprovat)
    print("La quantitat de suspesos és: ", auxsuspes)


if __name__ == "__main__":
    main()
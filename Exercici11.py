TOTAL = 15

def main():
    auxaprovat = 0
    auxsuspes = 0
    aprovat = 0
    suspes = 0
    i = 0

    for i in range(TOTAL):
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
    print(f"\nLa mitjana d'aprovats és: {aprovat:.2f}")
    print(f"La mitjana de suspesos és: {suspes:.2f}")
    print("\nLa quantitat d'aprovats és: ", auxaprovat)
    print("La quantitat de suspesos és: ", auxsuspes)


if __name__ == "__main__":
    main()
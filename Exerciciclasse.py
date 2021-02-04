def main():
    x = 0
    j = 0
    i = 0
    aula = {}
    nom_aula = {}
    ip = {}
    nombre_pcs = {}
    maxnum = int(input("Quants registres vols introduir?: "))
    for x in range(maxnum):
        print("\nIntrodueix els valor per el registre", x)
        aula[x] = int(input("Quina aula és?: "))
        while 1 < aula[x] > 50:
            aula[x] = int(input("Quina aula és?: "))
        nom_aula[x] = str(input("Quin es el nom de l'aula?: "))
        ip[x] = str(input("Quina és l'IP de l'aula?: "))
        nombre_pcs[x] = int(input("Quin es el nombre de PCs de l'aula?: "))
        while 1 < nombre_pcs[x] > 20:
            nombre_pcs[x] = int(input("Quin es el nombre de PCs de l'aula?: "))
    print("\n")

    aules = {
        "aula": aula,
        "nom_aula": nom_aula,
        "ip": ip,
        "nombre_pcs": nombre_pcs
    }
    for i in aules.items():
        print(i)

if __name__ == "__main__":
    main()
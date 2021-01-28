MAXNUM = 10

def main():
    numlist = []
    numpar = []
    numimp = []
    par = 0
    imp = 0
    i = 1

    for i in range(MAXNUM):
        num = int(input("Introdueix un número del 0 al 10: "))
        numlist.append(num)
        while numlist[i] < 0 or numlist[i] > 10:
            numlist[i] = int(input("Introdueix números del 0 al 10: "))
    for i in range(MAXNUM):
        if numlist[i] % 2 == 0:
            numpar.append(numlist[i])
            par += 1
        else:
            numimp.append(numlist[i])
            imp += 1
    print("\nEls nombres parells són: ")
    for i in range(par):
        print(numpar[i], end=" ")
    print("\n\nEls nombres senars són: ")
    for i in range(imp):
        print(numimp[i], end=" ")

if __name__ == "__main__":
    main()
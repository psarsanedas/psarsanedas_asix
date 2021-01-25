ROMBO = 7

def main():
    for i in range(ROMBO+1):
        for j in range(ROMBO-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print(i, end=" ")
        print()
    for i in range(ROMBO-1, 0, -1):
        for j in range(ROMBO-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print(i, end=" ")
        print()


if __name__ == "__main__":
    main()

import os
os.system("clear")


def main():
    n = int(input("Posa un nombre natural: "))
    for i in range(n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print(i, end=" ")
        print()
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print(i, end=" ")
        print()


if __name__ == "__main__":
    main()

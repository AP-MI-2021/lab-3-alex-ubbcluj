def citire_lista() -> list:
    l = []
    listAsString = input("Dati lista, cu elementele separate printr-un singur spatiu: ")
    numbersFromList = listAsString.split(" ")
    for i in numbersFromList:
        l.append(int(i))
    return l


def is_palindrome(n: int) -> bool:
    """
    Determină dacă un număr dat este palindrom
    param. n - numarul dat
    return - True daca n este palindrom, False in caz contrar
    """
    copie_n = n
    oglindit_n = 0
    while copie_n > 0:
        oglindit_n = 10 * oglindit_n + copie_n % 10
        copie_n = copie_n // 10
    if n == oglindit_n: return True
    return False


def get_longest_all_palindromes(lst: list) -> list:
    """
    determina cea mai lunga secventa dintr-o lista in care toate numerele sunt palindroame
    param. lst - lista
    return - o lista ce contine cea mai lunga secventa in care toate numerele sunt palindroame
    """
    pass


def test_get_longest_all_palindromes():
    pass


test_get_longest_all_palindromes()


def get_longest_powers_of_k(lst: list, k: int) -> list:
    """
    determina cea mai lunga secventa dintr-o lista in care toate numerele se pot scrie ca x**k
    param: lst - lista; k - un numar intreg citit de la tastatura
    return - o lista ce contine cea mai lunga secventa in care toate numerele se pot scrie ca x**k
    """
    pass


def test_get_longest_powers_of_k():
    pass


test_get_longest_powers_of_k()


def main():
    l = []
    while True:
        print("1. Citire date.")
        print("2. Afisare cea mai lungă subsecvență cu proprietatea de la ex. 5")
        print("3. Afisare cea mai lungă subsecvență cu proprietatea de la ex. 15")
        print("4. Ieșire.")
        option = int(input("Selectati optiunea: "))
        if option == 1: l = citire_lista()
        elif option == 2: print(get_longest_all_palindromes(l))
        elif option == 3:
            k = input("Dati valoarea k: ")
            print(get_longest_powers_of_k(l, k))
        elif option == 4: break
        else: print("Optiune invalida")


main()

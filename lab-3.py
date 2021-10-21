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


def only_palindromes(lst: list) -> bool:
    #verifica daca toate numerele din lst sunt palindroame
    for i in lst:
        if is_palindrome(i) == False: return False
    return True


def get_longest_all_palindromes(lst: list) -> list:
    """
    determina cea mai lunga secventa dintr-o lista in care toate numerele sunt palindroame
    param. lst - lista
    return - o lista ce contine cea mai lunga secventa in care toate numerele sunt palindroame
    """
    max_seq = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if len(lst[i: j+1]) > len(max_seq) and only_palindromes(lst[i: j+1]) == True: max_seq = lst[i: j+1]
    return max_seq


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


def isprime(x: int) -> bool:
    """
    determina daca un nr intreg e prim
    param. x - un numar intreg
    return - True daca x e prim, False in caz contrar
    """
    if x < 2: return False
    for i in range(2, x//2+1):
        if x % i == 0: return False
    return True


def get_longest_all_primes(lst: list) -> list:
    pass


def test_get_longest_all_primes():
    pass


test_get_longest_all_primes()


def main():
    l = []
    while True:
        print("1. Citire date.")
        print("2. Afisare cea mai lungă subsecvență cu proprietatea de la ex. 5")
        print("3. Afisare cea mai lungă subsecvență cu proprietatea de la ex. 15")
        print("4. Afisare cea mai lungă subsecvență cu proprietatea de la ex. 2")
        print("5. Ieșire.")
        option = int(input("Selectati optiunea: "))
        if option == 1: l = citire_lista()
        elif option == 2: print(get_longest_all_palindromes(l))
        elif option == 3:
            k = input("Dati valoarea k: ")
            print(get_longest_powers_of_k(l, k))
        elif option == 4: print(get_longest_all_primes(l))
        elif option == 5: break
        else: print("Optiune invalida")


main()
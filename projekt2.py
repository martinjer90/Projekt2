"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Jeřábek
email: martinjer90@gmail.com
discord: blbec908874
"""
import random
import time


def vytvor_nahodne_cislo()->str:
    """
    Funkce generuje náhodné čtyřmístné číslo jako řetězec.
    - Nejprve se vytvoří seznam čísel "123456789".
    - Z tohoto seznamu se náhodně vybere první číslo, které nemůže být nula.
    - Vybrané číslo se odstraní ze seznamu, aby se zabránilo jeho opakování.
    - Zbývající čísla spolu s nulou se náhodně permutují a vyberou se tři z nich.
    - Výsledkem je řetězec čtyř čísel, které tvoří náhodné čtyřmístné číslo.

    Returns:
    - Řetězec reprezentující náhodné čtyřmístné číslo.

    Příklad použití:
    >>> vytvor_nahodne_cislo()
    '4820'
    >>> vytvor_nahodne_cislo()
    '1759'
    """
    cisla = list("123456789")
    prvni_cislo = random.choice(cisla)
    cisla.remove(prvni_cislo)
    ostatni_cisla = random.sample(cisla + ["0"], 3)
    return prvni_cislo + ''.join(ostatni_cisla)

def validovat_cislo(cislo:str)->bool:
    """
    Funkce kontroluje, zda zadané číslo splňuje tyto podmínky:
    - Musí obsahovat pouze čísla.
    - Musí mít přesně 4 znaky.
    - Nesmí začínat nulou.
    - Všechna čísla musí být unikátní.

    Returns:
    - True, pokud číslo splňuje všechny podmínky.
    - False a vypíše odpovídající chybové hlášky, pokud číslo nesplňuje některou z podmínek.

  
    Příklad použití:
    >>> validovat_cislo("1234")
    True
    >>> validovat_cislo("0123")
    Číslo nesmí začínat nulou!
    False
    >>> validovat_cislo("1122")
    Některá čísla se opakují
    False
    >>> validovat_cislo("abcd")
    Zadání musí obsahovat pouze čísla!
    False
    """
    if not cislo.isdigit():
        print(f"Zadání musí obsahovat pouze čísla!")
        return False
    elif len(cislo)!=4:
        print(f"Číslo nemá 4 znaky!")
        return False
    elif cislo[0]=="0":
        print(f"Číslo nesmí začínat nulou!")
        return False
    elif len(set(cislo)) != 4:
        print(f"Některá čísla se opakují")
        return False
    else:
        return True
    
def bulls_cows(tajne_cislo: str, zadane_cislo: str)->tuple:
    """
    Tato funkce porovnává zadané číslo s tajným číslem a počítá počet bulls (správná čísla na správných pozicích)
    a cows (správná čísla na nesprávných pozicích).

    Returns:
    - Tuple obsahující počet bulls a cows.

    Příklad použití:
    >>> bulls_cows("1234", "4321")
    (0, 4)
    >>> bulls_cows("5678", "5689")
    (2, 1)
    >>> bulls_cows("9999", "1999")
    (3, 0)
    """
    bulls=0
    cows=0
    for i in range (4):
        if zadane_cislo[i]==tajne_cislo[i]:
            bulls+=1
        elif zadane_cislo[i] in tajne_cislo:
            cows+=1
    return(bulls,cows)
        



separator="-"*50
statistiky=[]

while True:
    print(f"Ahoj!\n{separator}")
    print(f"Vygeneroval jsem pro tebe 4 náhodná čísla.\nPojďme si zahrát hru bulls and cows.\n{separator}")
    print(f"Zadej 4 místné číslo:\n{separator}")

    pocatecni_cas=time.time()
    scitac_pokusu=0
    nahodne_cislo=vytvor_nahodne_cislo()

    while True:
        vyber_cisel=input(">>> ")
        if validovat_cislo(vyber_cisel):
            scitac_pokusu+=1
            bulls,cows=bulls_cows(nahodne_cislo,vyber_cisel) 
            print(f"{bulls}bulls,{cows}cows")
            print(separator)
            if bulls==4:
                konecny_cas=time.time()
                probehly_cas=konecny_cas-pocatecni_cas
                print(f"Gratulujeme, uhodli jste číslo na pokus číslo {scitac_pokusu}.")
                print(f"Trvalo ti to {probehly_cas:.0f} sekund.")
                if scitac_pokusu <=5:
                    print(f"To je úžasný výsledek!") 
                    print(separator)
                elif 6<= scitac_pokusu <=10:
                    print(f"To je průměrný výsledek.")
                    print(separator)
                else:
                    print(f"To je podprůměrný výsledek.") 
                    print(separator)
                 
                statistiky.append({"pokusy": scitac_pokusu,"cas": probehly_cas})
                break
            else:
                print(f"Zkus zadat jiné číslo:")
                continue
        else:
            print(f"Zadej číslo znovu:\n{separator}")
            continue
    
    print(f"Statistika minulých her:")
    for idx, hra in enumerate(statistiky, start=1):
            print(f"Hra {idx}: Počet pokusů: {hra["pokusy"]}, Trvání: {hra["cas"]:.0f} sekund.")
    opakovat_hru=input(f"Chceš hrát další hru(ano/ne): ").lower()
    if opakovat_hru!="ano":
        print(f"Ukončuji hru...")
        break
    else:
        print(f"Spouštím další hru:")
        print(separator)
        continue
    
         
            
                

   
               

    
        
    
    
    
    

    
  


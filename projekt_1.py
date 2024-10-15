'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Szotkowski
email: michal.szotkowski@molnlycke.com
discord: Michal S. misande
'''
# Zadaný text na zpracování
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Seznam registrovaných uživatelů a jejich hesel
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Uživatel musí zadat své uživatelské jméno a heslo
print("& python projekt_1.py")
uzivatel = input("Username: ")
heslo = input("Password: ")

# Ověření uživatelského jména a hesla
if uzivatele.get(uzivatel) != heslo:
    print("unregistered user, terminating the program..")
    exit()

# Uvítání uživatele
oddelovaci_cara = "-" * 40
print(oddelovaci_cara)
print("Welcome to the app,", uzivatel)
print("We have 3 texts to be analyzed.")
print(oddelovaci_cara)

# Výběr textu k analýze
cislo_textu = input("Enter a number btw. 1 and 3 to select: ")

if cislo_textu.isdigit() == False or int(cislo_textu) not in range(1, 4):   # Ověření zda uživatel zadal číslo 1-3
    print("invalid number, terminating the program..")
    exit()

text = TEXTS[int(cislo_textu) - 1]  # Vybraný text k analýze

# Úprava textu
slova = text.split()    # Rozdělení textu na slova
slova = [slovo.strip(",.") for slovo in slova]  # Odstranění interpunkce ze slov

# Proměnné pro analýzu
pocet_slov = 0                      # Počet slov ve vybraném textu
pocet_slov_zac_velkym_pismenem = 0  # Počet slov začínajících velkým písmenem
pocet_slov_velka_pismena = 0        # Počet slov psaných velkými písmeny
pocet_slov_mala_pismena = 0         # Počet slov psaných malými písmeny
pocet_cisel = 0                     # Počet čísel
suma_cisel = 0                      # Součet všech čísel v textu

# Analýza textu
pocet_slov = len(slova) # Počet slov ve vybraném textu
delky_slov = dict() # Slovník pro délky slov

for slovo in slova:
    if slovo.istitle():
        pocet_slov_zac_velkym_pismenem += 1 # Počet slov začínajících velkým písmenem
    elif slovo.isupper():
        pocet_slov_velka_pismena += 1 # Počet slov psaných velkými písmeny
    elif slovo.islower():
        pocet_slov_mala_pismena += 1 # Počet slov psaných malými písmeny
    elif slovo.isdigit():
        pocet_cisel += 1 # Počet čísel
        suma_cisel += int(slovo) # Součet všech čísel v textu

    delka_slova = len(slovo)    # Délka slova
    if delky_slov.get(delka_slova) == None: # Pokud délka slova není v slovníku
        delky_slov[delka_slova] = 1 # Přidat délku slova do slovníku
    else:
        delky_slov[delka_slova] += 1    # Zvýšit počet slov s touto délkou

delky_slov = dict(sorted(delky_slov.items()))   # Seřadit slovník podle klíčů

# Výsledky analýzy
print(oddelovaci_cara)
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_slov_zac_velkym_pismenem} titlecase words.")
print(f"There are {pocet_slov_velka_pismena} uppercase words.")
print(f"There are {pocet_slov_mala_pismena} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")
print(oddelovaci_cara)
print("LEN|  OCCURENCES        |NR.")
print(oddelovaci_cara)

for delka, pocet in delky_slov.items():
    print(f"{delka:>3}|{'*' * pocet:<20}|{pocet:<2}")   # Grafické znázornění délek slov
    
print(oddelovaci_cara)
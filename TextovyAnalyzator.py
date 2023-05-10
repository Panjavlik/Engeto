"""
TextovyAnalyzator.py: první projekt do Engeto Online Python Akademie
author: Jan Pavlík
email: Jan.Pavlik@rmgastro.com
discord: Jan P.#7609
"""

#Const
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

Users = {
    'Bob': '123',
    'Ann': 'pass123',
    'Mike': 'password123',
    'Liz': 'pass123'
       }

#var
separator = "-" * 65
PocetTitle = 0
PocetUpper = 0
PocetLower = 0
PocetNum = 0
SumNum = 0
counts = {}
text = ''

#Přihlášení uživatele
username = input("Jmeno:")
password = input("Heslo:")


# Ověření přihlášení
if Users.get(username.capitalize()) == password:
       print(separator, "Welcome to the app " + username, "We have 3 texts to be analyzed.", separator, sep="\n")
else:
       print(separator, "username:"+username, "password"+password, "unregistered user, terminating the program..", separator, sep="\n")
       exit()

text_no = input("Enter a number btw. 1 and 3 to select:")

if text_no.isnumeric():
        if int(text_no) < len(TEXTS):
              text = TEXTS[int(text_no)]
              print(separator)
        else:
              print('The entered value was not found!')
              exit()
else:   print("The entered value is not a number!")

#Průchod textem
for i in text.split():
    if i[0].isupper():
        PocetTitle = PocetTitle + 1
    elif i.isupper():
        PocetUpper = PocetUpper + 1
    elif i.islower():
        PocetLower = PocetLower + 1
    elif i.isnumeric():
        PocetNum = PocetNum + 1
        SumNum = SumNum + int(i)

#Output
print('There are', len(text.split()), 'words in the selected text.')
print('There are', PocetTitle, 'titlecase words.')
print('There are', PocetUpper, 'upercase words.')
print('There are', PocetLower, 'lowercase words.')
print('There are', PocetNum, 'numeric words.')
print('The sum of all the numbers', SumNum)

print(separator)
print(f'LEN\t\t\tOCCURENCES\t\tNR')
print(separator)

# Cyklus, který spočítá jednotlivé výskyty čísel
for count in text.split():

    # .. pokud číslo není uložené, eviduj jej jako první hodnotu
    if len(count) not in counts:
        counts[len(count)] = 1

    # .. pokud číslo je uložené, inkrementuj původní hodnotu
    else:
        counts[len(count)] = counts[len(count)] + 1

#Setřiď podle klíče a vypiš seřazené hodnoty
for key, value in sorted(counts.items()):
    print(f'{key}\t\t\t{value* "*"}\t\t\t{value}')
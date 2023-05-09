"""
TextovyAnalyzator.py: první projekt do Engeto Online Python Akademie
author: Jan Pavlík
email: Jan.Pavlik@rmgastro.com
discord: Jan P.#7609
"""

from task_template import TEXTS  # Import Var
from task_template import Users  # Import Přihlášení

#var
separator = "-" * 65
PocetTitle = 0
PocetUpper = 0
PocetLower = 0
PocetNum = 0
SumNum = 0
counts = {}

#Přihlášení uživatele
username = input("Jmeno:")
password = input("Heslo:")

print(username)
# Ověření přihlášení
if Users.get(username.capitalize()) == password:
        print(separator ,"Welcome to the app "+ username, "We have 3 texts to be analyzed.",separator, sep="\n")
else:
        print(separator, "username:"+username,"password"+password,"unregistered user, terminating the program..", separator, sep="\n")
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
    elif i.isupper() :
        PocetUpper = PocetUpper + 1
    elif i.islower():
        PocetLower = PocetLower + 1
    elif i.isnumeric():
        PocetNum = PocetNum + 1
        SumNum = SumNum + int(i)

print('There are',len(text.split()),'words in the selected text.')
print('There are',PocetTitle,'titlecase words.')
print('There are',PocetUpper,'upercase words.')
print('There are',PocetLower,'lowercase words.')
print('There are',PocetNum,'numeric words.')
print('The sum of all the numbers', SumNum)

print(separator)
print("LEN","OCCURENCES","NR",sep='\t'+'|')
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
      print(key,'*' * value, value ,sep='|')
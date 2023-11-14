ma_liste = [];
contat_wilfried = {"nom" : "Wilfried", "alias" : "Manu le COQ"}
ma_liste.append(contat_wilfried);
# print(ma_liste)

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
#for chien in races_de_chien:
    # print(chien)

# for i in range(5):
#     if (i == 3):
#         continue
#     print(i)
"""
QUELQUELS FONCTIONS ET APPLICATIONS
"""
def factoriel(nombre):
    if nombre <= 2 :
        return 2
    else :
        return nombre * factoriel(nombre - 1)

def somme(nombre):
    """
    DOC SOMME
    """
    if nombre == 0 :
        return 0
    else :
        return nombre + somme(nombre - 1)

def multiplication(x):
    print()
    for i in range(11):
        print(f"{x} * {i} = {x*i}")
    print()

# for element in range(10):
#     multiplication(element)

print(factoriel(5))
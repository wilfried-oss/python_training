def tri_insertion(liste):
    for i in range(0, len(liste)):
        for j in range(1, len(liste)):
            temp = liste[j]
            if liste[j+1] < liste[j] :
                liste[j+1] = temp
                liste[j] = liste[j+1]


def tri_insertion2(liste):
    for i in range(1, len(liste)):
        element_courant = liste[i]
        j = i - 1
        while j >= 0 and element_courant < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = element_courant               

if __name__ == '__main__':
    ma_liste = [12, 11, 13, 5, 6]
    tri_insertion2(ma_liste)
    print("Liste triée :", ma_liste)
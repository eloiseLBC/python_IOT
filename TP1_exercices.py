# ------------ Affectations multiples
# --- Exercice 2.1 
# largeur = 20 -> Assigner la valeur 20 à la variable largeur
# hauteur = 5 * 9.3 -> Assigner la valeur 5*9.3 à la variable hauteur
# largeur * hauteur -> Multiplier la valeur de largeur par la valeur de hauteur

# --- Exercice 2.2
def ex2_2():
    print("Exercice 2.2")
    a, b, c = 3, 5, 7
    print(a-b//c) # 3-5//7 = 3-0 = 3

# --- Exercice 2.3
def ex2_3():
    print("Exercice 2.3")
    r, pi = 12 , 3.14159
    s = pi * r**2
    print(type(r), type(pi), type(s)) # <class 'int'> <class 'float'> <class 'float'>
    
# ------------ Execution conditionnelle
# --- Exercice 3.1
def ex3_1():
    print("Exercice 3.1")
    a = input("Entrez un nombre entier : ")
    b = input("Entrez un autre nombre entier : ")
    try:
        if int(a) < int(b):
            print("a est plus petit que b")
        elif int(a) > int(b):
            print("a est plus grand que b")
        else:
            print("a est égal à b")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")

# --- Exercice 3.2
def ex3_2():
    print("Exercice 3.2")
    a = input("Entrez un nombre : ")
    try:
        if float(a) > 0:
            print("a est positif")
        elif float(a) < 0:
            print("a est négatif")
        else:
            print("a est nul")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
        
# --- Exercice 3.3
def ex3_3():
    print("Exercice 3.3")
    a = input("Entrez un nombre : ")
    try:
        if float(a) % 2 == 0:
            print("a est pair")
            print("a est divisible par 2")
        else:
            print("a est impair")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

# ------------ Réaffectation
# --- Exercice 4.1
def ex4_1():
    print("Exercice 4.1")
    a, b, c, d = 3, 4, 5, 7
    temp = a
    a = c
    c = temp
    print(f"a : {a}, b : {b}, c : {c}, d : {d}") # 5 4 3 7
    
# ------------ Répétitions en boucle - l'instruction while
# --- Exercice 4.2
def ex4_2():
    print("Exercice 4.2")
    i = 0
    while i < 20:
        print(f"Itération {i+1} de la table de 7 : {7*(i+1)}")
        i += 1
    print("Fin des 20 premières itérations de la table de 7")
    
# --- Exercice 4.3
def ex4_3():
    print("Exercice 4.3")
    euro = 0
    result = 0
    while result <= 16384:
        result = euro * 1.65
        print(f"{euro} euros = {result} dollar(s) canadien(s)")
        
# --- Exercice 4.4
def ex4_4():
    print("Exercice 4.4")
    i = 0
    a = input("Entrez un nombre entier : ")
    try:
        a = int(a)
        while i < 12:
            print(a*3)
            a *= 3
            i += 1
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")
        return

# --- Exercice 4.7
def ex4_7():
    print("Exercice 4.7")
    i = 0
    message = ""
    while i < 20:
        if (i+1) % 3 == 0:
            message += f"{(i+1)*7} * "
        else:
            message += f"{(i+1)*7} "
        i += 1
    print(message)

# --- Exercice 4.8
def ex4_8():
    print("Exercice 4.8")
    i = 0
    while i < 50:
        if (i*13) % 7 == 0:
            print(f"{i*13}")
        i += 1
        
# --- Exercice 4.9
def ex4_9():
    print("Exercice 4.9")
    i = 0
    while i < 7:
        print("*" * (i+1))
        i += 1

# ------------ Le type float
# --- Exercice 5.3
def ex5_3():
    print("Exercice 5.3")
    a = input("Entrez une température en Farenheit : ")
    try:
        a = float(a)
        c = (a - 32) * 5 / 9
        print(f"La température de {a}F° en Celsius est : {c}C°")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
        return

# --- Exercice 5.4
def ex5_4():
    print("Exercice 5.4")
    annee = 0
    argent = 100
    while annee < 20:
        annee += 1
        argent *= 1.043
        print(f"Année {annee} : {argent} euros")
        
# --- Exercice 5.5
def ex5_5():
    print("Exercice 5.5")
    case = 1
    riz = 1
    while case <= 64:
        print(f"Case {case} : {riz} grains de riz")
        riz = riz*2
        case += 1
    print(f"Total de grains de riz : {riz}")

# ------------ Les données alphanumériques
# --- Exercice 5.6
def ex5_6():
    print("Exercice 5.6")
    phrase = input("Entrez une phrase : ")
    if "e" in phrase:
        print("La lettre 'e' est présente dans la phrase.")
    else:
        print("La lettre 'e' n'est pas présente dans la phrase.")
        
def ex5_7():
    print("Exercice 5.7")
    phrase = input("Entrez une phrase : ")
    if "e" in phrase:
        count_e = phrase.count("e")
        print(f"La lettre 'e' est présente {count_e} fois dans la phrase.")
    else:
        print("La lettre 'e' n'est pas présente dans la phrase.")
    
# --- Exercice 5.8
def ex5_8():
    print("Exercice 5.8")
    phrase = input("Entrez une phrase : ")
    message = ""
    for char in phrase:
        message += char + "*"
    print(message[:-1]) 

# --- Exercice 5.9
def ex5_9():
    print("Exercice 5.9")
    phrase = input("Entrez une phrase : ")
    message = ""
    for char in phrase:
        message += phrase[-1:]
        phrase = phrase[:-1]     
    print(message)
    
# --- Exercice 5.10
def ex5_10():
    print("Exercice 5.10")
    phrase = input("Entrez une phrase : ")
    verse = phrase
    message = ""
    for char in phrase:
        message += phrase[-1:]
        phrase = phrase[:-1]     
    if message == verse:
        print("La phrase est un palindrome.")
    else:
        print("La phrase n'est pas un palindrome.")
        
# ------------ Les listes (première approche)
# --- Exercice 5.11
def ex5_11():
    print("Exercice 5.11")
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    liste = []
    for day, month in zip(days, months):
        liste.append(month)
        liste.append(day)
    print(liste)

# --- Exercice 5.12
def ex5_12():
    print("Exercice 5.12")
    months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    print(*months)

# --- Exercice 5.13
def ex5_13():
    print("Exercice 5.13")
    lst = [32, 5, 12, 8, 75, 89, 10, 66, 45, 23]
    print("Le plus grand élément de la liste est :", max(lst))    

# --- Exercice 5.14
def ex5_14():
    print("Exercice 5.14")
    lst = [32, 5, 12, 8, 75, 89, 10, 66, 45, 23]
    lst_pairs = []
    lst_impairs = []
    for element in lst:
        if element % 2 == 0:
            lst_pairs.append(element)
        else:
            lst_impairs.append(element)
    print("Liste des éléments pairs :", lst_pairs)
    print("Liste des éléments impairs :", lst_impairs)

# --- Exercice 5.15
def ex5_15():
    print("Exercice 5.15")
    lst = ["Jean", "Maximilien", "Pierre", "Paul", "Jacques", "Brigitte", "Marie", "Sophie"]
    lst_up = []
    lst_down = []
    for el in lst:
        if len(el) < 6:
            lst_down.append(el)
        else:
            lst_up.append(el)
    print("Liste des prénoms de moins de 6 caractères :", lst_down)
    print("Liste des prénoms de 6 caractères ou plus :", lst_up)
    
# ------------ Fonctions prédéfinies
# --- Exercice 6.1
def ex6_1():
    print("Exercice 6.1")
    miles_per_hour = input("Entrez une vitesse en miles par heure : ")
    try:
        miles_per_hour = float(miles_per_hour)
        kilometers_per_hour = miles_per_hour * 1.60934
        meters_per_second = kilometers_per_hour / 3.6
        print(f"{miles_per_hour} mph est égal à {kilometers_per_hour} km/h")
        print(f"{miles_per_hour} mph est égal à {meters_per_second} m/s")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
        return

# --- Exercice 6.2
def ex6_2():
    print("Exercice 6.2")
    c1 = input("Entrez la longueur du premier côté : ")
    c2 = input("Entrez la longueur du deuxième côté : ")
    c3 = input("Entrez la longueur du troisième côté : ")
    try:
        perimetre = float(c1) + float(c2) + float(c3)
        demi_perimetre = perimetre / 2
        aire = (demi_perimetre * (demi_perimetre - float(c1)) * (demi_perimetre - float(c2)) * (demi_perimetre - float(c3))) ** 0.5
        print(f"Le périmètre du triangle est : {perimetre}")
        print(f"L'aire du triangle est : {aire}")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return

# --- Exercice 6.4
def ex6_4():
    print("Exercice 6.4")
    print("Vous pouvez terminer la liste en frappant sur <Entrer>")
    a = input("Entrez une valeur : ")
    lst = []
    while a != "":
        lst.append(a)
        a = input("Entrez une valeur : ")
    print("Liste des valeurs :", lst)

# ------------ Révisions
# --- Exercice 6.5
def ex6_5():
    print("Exercice 6.5")
    print("Le résultat si a vaut 1 est : perdu")
    print("Le résultat si a vaut 2 est : gagné")
    print("Le résultat si a vaut 3 est : un instant svp")
    print("Le résultat si a vaut 15 est : perdu")

# --- Exercice 6.6
def ex6_6():
    print("Exercice 6.6")
    print("Le premier programme a pour résultat : Rien d'affiché")
    print("Le deuxième programme a pour résultat : 'presque gagné'")
    print("Le troisième programme a pour résultat : 'perdu'")

# --- Exercice 6.7
def ex6_7():
    print("Exercice 6.7")
    print("Si on prend le programme c précédent et que a=0 alors le résultat est : 'gagné'")
    
# --- Exercice 6.8a
def ex6_8a():
    print("Exercice 6.8a")
    a = 0
    b = 32
    result = 0
    for number in range(a, b):
        if number % 3 == 0 and number % 5 == 0:
            result += number
    print("La somme des multiples de 3 et 5 entre 0 et 32 est :", result)

# --- Exercice 6.8b
def ex6_8b():
    print("Exercice 6.8b")
    a = 0
    b = 32
    result = 0
    for number in range(a, b):
        if number % 3 == 0 or number % 5 == 0:
            result += number
    print("La somme des multiples de 3 et 5 entre 0 et 32 est :", result)
    
# --- Exercice 6.14
def ex6_14():
    print("Exercice 6.14")
    lst = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
    for el in lst:
        print(f"{el} : {len(el)} caractères")    

# --- Exercice 6.15
def ex6_15():
    print("Exercice 6.15")
    note = input("Entrez une note : ")
    lst = []
    while float(note) > 0 :
        try:
            note = float(note)
            if note > 20:
                raise ValueError("La note doit être comprise entre 0 et 20.")
            if note < 0:
                return 
            lst.append(note)    
            note = input("Entrez une note : ")   
        except ValueError as e:
            print(f"Erreur : {e}")
            print("La liste des notes actuelle est comme ceci : ", lst)
            return
    print(f"Il y a {len(lst)} note(s) dans la liste.")
    print(f"La note la plus élevée est : {max(lst)}")
    print(f"La note la plus basse est : {min(lst)}")
    print(f"La moyenne des notes est : {sum(lst)/len(lst)}")

# ------------ Fonctions définies par l'utilisateur
# --- Exercice 7.2
def ex7_2():
    print("Exercice 7.2")
    def ligneCar(n, ca):
        print(ca * n)
    n = input("Entrez le nombre de caractères : ")
    ca = input("Entrez le caractère : ")
    try:
        n = int(n)
        ligneCar(n, ca)
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")
        return

# --- Exercice 7.5
def ex7_5():
    print("Exercice 7.5")
    def maximum(n1, n2, n3):
        return max(n1, n2, n3)
    n1 = input("Entrez le premier nombre : ")
    n2 = input("Entrez le deuxième nombre : ")
    n3 = input("Entrez le troisième nombre : ")
    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        print("Le maximum est :", maximum(n1, n2, n3))
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return

# --- Exercice 7.9
def ex7_9():
    print("Exercice 7.9")
    def compteCar(ca, ch):
        print(f"Le caractère '{ca}' apparaît {ch.count(ca)} fois dans la chaîne.")
    ca = input("Entrez le caractère à compter : ")
    ch = input("Entrez la chaîne de caractères : ")
    compteCar(ca, ch)

# --- Exercice 7.10
def ex7_10():
    def indexMax(liste):
        max_value = max(liste)
        index = liste.index(max_value)
        return index
    lst = []
    while True:
        value = input("Entrez une valeur (ou 'stop' pour trouver l'index de la plus grande valeur) : ")
        if value.lower() == 'stop':
            print("Liste des valeurs :", lst)
            if lst:
                index = indexMax(lst)
                print(f"L'index de la plus grande valeur est : {index}")
            else:
                print("La liste est vide.")
            break
        try:
            value = float(value)
            lst.append(value)
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")
            continue
        
# --- Exercice 7.11
def ex7_11():
    print("Exercice 7.11")
    def nomMois(n):
        mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        if 1 <= n <= 12:
            return mois[n-1]
        else:
            return None
    n = input("Entrez un nombre entre 1 et 12 : ")
    try:
        n = int(n)
        mois = nomMois(n)
        if mois:
            print(f"Le mois correspondant au nombre {n} est : {mois}")
        else:
            print("Erreur : Le nombre doit être compris entre 1 et 12.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")
        return

# --- Exercice 7.12
def ex7_12():
    print("Exercice 7.12")
    def inverse(ch):
        message = ""
        for char in ch:
            message += ch[-1:]
            ch = ch[:-1]     
        return message
    ch = input("Entrez une chaîne de caractères : ")
    result = inverse(ch)
    print("La chaîne inversée est :", result)
    
# --- Exercice 7.13
def ex7_13():
    print("Exercice 7.13")
    def compteMots(ph):
        nb_mots = len(ph.split())
        return nb_mots
    ph = input("Entrez une phrase : ")
    result = compteMots(ph)
    print("Le nombre de mots dans la phrase est :", result)

# ------------ Fonctions définies par l'utilisateur
# --- Exercice 7.14
def ex7_14():
    print("Exercice 7.14")
    def volBoite(x1=10, x2=10, x3=10):
        try:
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            return x1 * x2 * x3
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            return None
    x1 = input("Entrez la longueur de la boîte : ")
    x2 = input("Entrez la largeur de la boîte : ") 
    x3 = input("Entrez la hauteur de la boîte : ")
    if x1 == "":
        if x2 == "":
            if x3 == "":
                print("Le volume de la boîte est :", volBoite())
            else:
                print("Le volume de la boîte est :", volBoite(x3=x3))
        else:
            if x3 == "":
                print("Le volume de la boîte est :", volBoite(x2=x2))
            else:
                print("Le volume de la boîte est :", volBoite(x2=x2, x3=x3))
    else:
        if x2 == "":
            if x3 == "":
                print("Le volume de la boîte est :", volBoite(x1=x1))
            else:
                print("Le volume de la boîte est :", volBoite(x1=x1, x3=x3))
        else:
            if x3 == "":
                print("Le volume de la boîte est :", volBoite(x1=x1, x2=x2))
            else:
                print("Le volume de la boîte est :", volBoite(x1=x1, x2=x2, x3=x3))

# --- Exercice 7.15
def ex7_15():
    print("Exercice 7.15")
    def volBoite(x1=1, x2=1, x3=1):
        try:
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            return x1 * x2 * x3
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            return None
    x1 = input("Entrez la longueur de la boîte : ")
    x2 = input("Entrez la largeur de la boîte : ")
    x3 = input("Entrez la hauteur de la boîte : ")
    if x1 == "":
        if x2 == "":
            if x3 == "":
                print("Le volume de la boîte est :", volBoite())
            else:
                print("Le volume de la boîte est :", volBoite(x3=x3))
        else:
            if x3 == "":
                print("Le volume de la boîte est :", volBoite(x2=x2))
            else:
                print("Le volume de la boîte est :", volBoite(x2=x2, x3=x3))
    else:
        if x2 == "":
            if x3 == "":
                print("Le volume de la boîte est :", volBoite(x1=x1))
            else:
                print("Le volume de la boîte est :", volBoite(x1=x1, x3=x3))
        else:
            if x3 == "":
                print("Le volume de la boîte est :", volBoite(x1=x1, x2=x2))
            else:
                print("Le volume de la boîte est :", volBoite(x1=x1, x2=x2, x3=x3))
    
    
# --- Exercice 7.16
def ex7_16():
    print("Exercice 7.16")
    def changeCar(ch, ca1, ca2, debut, fin):
        if debut < 0 or fin > len(ch) or debut >= fin:
            return ch
        else:
            return ch[:debut] + ch[debut:fin].replace(ca1, ca2) + ch[fin:]
    ch = input("Entrez une chaîne de caractères : ")
    ca1 = input("Entrez le caractère à remplacer : ")
    ca2 = input("Entrez le caractère de remplacement : ")
    debut = input("Entrez la position de début : ")
    fin = input(f"Entrez la position de fin (La chaîne de caractères est de longueur {len(ch)}): ")
    try:
        debut = int(debut)
        fin = int(fin)
        result = changeCar(ch, ca1, ca2, debut, fin)
        print("La chaîne modifiée est :", result)
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
        return
# --- Exercice 7.17
def ex7_17():
    def eleMax(lst, debut, fin):
        if debut < 0 or fin > len(lst) or debut >= fin:
            return None
        else:
            max_value = max(lst[debut:fin])
            return max_value
    lst = [9, 3, 6, 1, 7, 5, 4, 8, 2]
    print("Voici la liste :", lst)
    debut = input("Entrez la position de début : ")
    fin = input("Entrez la position de fin : ")
    try:
        debut = int(debut)
        fin = int(fin)
        result = eleMax(lst, debut, fin)
        if result is not None:
            print("L'élément maximum entre les positions", debut, "et", fin, "est :", result)
        else:
            print("Erreur : Les positions doivent être valides.")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
        return
    
# ------------ Chaînes et while
# --- Exercice 10.2
def ex10_2():
    print("Exercice 10.2")
    def decoupe(ch):
        fragments = []
        for i in range(0, len(ch), 5):
            fragments.append(ch[i:i+5])
        return fragments
    def inverse(fragments):
        return fragments[::-1]
    ch = input("Entrez une chaîne de caractères : ")
    fragments = decoupe(ch)
    fragments_inverse = inverse(fragments)
    print("Les fragments de 5 caractères dans l'ordre inverse sont :")
    for fragment in fragments_inverse:
        print(fragment)
    
# --- Exercice 10.3
def ex10_3():
    print("Exercice 10.3")
    def trouve(ch, n):
        index_lst = []
        for i in range(len(ch)):
            if ch[i] == n:
                index_lst.append(i)
        return index_lst if index_lst else -1
    ch = input("Entrez une chaîne de caractères : ")
    n = input("Entrez un caractère à chercher dans la chaîne : ")

    index = trouve(ch, n)
    if index != -1:
        print(f"Le caractère {n} se trouve à l'index {index} dans '{ch}'.")
    else:
        print(f"Le caractère {n} ne se trouve pas dans la '{ch}.")

# --- Exercice 10.4
def ex10_4():
    print("Exercice 10.4")
    def trouve(ch, n, position):
        for i in range(position, len(ch)):
            if ch[i] == n:
                return i
        return -1
    ch = input("Entrez une chaîne de caractères : ")
    n = input("Entrez un caractère à chercher dans la chaîne : ")
    position = input("Entrez la position de départ : ")
    try:
        position = int(position)
        index = trouve(ch, n, position)
        if index != -1:
            print(f"Le nombre {n} se trouve à l'index {index} dans '{ch}'.")
        else:
            print(f"Le nombre {n} ne se trouve pas dans la '{ch}.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")
        return

# --- Exercice 10.5
def ex10_5():
    print("Exercice 10.5")
    def compteCar(ch, ca):
        return ch.count(ca)
    ch = input("Entrez une chaîne de caractères : ")
    ca = input("Entrez le caractère à compter : ")
    try:
        count = compteCar(ch, ca)
        print(f"Le caractère '{ca}' apparaît {count} fois dans la chaîne.")
    except ValueError:
        print("Erreur : Veuillez entrer un caractère valide.")
        return

# ------------ L'instruction for ... in ...
# --- Exercice 10.6
def ex10_6():
    print("Exercice 10.6")
    prefixes = "JKLMNOP"
    suffix = "ack"
    for letter in prefixes:
        print(letter + suffix)

# --- Exercice 10.7
def ex10_7():
    print("Exercice 10.7")
    nb = 0
    phrase = input("Entrez une phrase : ")
    for mot in phrase.split():
        nb += 1
    print("Le nombre de mots dans la phrase est :", nb)

# --- Exercice 10.9
def ex10_9():
    print("Exercice 10.9")
    def estUnChiffre(c):
        return c.isdigit()
    c = input(("Entrez un caractère : "))
    if estUnChiffre(c):
        print(f"{c} est un chiffre.")
    else:
        print(f"{c} n'est pas un chiffre.")
    
# --- Exercice 10.10
def ex10_10():
    print("Exercice 10.10")
    def estUneMaJ(c):
        return c.isupper()
    c = input("Entrez un caractère : ")
    if estUneMaJ(c):
        print(f"{c} est une majuscule.")
    else:
        print(f"{c} n'est pas une majuscule.")

# --- Exercice 10.11
def ex10_11():
    print("Exercice 10.11")
    def chaineListe(phrase):
        return phrase.split()
    phrase = input("Entrez une phrase : ")
    liste = chaineListe(phrase)
    print("La liste des mots est :", liste)

# --- Exercice 10.12
def ex10_12():
    def chaineListe(phrase):
        return phrase.split()
    def estUneMaJ(c):
        return c.isupper()
    phrase = input("Entrez une phrase : ")
    liste = chaineListe(phrase)
    lst_maj = []
    for i in liste:
        if estUneMaJ(i[0]):
            lst_maj.append(i)
    print("Les mots qui commencent par une majuscule sont :", lst_maj)
            
# --- Exercice 10.13
def ex10_13():
    print("Exercice 10.13")
    def estUneMaJ(c):
        return c.isupper()
    phrase = input("Entrez une phrase : ")
    nb_maj = 0
    for i in phrase:
        if estUneMaJ(i):
            nb_maj += 1
    print("Le nombre de majuscules dans la phrase est :", nb_maj)
    print("Le nombre de minuscules dans la phrase est :", len(phrase) - nb_maj)
        
    
    


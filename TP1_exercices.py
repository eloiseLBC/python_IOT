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


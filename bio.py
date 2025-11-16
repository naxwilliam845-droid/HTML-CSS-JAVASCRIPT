while True :
    try:
        valeur = int(input("Entrez un nombre entre 1 et 100 :"))
        if 1 <= valeur <= 100:
            print ("valide !")
            break
        else:
            print("le nombre doit etre 1 et 100.")
    except ValueError:
            print("Erreur :Entrez un nombre valide.")
        githhub
# demande nom et prenom

def inputUserInfos():   #function
    while True:
        nom = input("Entrer votre nom : ")
        if len(nom) <2 :
            return inputUserInfos()

        age = input("entre votrer age : ")
        try:
            ageInt = int(age)
        except ValueError:
            print("Erreur vous devez entre un nombre")
            age = input("entre votrer age")
        break
    info = (f"Bonjour,{nom}, tu as {age} ans et bienvenue à ODC.")
    return info

nameAndAge = inputUserInfos()
print(nameAndAge)
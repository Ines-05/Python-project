import csv

list_class=[]
matricules=[]


print("-------------------Bienvenue sur notre application de gestion de notes dans une classe ---------------")
nbr_etudiant=int(input("Quel est l'effectif de la classe : "))
nbr_remplir=int(input("Veuillez préciser le nombre d'etudiants à enregistrer : "))
nbr_matiere=int(input("Veuillez indiquez le nombre de matière : "))
def remplir_liste():
    print("**************Remplir la liste de la classe***********")
    for i in range(nbr_remplir):
        name= input("Veuillez entrez le nom et le prenom de l'etudiant : ")
        if name in list_class:
            print("Name already in the list")
        else:
            matricule=input("Veuiller entre le matricule de l'etudiant : ")
            if matricule in matricules:
                print("Ce matricule appartient deja à un autre etudiant.")
            else:
                matricules.append(matricule)
                list_class.append(name)  
            
    list_sorted=sorted(list_class)
    return list_sorted

def ajouter_etu():
    name=input("Entrer le nom et le prenom du nouvel étudiant : ")
    matricule=input("Veuillez précisez le matricule de l'etudiant : ")
    if matricule not in matricules:
        matricules.append(matricule)
    else:
        print("Matricule already taken")
    if name not in list_class:
        list_class.append(name)
        list_sorted=sorted(list_class)
        return list_sorted
    else:
        return False
    
def saisir_note():
    notes_etu=[]
    
    for i in range(nbr_matiere):
        notes=[]
        for j in range(2):
            note=float(input(f"Veuillez entre la note {j+1} de l'etudiant pour la matière {i+1} : "))
            while (note <0 or note >20 ):
                note=float(input("La note entrer n'est pas valide. Veuillez retaper la note : "))
            notes.append(note)
        notes_etu.append(notes)
        print(notes_etu)
        # notes_etu.clear()
    
    return notes_etu

def calcul_mat(notes_etu):#calculer moyenne matiere
    matiere=[]
    for note in notes_etu:
        mat=[]
        for i in range(0,len(note),2):
            som=note[i]+note[i+1]
            moy_mat=som/2
            mat.append(moy_mat)
        matiere.append(mat)
    return matiere

def calculer_moyG(matiere):#calculer moyenne géneral
    moyenne_G=[]
    for n in matiere:
        # print(n)
        s=sum(n)
        moy_G=s/len(n)
        moyenne_G.append(moy_G)
    return moyenne_G

def sauvegarder_fichier_csv(noms, notes_etudiants):
    with open("notes_etudiants.csv",mode="a+",newline='') as file :
        writer = csv.writer(file)

        header=["Nom et prenom"]

        for i in range(len(notes_etudiants[0])//2):
            header.append(f"Matiere {i+1} _Note 1 ")
            header.append(f"Matiere {i+1} _Note 2 ")
        header.append("Moyenne")

        writer.writerow(header)

        for i in range(len(noms)):
            ligne=[noms[i]]
            for j in range(0,len(notes_etudiants[i]),2):
                note1=notes_etudiants[i][j]
                note2=notes_etudiants[i][j+1]
                ligne.extend([note1,note2])

            moyenne=calculer_moyG([notes_etudiants[i]])[0]
            ligne.append(moyenne)
            writer.writerow(ligne)



# def rank(list_etudiants,moyenne):
#     etudiant=list(zip(list_etudiants,moyenne))

#     etudiant_tries= sorted(etudiant, key=lambda x:x[1] , reverse=True)
#     rang={}
#     for i ,(nom,moyenne) in enumerate(etudiant_tries,start=1):
#         rang[nom]=i
#     return rang


def mention(moy_g):
    if moy_g > 0 and moy_g < 10:
        print("Mention : Mediocre")
    
    elif (moy_g >=10 and moy_g <12):
        print("Mention : Insuffisant")

    elif (moy_g >=12 and moy_g <14):
        print("Mention : Assez-bien")
    
    elif (moy_g >=14 and moy_g <16):
        print("Mention : Bien")

    elif (moy_g >=16 and moy_g <18):
        print("Mention : Très-bien")  
    else :
        print("Mention : Excellente")


def remplir_information():
    student_dictionnary={}
    for i in list_class[:nbr_remplir]:
        note_list=saisir_note()
    #creer un dictionnaire qui prend comme valeur le nom et le prenom de l'etudiant et comme valeur une liste de ces notes par matiere
    #student_dictionnary=dict(zip(list_class,note_list))
        student_dictionnary[i]=note_list


    for x,y in student_dictionnary.items():
        print(x,y)

    return student_dictionnary


def moyenne_classe_minmax(effectif,moyenne):
    Moyenne_min =min(moyenne)
    Moyenne_max=max(moyenne)
    for i in range(effectif):
        somme= sum(moyenne)
        M=somme/effectif
    return M,Moyenne_min ,Moyenne_max


# list_class=remplir_liste()
# # student=remplir_information()

# # print(list_class)

# #saisir les notes des étudiants
# notes_etu=saisir_note()

# #calcul des moyennes par matiere
# matieres=calcul_mat(notes_etu)

# #calcul des moyennes génerales 
# moyennes=calculer_moyG(matieres)

# sauvegarder_fichier_csv(list_class,notes_etu)

# Collecte des informations des étudiants
etudiants = remplir_information()

# Récupération des noms des étudiants et de leurs notes
noms_etudiants = list(etudiants.keys())
notes_etudiants = list(etudiants.values())

# Appel de la fonction pour sauvegarder les données dans un fichier CSV
sauvegarder_fichier_csv(noms_etudiants, notes_etudiants)






n=[[12,14,5,8,10,17],[8,14,11,10,13,15],[8,14,17,20,19,19]]

moy=calcul_mat(n)
moy_G=calculer_moyG(moy)
#print(moy_G)

# for x in n:
#     moy=0
#     s=0
#     for i in range(0,len(x),2):
#         s= x[i]+x[i+1]
#         #print(s)
#         moy=s/2
#         print(moy)




    